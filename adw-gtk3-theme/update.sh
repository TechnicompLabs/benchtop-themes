#!/bin/bash
# SPDX-License-Identifier: MIT
# Moves adw-gtk3-theme.spec to upstream's latest release: Version and the
# checksums of the two remote assets. Prints a commit message line when it
# changes the spec, nothing otherwise.
set -euo pipefail
cd "$(dirname "$0")"
. ../tools/lib.sh
spec=adw-gtk3-theme.spec
tag=$(latest_release lassekongo83/adw-gtk3)
new=${tag#v}
old=$(spec_version "$spec")
[ "$new" = "$old" ] && exit 0
set_version "$spec" "$new"
set_digest "$spec" 0 "https://github.com/lassekongo83/adw-gtk3/releases/download/${tag}/adw-gtk3${tag}.tar.xz"
set_digest "$spec" 1 "https://raw.githubusercontent.com/lassekongo83/adw-gtk3/${tag}/LICENSE"
echo "- adw-gtk3-theme: ${old} -> ${new}"
