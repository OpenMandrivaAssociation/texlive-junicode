# revision 28286
# category Package
# catalog-ctan /fonts/junicode
# catalog-date 2012-11-17 16:00:23 +0100
# catalog-license gpl
# catalog-version 0.7.7
Name:		texlive-junicode
Version:	0.7.7
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
Junicode is a TrueType font with many OpenType features for
antiquarians (especially medievalists) based on typefaces used
by the Oxford Press in the late 17th and early 18th centuries.
It works well with Xe(La)TeX.

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
%doc %{_texmfdistdir}/doc/fonts/junicode/aelfric_job.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/aelfric_job.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/fleurons
%doc %{_texmfdistdir}/doc/fonts/junicode/homer_sample.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/homer_sample.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/replacements

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
