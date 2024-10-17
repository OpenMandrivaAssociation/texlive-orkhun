Name:		texlive-orkhun
Version:	15878
Release:	2
Summary:	A font for orkhun script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/orkhun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orkhun.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orkhun.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font covers an old Turkic script. It is provided as
MetaFont source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/orkhun
%{_texmfdistdir}/fonts/tfm/public/orkhun
%doc %{_texmfdistdir}/doc/fonts/orkhun

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
