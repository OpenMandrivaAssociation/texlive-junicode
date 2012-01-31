# revision 25191
# category Package
# catalog-ctan /fonts/junicode
# catalog-date 2012-01-23 23:37:37 +0100
# catalog-license gpl
# catalog-version 0.7.1
Name:		texlive-junicode
Version:	0.7.1
Release:	1
Summary:	A TrueType font for mediaevalists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/junicode
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Junicode is a TrueType font with many OpenType features, that
works well with Xe(La)TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode.ttf
%{_texmfdistdir}/tex/latex/junicode/mt-Junicode.cfg
%doc %{_texmfdistdir}/doc/fonts/junicode/Junicode.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/Junicode.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/README
%doc %{_texmfdistdir}/doc/fonts/junicode/mufi.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/mufi.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/replacements

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
