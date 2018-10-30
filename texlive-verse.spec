# revision 34017
# category Package
# catalog-ctan /macros/latex/contrib/verse
# catalog-date 2014-05-10 11:58:31 +0200
# catalog-license lppl
# catalog-version 2.4b
Name:		texlive-verse
Version:	2.4b
Release:	6
Summary:	Aids for typesetting simple verse
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verse
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verse.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verse.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verse.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package documentation discusses approaches to the problem;
the package is strong on layout, from simple alternate-line
indentation to the Mouse's tale from Alice in Wonderland.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verse/verse.sty
%doc %{_texmfdistdir}/doc/latex/verse/README
%doc %{_texmfdistdir}/doc/latex/verse/verse.pdf
#- source
%doc %{_texmfdistdir}/source/latex/verse/verse.dtx
%doc %{_texmfdistdir}/source/latex/verse/verse.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
