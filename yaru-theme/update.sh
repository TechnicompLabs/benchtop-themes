#!/bin/bash
# SPDX-License-Identifier: MIT
# Moves yaru-theme.spec to upstream's highest release tag (X.Y.Z; Yaru's
# packaging tags such as 26.10.3ubuntu are skipped): Version and the
# checksum of the remote asset. Prints a commit message line when it changes
# the spec, nothing otherwise.
set -euo pipefail
cd "$(dirname "$0")"
. ../tools/lib.sh
spec=yaru-theme.spec
new=$(latest_tag ubuntu/yaru '[0-9]+\.[0-9]+\.[0-9]+')
old=$(spec_version "$spec")
[ "$new" = "$old" ] && exit 0
set_version "$spec" "$new"
set_digest "$spec" 0 "https://github.com/ubuntu/yaru/archive/${new}.tar.gz"
echo "- yaru-theme: ${old} -> ${new}"
