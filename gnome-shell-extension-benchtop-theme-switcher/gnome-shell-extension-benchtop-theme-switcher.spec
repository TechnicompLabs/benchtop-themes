#
# spec file for package gnome-shell-extension-benchtop-theme-switcher
# Technicomp Benchtop Linux - switches the GTK 3 and Kvantum themes between
# their light and dark variants with the system's style.
#
# Built directly from git (OBS scmsync, this subdirectory). The extension is
# laid out as a filesystem tree (usr/) that mirrors its install path; the spec
# installs that tree verbatim. It is a fork, kept here with its history, so it
# is not followed by update.sh.
#
%global uuid theme-switcher@technicomplabs.github.io
%global extdir %{_datadir}/gnome-shell/extensions/%{uuid}
Name:           gnome-shell-extension-benchtop-theme-switcher
Version:        1
Release:        0
Summary:        GNOME Shell extension that switches GTK 3 and Kvantum themes to dark
# a fork of Legacy (GTK3) Theme Scheme Auto Switcher by Mukul Joshi, whose
# code says GPL-2.0-or-later and whose repository's LICENSE is the AGPL-3.0;
# TCBL's changes, and the extension as TCBL distributes it, are AGPL-3.0-only
# (GPL-3.0 permits combining with AGPL-3.0 code, section 13)
License:        AGPL-3.0-only
URL:            https://github.com/TechnicompLabs/benchtop-themes
BuildArch:      noarch
Requires:       gnome-shell >= 45

%description
Benchtop Theme Switcher switches the GTK 3 theme (adw-gtk3 and adw-gtk3-dark,
Yaru-blue and Yaru-blue-dark, and so on) and the Kvantum theme of Qt
applications (KvLibadwaita and KvLibadwaitaDark, and so on) between their light
and dark variants when the system's style changes. A fork of Legacy (GTK3)
Theme Scheme Auto Switcher by Mukul Joshi, for Technicomp Benchtop Linux.

%prep

%build

%install
treeroot=
for base in "%{_sourcedir}" "%{_sourcedir}/%{name}-%{version}" "%{_topdir}/SOURCES" "%{_builddir}/%{name}-%{version}" "%{_builddir}" "$PWD"; do
    if [ -d "$base/usr/share/gnome-shell/extensions/%{uuid}" ]; then
        treeroot="$base"
        break
    fi
done
if [ -z "$treeroot" ]; then
    echo "ERROR: file tree (usr/) not found under the build sources" >&2
    exit 1
fi
install -d "%{buildroot}"
( cd "$treeroot" && cp -a --no-preserve=ownership usr "%{buildroot}/" )

%files
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%dir %{extdir}
%{extdir}/extension.js
%{extdir}/metadata.json
%doc %{extdir}/README.md
%license %{extdir}/LICENSE

%changelog
