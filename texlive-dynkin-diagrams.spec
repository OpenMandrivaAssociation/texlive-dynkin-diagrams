Name:		texlive-dynkin-diagrams
Version:	67267
Release:	1
Summary:	Draw Dynkin, Coxeter, and Satake diagrams using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dynkin-diagrams
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynkin-diagrams.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynkin-diagrams.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Draws Dynkin, Coxeter, and Satake diagrams in LaTeX documents,
using the TikZ package. The package requires amsmath, amssymb,
etoolbox, expl3, mathtools, pgfkeys, pgfopts, TikZ, xparse, and
xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dynkin-diagrams
%doc %{_texmfdistdir}/doc/latex/dynkin-diagrams

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
