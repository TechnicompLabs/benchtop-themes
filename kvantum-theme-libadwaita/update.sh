#!/bin/bash
# SPDX-License-Identifier: MIT
# Moves kvantum-theme-libadwaita.spec to upstream's newest commit: the commit, its date, Version
# and the checksum of the remote asset. Prints a commit message line when it
# changes the spec, nothing otherwise.
set -euo pipefail
cd "$(dirname "$0")"
. ../tools/lib.sh
spec=kvantum-theme-libadwaita.spec
read -r sha date < <(latest_commit GabePoel/KvLibadwaita)
old=$(sed -n 's/^%global commit[[:space:]]\+//p' "$spec")
[ "$sha" = "$old" ] && exit 0
set_global "$spec" commit "$sha"
set_global "$spec" shortcommit "${sha:0:7}"
set_global "$spec" commitdate "$date"
set_digest "$spec" 0 "https://github.com/GabePoel/KvLibadwaita/archive/${sha}.tar.gz"
echo "- kvantum-theme-libadwaita: ${old:0:7} -> ${sha:0:7}"
