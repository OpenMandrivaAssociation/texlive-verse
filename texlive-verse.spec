%global tl_name verse
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4c
Release:	%{tl_revision}.1
Summary:	Aids for typesetting simple verse
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/verse
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verse.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verse.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verse.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package documentation discusses approaches to the problem; the
package is strong on layout, from simple alternate-line indentation to
the Mouse's tale from Alice in Wonderland.

