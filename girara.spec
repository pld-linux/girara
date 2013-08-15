Summary:	User interface library
Name:		girara
Version:	0.1.7
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://pwmt.org/projects/girara/download/%{name}-%{version}.tar.gz
# Source0-md5:	ff73bf26b56cdc28a4a2dcce46f4aa20
URL:		http://pwmt.org/projects/girara
BuildRequires:	gtk+2-devel >= 2:2.18.6
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
girara is a library that implements a user interface that focuses on
simplicity and minimalism. Currently based on GTK+, a cross-platform
widget toolkit, it provides an interface that focuses on three main
components: A so-called view widget that represents the actual
application (e.g. a website (browser), an image (image viewer) or the
document (document viewer)), an input bar that is used to execute
commands of the application and the status bar which provides the user
with current information. girara was designed to replace and enhance
the user interface that is used by zathura and jumanji and other
features that those applications share.

%package devel
Summary:	Header files for girara library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for girara library.

%package static
Summary:	Static girara library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static girara library.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%find_lang libgirara-gtk2-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgirara-gtk2-1.lang
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libgirara-gtk2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgirara-gtk2.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgirara-gtk2.so
%{_includedir}/girara
%{_pkgconfigdir}/girara-gtk2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgirara-gtk2.a
