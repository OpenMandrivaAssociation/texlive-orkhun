# revision 15878
# category Package
# catalog-ctan /fonts/orkhun
# catalog-date 2009-04-22 11:33:20 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-orkhun
Version:	20090422
Release:	2
Summary:	A font for orkhun script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/orkhun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orkhun.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orkhun.doc.tar.xz
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
%{_texmfdistdir}/fonts/source/public/orkhun/orhant.mf
%{_texmfdistdir}/fonts/source/public/orkhun/orhant11.mf
%{_texmfdistdir}/fonts/source/public/orkhun/orhant14.mf
%{_texmfdistdir}/fonts/source/public/orkhun/orhant16.mf
%{_texmfdistdir}/fonts/source/public/orkhun/orhant20.mf
%{_texmfdistdir}/fonts/source/public/orkhun/orhant25.mf
%{_texmfdistdir}/fonts/tfm/public/orkhun/orhant11.tfm
%{_texmfdistdir}/fonts/tfm/public/orkhun/orhant14.tfm
%{_texmfdistdir}/fonts/tfm/public/orkhun/orhant16.tfm
%{_texmfdistdir}/fonts/tfm/public/orkhun/orhant20.tfm
%{_texmfdistdir}/fonts/tfm/public/orkhun/orhant25.tfm
%doc %{_texmfdistdir}/doc/fonts/orkhun/README_Orkhun.txt
%doc %{_texmfdistdir}/doc/fonts/orkhun/rakhimov.pdf
%doc %{_texmfdistdir}/doc/fonts/orkhun/rakhimov.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
