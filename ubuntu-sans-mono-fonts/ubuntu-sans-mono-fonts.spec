#
# spec file for package ubuntu-sans-mono-fonts
# Technicomp Benchtop Linux - Ubuntu Sans Mono, from upstream's GitHub release.
#
# Two packages, which conflict so that the family is never listed twice:
# ubuntu-sans-mono-fonts, the variable fonts (every weight, installed by default), and
# ubuntu-sans-mono-static-fonts, the same family as static TrueType files, one per style.
# The release's OpenType and web fonts are the same designs again and are
# left out.
#
# Built from git (OBS scmsync, this subdirectory). The source is a remote
# asset that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves Version and the checksum to a new
# release.
#
Name:           ubuntu-sans-mono-fonts
Version:        1.100
Release:        0
Summary:        Ubuntu Sans Mono, variable fonts
License:        Ubuntu-font-1.0
URL:            https://github.com/canonical/Ubuntu-Sans-Mono-fonts
#!RemoteAsset: sha256:0e459ed18b552190971561b3e474d0c4583db40483debf9e951321c2a1c2dec8
Source0:        https://github.com/canonical/Ubuntu-Sans-Mono-fonts/releases/download/v%{version}/Ubuntu-Sans-Mono-fonts-v%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Conflicts:      ubuntu-sans-mono-static-fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Ubuntu Sans Mono is the monospaced typeface of Ubuntu, a revision of Ubuntu
Mono to match Ubuntu Sans.

This package has the variable fonts, which cover every weight.

%package -n ubuntu-sans-mono-static-fonts
Summary:        Ubuntu Sans Mono, static fonts
Conflicts:      ubuntu-sans-mono-fonts
%reconfigure_fonts_prereq

%description -n ubuntu-sans-mono-static-fonts
Ubuntu Sans Mono is the monospaced typeface of Ubuntu, a revision of Ubuntu
Mono to match Ubuntu Sans.

This package has the static TrueType fonts, one file per style.

%prep
%autosetup -n Ubuntu-Sans-Mono-fonts-v%{version}

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 0644 fonts/variable/*.ttf fonts/ttf/*.ttf %{buildroot}%{_ttfontsdir}/
# the static files, by name (the variable files' names contain brackets)
for f in fonts/ttf/*.ttf; do echo "%{_ttfontsdir}/${f##*/}"; done > static.files

%reconfigure_fonts_scriptlets
%reconfigure_fonts_scriptlets -n ubuntu-sans-mono-static-fonts

%files
%license LICENCE.txt
%{_ttfontsdir}/UbuntuSansMono*wght*.ttf

%files -n ubuntu-sans-mono-static-fonts -f static.files
%license LICENCE.txt

%changelog
