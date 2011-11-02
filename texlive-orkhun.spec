Name:		texlive-orkhun
Version:	20090422
Release:	1
Summary:	A font for orkhun script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/orkhun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orkhun.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orkhun.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The font covers an old Turkic script. It is provided as
MetaFont source.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
