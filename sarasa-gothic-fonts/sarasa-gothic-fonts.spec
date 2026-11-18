#
# spec file for package sarasa-gothic-fonts
# Technicomp Benchtop Linux - Sarasa Gothic, from upstream's GitHub release:
# every family, orthography and weight, as TrueType collections (hinted).
#
# Built from git (OBS scmsync, this subdirectory). The sources are remote
# assets that OBS downloads from GitHub; update.sh, run daily by the
# repository's GitHub Actions job, moves Version and the checksums to a new
# release.
#
Name:           sarasa-gothic-fonts
Version:        1.0.43
Release:        0
Summary:        Sarasa Gothic, CJK programming fonts
License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
#!RemoteAsset: sha256:3f93cd32b977e7f777880672eb26b839d0db447f66284117018c7b7e42f05ff2
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/Sarasa-TTC-%{version}.7z
# the release has no license file
#!RemoteAsset: sha256:32c932e0dbae4f6e6386964bbc2d04178707665a05ca65cf636241af13d50a53
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE
BuildRequires:  7zip
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Sarasa Gothic pairs Source Han Sans' Chinese, Japanese and Korean characters
with Inter's Latin letters in Sarasa Gothic and Sarasa UI, and with Iosevka's
in the monospaced families, where each CJK character is exactly two Latin
letters wide: Mono, Term (for terminals) and Fixed (Term without ligatures),
and their Slab versions. Each family comes in Simplified, Traditional, Hong
Kong and Classical Chinese, Japanese and Korean forms.

%prep
%setup -q -c -T
7z x -bd %{SOURCE0}
cp %{SOURCE1} LICENSE

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttc %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/Sarasa-*.ttc

%changelog
