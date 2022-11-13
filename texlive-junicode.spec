Name:		texlive-junicode
Version:	61719
Release:	1
Summary:	A TrueType font for mediaevalists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/junicode
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/junicode
%{_texmfdistdir}/fonts/map/dvips/junicode
%{_texmfdistdir}/fonts/tfm/public/junicode
%{_texmfdistdir}/fonts/truetype/public/junicode
%{_texmfdistdir}/fonts/vf/public/junicode
%{_texmfdistdir}/tex/latex/junicode
%doc %{_texmfdistdir}/doc/fonts/junicode

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
