# revision 25896
# category Package
# catalog-ctan /fonts/junicode
# catalog-date 2012-04-09 14:52:28 +0200
# catalog-license gpl
# catalog-version 0.7.6
Name:		texlive-junicode
Version:	0.7.6
Release:	2
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


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.6-1
+ Revision: 790632
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7.1-1
+ Revision: 770188
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6.17-2
+ Revision: 752935
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6.17-1
+ Revision: 718759
- texlive-junicode
- texlive-junicode
- texlive-junicode
- texlive-junicode

