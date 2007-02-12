# TODO:
# - Ckeck if it requires lua50

Summary:	Misfit Model 3D - OpenGL-based 3D model editor
Summary(pl.UTF-8):   Misfit Model 3D - oparty o OpenGL edytor modeli 3D
Name:		mm3d
Version:	1.1.10
Release:	1
Epoch:		0
License:	GPL
Group:		X11/Graphics
Source0:	http://dl.sourceforge.net/misfitmodel3d/%{name}-%{version}.tar.gz
# Source0-md5:	920363c114f8dcb1229ba5c90ec646fa
URL:		http://www.misfitcode.com/misfitmodel3d/
BuildRequires:	lua50-devel
BuildRequires:	qt-devel >= 3.3.3-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Misfit Model 3D is an OpenGL-based 3D model editor that works with
triangle-based models. It supports multi-level undo, skeletal
animations, simple texturing, scripting, command-line batch
processing, and a plugin system for adding new model and image
filters. Complete online help is included. It is designed to be easy
to use and easy to extend with plugins and scripts.

%description -l pl.UTF-8
Misfit Model 3D to oparty o OpenGL edytor modeli trójwymiarowych
działający z modelami opartymi na trójkątach. Obsługuje wielopoziomowe
undo, animacje szkieletowe, proste teksturowanie, skrypty,
przetwarzanie wsadowe z linii poleceń oraz system wtyczek do dodawania
nowych filtrów modeli i obrazów. Dołączona jest kompletna pomoc
online. Edytor jest zaprojektowany z myślą o łatwym używaniu i
rozszerzaniu przy pomocy wtyczek i skryptów.

%prep
%setup -q

%build
%configure2_13 \
        --with-Qt-include-dir=%{_includedir}/qt \
        --with-Qt-lib-dir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	DOCDIR=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_docdir}/%{name}-%{version}
