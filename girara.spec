Summary:	User interface library
Name:		girara
Version:	0.2.6
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://pwmt.org/projects/girara/download/%{name}-%{version}.tar.gz
# Source0-md5:	99900fc6bfb769a2cc76c234000a64d7
URL:		http://pwmt.org/projects/girara
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool
BuildRequires:	json-c-devel
BuildRequires:	libnotify-devel >= 0.7.0
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
%{__make} COLOR=0 VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%find_lang libgirara-gtk3-2

chmod +x $RPM_BUILD_ROOT%{_libdir}/libgirara-gtk3.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgirara-gtk3-2.lang
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgirara-gtk3.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so
%{_includedir}/girara
%{_pkgconfigdir}/girara-gtk3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgirara-gtk3.a
