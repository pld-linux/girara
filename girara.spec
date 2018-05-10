Summary:	User interface library
Name:		girara
Version:	0.2.9
Release:	3
License:	BSD-like
Group:		Libraries
Source0:	http://pwmt.org/projects/girara/download/%{name}-%{version}.tar.xz
# Source0-md5:	631ff6edb1413c043effd37fd920db2b
URL:		http://pwmt.org/projects/girara
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	intltool
BuildRequires:	json-c-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	meson >= 0.43
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.727
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.20
Requires:	libnotify >= 0.7.0
Obsoletes:	girara-static < 0.2.9
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

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang libgirara-gtk3-3

chmod +x $RPM_BUILD_ROOT%{_libdir}/libgirara-gtk3.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgirara-gtk3-3.lang
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgirara-gtk3.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so
%{_includedir}/girara
%{_pkgconfigdir}/girara-gtk3.pc
