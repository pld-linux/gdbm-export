Summary:	gdbmexport utility to export old GDBM 1.8.x databases
Summary(pl.UTF-8):	Narzędzie gdbmexport pozwalające wyeksportować stare bazy GDBM 1.8.x
Name:		gdbm-export
Version:	1.14.1
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz
# Source0-md5:	c2ddcb3897efa0f57484af2bd4f4f848
Patch0:		gdbm-link.patch
URL:		http://www.gnu.org/software/gdbm/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	gdbm18-devel >= 1.8.3
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	libtool
Requires:	gdbm18 >= 1.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdbmexport utility to export old GDBM 1.8.x databases in order to load
them in new GDBM format.

%description -l pl.UTF-8
Narzędzie gdbmexport pozwalające wyeksportować stare bazy GDBM 1.8.x w
celu wczytania do nowego formatu GDBM.

%prep
%setup -q -n gdbm-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gdbm-export \
	--with-gdbm183-includedir=%{_includedir}/gdbm-1.8 \
	--with-gdbm183-library="-lgdbm-1.8" \
	--without-readline

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# package just gdbmexport, the rest (in newer version) is packaged in gdbm.spec
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{gdbm_dump,gdbm_load,gdbmtool}
%{__rm} -r $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_infodir},%{_localedir},%{_mandir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NOTE-WARNING README
%attr(755,root,root) %{_bindir}/gdbmexport
