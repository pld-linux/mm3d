Summary:	Misfit Model 3D
Summary(pl):	Misfit Model 3D
Name:		mm3d
Version:	1.0.0
Release:	0
Epoch:		0
License:	GPL
Group:		X11/Graphics
#Vendor:		-
#Icon:		-
Source0:	http://dl.sourceforge.net/misfitmodel3d/%{name}-%{version}.tar.gz
# Source0-md5:	2fd1bc082951bcbb9e3fcfde21c5ad18
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-what.patch
#URL:		-
BuildRequires:	qt-devel >= 3.3.3-4
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-

#%description subpackage

#%description subpackage -l pl

%prep
%setup -q
#%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	DOCDIR=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/doc/%{name}-%{version}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
