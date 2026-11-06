# benchtop-themes

Technicomp Benchtop Linux packaging of desktop themes and fonts, each built from its upstream on GitHub. Each subdirectory is one OBS package in home:technicomp:benchtop, connected by scmsync (`?subdir=`).

| Directory | Upstream | Follows |
|---|---|---|
| `adw-gtk3-theme/` | [adw-gtk3](https://github.com/lassekongo83/adw-gtk3) | releases |
| `yaru-theme/` | [Yaru](https://github.com/ubuntu/yaru) (takes the place of openSUSE's older yaru-theme) | release tags (X.Y.Z) |
| `kvantum-theme-libadwaita/` | [KvLibadwaita](https://github.com/GabePoel/KvLibadwaita) | commits (no releases) |
| `kvantum-theme-yaru-colors/` | [KvYaru-Colors](https://github.com/GabePoel/KvYaru-Colors) | commits (no releases) |
| `ubuntu-sans-fonts/` | [Ubuntu Sans](https://github.com/canonical/Ubuntu-Sans-fonts) | releases |
| `ubuntu-sans-mono-fonts/` | [Ubuntu Sans Mono](https://github.com/canonical/Ubuntu-Sans-Mono-fonts) | releases |
| `kvantum/` | [Kvantum](https://github.com/tsujan/Kvantum), openSUSE Factory's package with TCBL's patch for the `kvantum-auto` style key, which follows the desktop's color scheme (`kvantum-auto-color-scheme.patch`); the TCBL repository's priority puts it above openSUSE's | releases |
| `gnome-shell-extension-benchtop-theme-switcher/` | Benchtop Theme Switcher, TCBL's fork of [Legacy (GTK3) Theme Scheme Auto Switcher](https://github.com/mukul29/legacy-theme-auto-switcher-gnome-extension), with its history; it also switches the Kvantum theme | not followed (a fork; its source is here) |

The sources are not kept here. Each spec names them as remote assets (`#!RemoteAsset: sha256:…` before a `Source:` URL), which OBS downloads from GitHub and checks before building.

Updates: the GitHub Actions job `.github/workflows/follow-upstream.yml` runs every package's `update.sh` once a day. A script that finds a newer upstream release (or commit) sets the spec's Version and checksums, and the job commits and pushes; the push reaches OBS through the organization's webhook and `.obs/workflows.yml`. The scripts share `tools/lib.sh` and can be run by hand the same way.

A new Kvantum release that the patch no longer applies to fails at `%prep` on OBS; the patch is then updated by hand.

Each font family is two packages that conflict, so that it is never listed twice: the variable fonts (installed by default) and the static TrueType fonts.
