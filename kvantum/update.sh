#!/bin/bash
# SPDX-License-Identifier: MIT
# Moves kvantum.spec to upstream's latest release: Version and the checksum
# of the remote asset. Prints a commit message line when it changes the spec,
# nothing otherwise. If the TCBL patch no longer applies to the new release,
# the OBS build fails at %prep and the patch has to be updated by hand.
set -euo pipefail
cd "$(dirname "$0")"
. ../tools/lib.sh
spec=kvantum.spec
tag=$(latest_release tsujan/Kvantum)
new=${tag#V}
old=$(spec_version "$spec")
[ "$new" = "$old" ] && exit 0
set_version "$spec" "$new"
set_digest "$spec" 0 "https://github.com/tsujan/Kvantum/releases/download/${tag}/Kvantum-${new}.tar.xz"
echo "- kvantum: ${old} -> ${new}"
