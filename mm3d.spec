Summary:	Misfit Model 3D - OpenGL-based 3D model editor
Summary(pl):	Misfit Model 3D - oparty o OpenGL edytor modeli 3D
Name:		mm3d
Version:	1.0.0
Release:	0
Epoch:		0
License:	GPL
Group:		X11/Graphics
Source0:	http://dl.sourceforge.net/misfitmodel3d/%{name}-%{version}.tar.gz
# Source0-md5:	2fd1bc082951bcbb9e3fcfde21c5ad18
URL:		http://www.misfitcode.com/misfitmodel3d/
BuildRequires:	qt-devel >= 3.3.3-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Misfit Model 3D is an OpenGL-based 3D model editor that works with
triangle-based models. It supports multi-level undo, skeletal
animations, simple texturing, scripting, command-line batch
processing, and a plugin system for adding new model and image
filters. Complete online help is included. It is designed to be easy
to use and easy to extend with plugins and scripts.

%description -l pl
Misfit Model 3D to oparty o OpenGL edytor modeli trójwymiarowych
dzia³aj±cy z modelami opartymi na trójk±tach. Obs³uguje wielopoziomowe
undo, animacje szkieletowe, proste teksturowanie, skrypty,
przetwarzanie wsadowe z linii poleceñ oraz system wtyczek do dodawania
nowych filtrów modeli i obrazów. Do³±czona jest kompletna pomoc
online. Edytor jest zaprojektowany z my¶l± o ³atwym u¿ywaniu i
rozszerzaniu przy pomocy wtyczek i skryptów.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	DOCDIR=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_docdir}/%{name}-%{version}
