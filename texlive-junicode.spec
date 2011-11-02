Name:		texlive-junicode
Version:	0.6.17
Release:	1
Summary:	A TrueType font for mediaevalists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/junicode
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Junicode is a TrueType font with many OpenType features. As
such, it works well with Xe(La)TeX.

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
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/junicode/Junicode-Regular.ttf
%doc %{_texmfdistdir}/doc/fonts/junicode/Junicode.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/Junicode.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/License.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/License.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/README
%doc %{_texmfdistdir}/doc/fonts/junicode/aelfric_job.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/aelfric_job.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/mufi.pdf
%doc %{_texmfdistdir}/doc/fonts/junicode/mufi.tex
%doc %{_texmfdistdir}/doc/fonts/junicode/replacements

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
