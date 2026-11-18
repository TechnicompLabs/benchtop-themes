#!/bin/bash
# SPDX-License-Identifier: MIT
# Moves sarasa-gothic-fonts.spec to upstream's latest release: Version and the
# checksums of the remote assets. Prints a commit message line when it changes
# the spec, nothing otherwise.
set -euo pipefail
cd "$(dirname "$0")"
. ../tools/lib.sh
spec=sarasa-gothic-fonts.spec
repo=be5invis/Sarasa-Gothic
tag=$(latest_release "$repo")
new=${tag#v}
old=$(spec_version "$spec")
[ "$new" = "$old" ] && exit 0
set_version "$spec" "$new"
set_digest "$spec" 0 "https://github.com/${repo}/releases/download/${tag}/Sarasa-TTC-${new}.7z"
set_digest "$spec" 1 "https://raw.githubusercontent.com/${repo}/${tag}/LICENSE"
echo "- sarasa-gothic-fonts: ${old} -> ${new}"
