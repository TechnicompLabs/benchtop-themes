#
# spec file for package ubuntu-sans-fonts
# Technicomp Benchtop Linux - Ubuntu Sans, from upstream's GitHub release.
#
# Two packages, which conflict so that the family is never listed twice:
# ubuntu-sans-fonts, the variable fonts (every weight, installed by default), and
# ubuntu-sans-static-fonts, the same family as static TrueType files, one per style.
# The release's OpenType and web fonts are the same designs again and are
# left out.
#
# Built from git (OBS scmsync, this subdirectory). The source is a remote
# asset that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves Version and the checksum to a new
# release.
#
Name:           ubuntu-sans-fonts
Version:        1.006
Release:        0
Summary:        Ubuntu Sans, variable fonts
License:        Ubuntu-font-1.0
URL:            https://github.com/canonical/Ubuntu-Sans-fonts
#!RemoteAsset: sha256:20aa7af47beaa6d64327782f7bf60df375edeedbdee2fe407e0bf9721890fb83
Source0:        https://github.com/canonical/Ubuntu-Sans-fonts/releases/download/v%{version}/UbuntuSans-fonts-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Conflicts:      ubuntu-sans-static-fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Ubuntu Sans is the sans-serif typeface of Ubuntu, a revision of the Ubuntu font
family with added widths and weights.

This package has the variable fonts, which cover every weight.

%package -n ubuntu-sans-static-fonts
Summary:        Ubuntu Sans, static fonts
Conflicts:      ubuntu-sans-fonts
%reconfigure_fonts_prereq

%description -n ubuntu-sans-static-fonts
Ubuntu Sans is the sans-serif typeface of Ubuntu, a revision of the Ubuntu font
family with added widths and weights.

This package has the static TrueType fonts, one file per style.

%prep
%autosetup -n UbuntuSans-fonts-%{version}

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 0644 variable/*.ttf ttf/*.ttf %{buildroot}%{_ttfontsdir}/
# the static files, by name (the variable files' names contain brackets)
for f in ttf/*.ttf; do echo "%{_ttfontsdir}/${f##*/}"; done > static.files

%reconfigure_fonts_scriptlets
%reconfigure_fonts_scriptlets -n ubuntu-sans-static-fonts

%files
%license LICENCE.txt
%{_ttfontsdir}/UbuntuSans*wght*.ttf

%files -n ubuntu-sans-static-fonts -f static.files
%license LICENCE.txt

%changelog
