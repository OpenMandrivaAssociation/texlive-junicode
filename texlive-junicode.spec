%global tl_name junicode
%global tl_revision 77682
%global tl_version 2.218

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A TrueType and OpenType font family for mediaevalists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/junicode
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/junicode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Junicode is a TrueType/OpenType font family with many features for
antiquarians (especially medievalists) based on typefaces used by the
Oxford Press in the late 17th and early 18th centuries. It works well
with Lua(La)TeX or Xe(La)TeX, but the basic textual features are also
available with (pdf)LaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from junicode:
Map Junicode.map
TL_DROPIN_EOF
