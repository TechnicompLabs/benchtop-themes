#
# spec file for package adw-gtk3-theme
# Technicomp Benchtop Linux - adw-gtk3, built from its GitHub release.
#
# Built from git (OBS scmsync, this subdirectory). The sources are remote
# assets that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves Version and the checksums to a new
# release.
#
Name:           adw-gtk3-theme
Version:        6.5
Release:        0
Summary:        GTK 3 port of the libadwaita style
License:        LGPL-2.1-only
URL:            https://github.com/lassekongo83/adw-gtk3
#!RemoteAsset: sha256:a81780fadfc432be0fc3d89c4ebb41aa28e4f032d42c36f9789c57dd10cfa41c
Source0:        https://github.com/lassekongo83/adw-gtk3/releases/download/v%{version}/adw-gtk3v%{version}.tar.xz
# the release archive carries the themes only
#!RemoteAsset: sha256:20c17d8b8c48a600800dfd14f95d5cb9ff47066a9641ddeab48dc54aec96e331
Source1:        https://raw.githubusercontent.com/lassekongo83/adw-gtk3/v%{version}/LICENSE
BuildArch:      noarch

%description
adw-gtk3 is an unofficial GTK 3 port of libadwaita, the style of GNOME's own
applications, so that GTK 3 applications match libadwaita applications. It
has a light theme (adw-gtk3) and a dark theme (adw-gtk3-dark), each with GTK
3 and GTK 4 styles.

%prep
%setup -q -c -n adw-gtk3-%{version}
cp %{SOURCE1} LICENSE

%build

%install
install -d %{buildroot}%{_datadir}/themes
cp -a adw-gtk3 adw-gtk3-dark %{buildroot}%{_datadir}/themes/

%files
%license LICENSE
%{_datadir}/themes/adw-gtk3/
%{_datadir}/themes/adw-gtk3-dark/

%changelog
