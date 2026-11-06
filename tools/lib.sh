# SPDX-License-Identifier: MIT
# shellcheck shell=bash
# Helpers for the packages' update.sh scripts (sourced). They need curl,
# python3 and sha256sum; GH_TOKEN, when set, is used for GitHub's API.

gh_api() {
    local auth=()
    [ -n "${GH_TOKEN:-}" ] && auth=(-H "Authorization: Bearer ${GH_TOKEN}")
    curl -sSfL -m 60 "${auth[@]}" -H "Accept: application/vnd.github+json" "https://api.github.com/$1"
}

# the tag of a repository's latest release
latest_release() {
    gh_api "repos/$1/releases/latest" | python3 -c 'import json,sys; print(json.load(sys.stdin)["tag_name"])'
}

# the highest tag matching a regular expression (by version order)
latest_tag() {
    gh_api "repos/$1/tags?per_page=100" | python3 -c '
import json, re, sys
pat = re.compile(sys.argv[1])
tags = [t["name"] for t in json.load(sys.stdin) if pat.fullmatch(t["name"])]
key = lambda s: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)]
print(max(tags, key=key))' "$2"
}

# "SHA YYYYMMDD" of the newest commit on a repository's default branch
latest_commit() {
    gh_api "repos/$1/commits?per_page=1" | python3 -c '
import json, sys
c = json.load(sys.stdin)[0]
print(c["sha"], c["commit"]["committer"]["date"][:10].replace("-", ""))'
}

spec_version() {
    sed -n 's/^Version:[[:space:]]*//p' "$1" | head -1
}

set_version() {
    sed -i "s/^\(Version:[[:space:]]*\).*/\1$2/" "$1"
}

# set_global SPEC NAME VALUE: the value of a "%global NAME VALUE" line
set_global() {
    sed -i "s/^\(%global[[:space:]]\+$2[[:space:]]\+\).*/\1$3/" "$1"
}

# set_digest SPEC N URL: downloads URL and writes its checksum into the
# "#!RemoteAsset: sha256:..." line just before SourceN
set_digest() {
    local sum
    sum=$(curl -sSfL -m 600 "$3" | sha256sum | cut -d' ' -f1)
    python3 - "$1" "$2" "$sum" <<'PYEOF'
import re, sys
spec, n, digest = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(spec).read().split("\n")
for i, line in enumerate(lines):
    if re.match(r"Source%s:" % n, line) or (n == "0" and re.match(r"Source:", line)):
        if i == 0 or not lines[i - 1].startswith("#!RemoteAsset"):
            sys.exit("%s: no #!RemoteAsset line before Source%s" % (spec, n))
        lines[i - 1] = "#!RemoteAsset: sha256:" + digest
        break
else:
    sys.exit("%s: Source%s not found" % (spec, n))
open(spec, "w").write("\n".join(lines))
PYEOF
}
