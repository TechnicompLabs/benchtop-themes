#!/bin/bash
# SPDX-License-Identifier: MIT
# Moves ubuntu-sans-fonts.spec to upstream's latest release: Version and the checksum of
# the remote asset. Prints a commit message line when it changes the spec,
# nothing otherwise.
set -euo pipefail
cd "$(dirname "$0")"
. ../tools/lib.sh
spec=ubuntu-sans-fonts.spec
tag=$(latest_release canonical/Ubuntu-Sans-fonts)
new=${tag#v}
new=${new#.}
old=$(spec_version "$spec")
[ "$new" = "$old" ] && exit 0
set_version "$spec" "$new"
set_digest "$spec" 0 "https://github.com/canonical/Ubuntu-Sans-fonts/releases/download/${tag}/$(sed -n 's|^Source0:.*/||p' "$spec" | sed "s/%{version}/$new/g")"
echo "- ubuntu-sans-fonts: ${old} -> ${new}"
