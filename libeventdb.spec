Summary:	GPE Event Database library
Summary(pl.UTF-8):	Biblioteka bazy danych zdarzeń GPE
Name:		libeventdb
Version:	0.30
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	aeab2ac484b9cbb5a950f1f4ca2a32ad
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libgpewidget-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE Event Database library.

%description -l pl.UTF-8
Biblioteka bazy danych zdarzeń GPE.

%package devel
Summary:	Header files for libeventdb
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libeventdb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	libgpewidget-devel
Requires:	sqlite-devel

%description devel
Header files for libeventdb.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libeventdb.

%package static
Summary:	Static libeventdb library
Summary(pl.UTF-8):	Statyczna biblioteka libeventdb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libeventdb library.

%description static -l pl.UTF-8
Statyczna biblioteka libeventdb.

%package apidocs
Summary:	libeventdb API documentation
Summary(pl.UTF-8):	Dokumentacja API libeventdb
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libeventdb API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libeventdb.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libeventdb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeventdb.so
%{_libdir}/libeventdb.la
%{_includedir}/gpe/event-db.h
%{_pkgconfigdir}/libeventdb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libeventdb.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libeventdb
