#
# spec file for package kvantum-theme-libadwaita
# Technicomp Benchtop Linux - KvLibadwaita, a Kvantum theme, from upstream's latest
# commit (the project has no releases).
#
# Built from git (OBS scmsync, this subdirectory). The source is a remote
# asset that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves the commit, Version and the checksum
# to upstream's newest commit.
#
%global commit 1f4e0bec44b13dabfa1fe4047aa8eeaccf2f3557
%global shortcommit 1f4e0be
%global commitdate 20250913
Name:           kvantum-theme-libadwaita
Version:        0+git%{commitdate}.%{shortcommit}
Release:        0
Summary:        Kvantum theme matching libadwaita
License:        GPL-3.0-only
URL:            https://github.com/GabePoel/KvLibadwaita
#!RemoteAsset: sha256:ec9062ee7e283bd989464c2315a488f71ef93a96b69d5e71b8794239a7ac2790
Source0:        https://github.com/GabePoel/KvLibadwaita/archive/%{commit}.tar.gz#/KvLibadwaita-%{shortcommit}.tar.gz
Requires:       (kvantum-qt6 or kvantum-qt5)
BuildArch:      noarch

%description
KvLibadwaita is a Kvantum theme for Qt applications that matches libadwaita,
the style of GNOME's own applications, and adw-gtk3, in light (KvLibadwaita)
and dark (KvLibadwaitaDark) variants. It also carries matching KDE color
schemes.

%prep
%autosetup -n KvLibadwaita-%{commit}

%build

%install
install -d %{buildroot}%{_datadir}/Kvantum %{buildroot}%{_datadir}/color-schemes
cp -a src/KvLibadwaita %{buildroot}%{_datadir}/Kvantum/
install -m 0644 src/Colors/*.colors %{buildroot}%{_datadir}/color-schemes/

%files
%license LICENSE
%doc README.md CREDITS
%dir %{_datadir}/Kvantum
%{_datadir}/Kvantum/KvLibadwaita/
%dir %{_datadir}/color-schemes
%{_datadir}/color-schemes/Libadwaita*.colors

%changelog
