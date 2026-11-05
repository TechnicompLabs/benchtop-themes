#
# spec file for package kvantum-theme-yaru-colors
# Technicomp Benchtop Linux - KvYaru-Colors, a Kvantum theme, from upstream's latest
# commit (the project has no releases).
#
# Built from git (OBS scmsync, this subdirectory). The source is a remote
# asset that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves the commit, Version and the checksum
# to upstream's newest commit.
#
%global commit a43fe9ab9fcee922dfeb64d5c28155d890cde719
%global shortcommit a43fe9a
%global commitdate 20211127
Name:           kvantum-theme-yaru-colors
Version:        0+git%{commitdate}.%{shortcommit}
Release:        0
Summary:        Kvantum themes matching Yaru's colors
License:        GPL-3.0-only
URL:            https://github.com/GabePoel/KvYaru-Colors
#!RemoteAsset: sha256:a21d45d948d55880b2ea786cd4d0f0909eb6c5f9e39a7d9b7cec457c69d21649
Source0:        https://github.com/GabePoel/KvYaru-Colors/archive/%{commit}.tar.gz#/KvYaru-Colors-%{shortcommit}.tar.gz
Requires:       (kvantum-qt6 or kvantum-qt5)
BuildArch:      noarch

%description
KvYaru-Colors is a set of Kvantum themes for Qt applications that match Yaru,
Ubuntu's theme, in its accent colors, each in light and dark variants.

%prep
%autosetup -n KvYaru-Colors-%{commit}

%build

%install
install -d %{buildroot}%{_datadir}/Kvantum
cp -a src/KvYaru-* %{buildroot}%{_datadir}/Kvantum/

%files
%license LICENSE
%doc README.md CREDITS
%dir %{_datadir}/Kvantum
# the themes, and upstream's links from each KvYaru-<color>Light name to its theme
%{_datadir}/Kvantum/KvYaru-*

%changelog
