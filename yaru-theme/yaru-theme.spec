#
# spec file for package yaru-theme
# Technicomp Benchtop Linux - Yaru, Ubuntu's themes, from upstream's latest
# release. It takes the place of openSUSE's yaru-theme (24.04.0, April 2024):
# the subpackages have the same names and newer versions.
#
# Built from git (OBS scmsync, this subdirectory). The source is a remote
# asset that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves Version and the checksum to a new
# release.
#
Name:           yaru-theme
Version:        26.10.3
Release:        0
Summary:        Yaru, Ubuntu's themes
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://github.com/ubuntu/yaru
#!RemoteAsset: sha256:ac396932559dd1b515ee4d94d470093dfac407027d9609e756299df9e06c3f7b
Source0:        https://github.com/ubuntu/yaru/archive/%{version}.tar.gz#/yaru-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  glib2-tools
BuildRequires:  meson >= 1.4.0
BuildRequires:  python3
BuildRequires:  sassc
BuildRequires:  pkgconfig(gio-2.0)
BuildArch:      noarch

%description
Yaru is the theme of Ubuntu: GTK 3 and GTK 4 themes, a GNOME Shell theme,
icons and cursors, sounds and GtkSourceView styles, each in Ubuntu's accent
colors and in light and dark variants.

%package -n metatheme-yaru-common
Summary:        Common files of the Yaru themes
Recommends:     sound-theme-yaru
Recommends:     yaru-icon-theme

%description -n metatheme-yaru-common
The theme descriptions of Yaru, Ubuntu's themes, in each accent color.

%package -n gtk3-metatheme-yaru
Summary:        Yaru for GTK 3
Requires:       gtk3
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gtk3)

%description -n gtk3-metatheme-yaru
The GTK 3 style of Yaru, Ubuntu's theme, in each accent color, light and dark.

%package -n gtk4-metatheme-yaru
Summary:        Yaru for GTK 4
Requires:       gtk4
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gtk4)

%description -n gtk4-metatheme-yaru
The GTK 4 style of Yaru, Ubuntu's theme, in each accent color, light and dark,
for GTK 4 applications that do not use libadwaita.

%package -n gnome-shell-theme-yaru
Summary:        Yaru for GNOME Shell, and the Yaru session
Requires:       gnome-shell >= 46
Requires:       metatheme-yaru-common = %{version}
Supplements:    (metatheme-yaru-common and gnome-shell)

%description -n gnome-shell-theme-yaru
The GNOME Shell theme of Yaru, Ubuntu's theme, and a "Yaru" session in the
login screen's session list, which runs GNOME with the Yaru shell, GTK, icon,
cursor and sound themes (upstream's session for trying Yaru out).

%package -n metacity-theme-yaru
Summary:        Yaru for Metacity
Requires:       metatheme-yaru-common = %{version}

%description -n metacity-theme-yaru
The Metacity (GNOME Flashback) window decorations of Yaru, Ubuntu's theme.

%package -n gtksourceview-theme-yaru
Summary:        Yaru styles for GtkSourceView

%description -n gtksourceview-theme-yaru
The light and dark Yaru styles for text editors that use GtkSourceView.

%package -n yaru-icon-theme
Summary:        Yaru icons and cursors
License:        CC-BY-SA-4.0
Requires:       hicolor-icon-theme

%description -n yaru-icon-theme
The icons and cursors of Yaru, Ubuntu's theme, in each accent color, light and
dark.

%package -n sound-theme-yaru
Summary:        Yaru sounds
License:        CC-BY-SA-4.0

%description -n sound-theme-yaru
The sound theme of Yaru, Ubuntu's theme.

%prep
%autosetup -n yaru-%{version}

%build
%meson
%meson_build

%install
%meson_install
# Ubuntu Dock's style; TCBL does not ship Ubuntu Dock
rm %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css
rmdir %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com %{buildroot}%{_datadir}/gnome-shell/extensions
%fdupes %{buildroot}%{_datadir}

%files -n metatheme-yaru-common
%license COPYING COPYING.LGPL-2.1 COPYING.LGPL-3.0 LICENSE_CCBYSA
%doc AUTHORS CONTRIBUTING.md README.md
%dir %{_datadir}/themes/Yaru*/
%{_datadir}/themes/Yaru*/index.theme

%files -n gtk3-metatheme-yaru
%{_datadir}/themes/Yaru*/gtk-3.0/

%files -n gtk4-metatheme-yaru
%{_datadir}/themes/Yaru*/gtk-4.0/

%files -n gnome-shell-theme-yaru
%{_datadir}/themes/Yaru*/gnome-shell
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/theme
%{_datadir}/gnome-shell/theme/Yaru*/
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/yaru.json
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/Yaru.desktop
# GSettings for the Yaru session only (desktop name Yaru)
%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override

%files -n metacity-theme-yaru
%{_datadir}/themes/Yaru{,-dark}/metacity-1/

%files -n gtksourceview-theme-yaru
%{_datadir}/gtksourceview-*/
%{_datadir}/libgedit-gtksourceview-300/

%files -n yaru-icon-theme
%license COPYING LICENSE_CCBYSA
%{_datadir}/icons/Yaru*/

%files -n sound-theme-yaru
%license COPYING LICENSE_CCBYSA
%{_datadir}/sounds/Yaru/

%changelog
