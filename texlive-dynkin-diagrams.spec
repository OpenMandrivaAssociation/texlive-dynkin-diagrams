%global tl_name dynkin-diagrams
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.141592653589793238462
Release:	%{tl_revision}.1
Summary:	Draw Dynkin, Coxeter, and Satake diagrams using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/dynkin-diagrams
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dynkin-diagrams.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dynkin-diagrams.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Draws Dynkin, Coxeter, and Satake diagrams in LaTeX documents, using the
TikZ package. The package requires amsmath, amssymb, etoolbox, expl3,
mathtools, pgfkeys, pgfopts, TikZ, xparse, and xstring.

