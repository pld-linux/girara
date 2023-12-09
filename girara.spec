Summary:	User interface library
Summary(pl.UTF-8):	Biblioteka interfejsu użytkownika
Name:		girara
Version:	0.4.1
Release:	1
License:	BSD-like
Group:		Libraries
#Source0Download: https://git.pwmt.org/pwmt/girara/-/tags
Source0:	https://git.pwmt.org/pwmt/girara/-/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7aef527f5f0210c822fb9767b9f6ae8b
URL:		http://pwmt.org/projects/girara
# C11
BuildRequires:	gcc >= 6:8.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	json-glib-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	meson >= 0.61
BuildRequires:	ninja
BuildRequires:	pango-devel >= 1:1.14
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.20
Requires:	libnotify >= 0.7.0
Requires:	pango >= 1:1.14
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

%description -l pl.UTF-8
girara to biblioteka implementująca interfejs użytkownika skupiający
się na prostocie i minimalizmie. Obecnie jest oparty na GTK+ -
wieloplatformowym toolkicie widgetów - zapewnia interfejs o trzech
głównych komponentach: tzw. widgecie widoku, reprezentującym właściwą
aplikację (np. stronę dla przeglądarki WWW, obraz dla przeglądarki
obrazków czy dokument dla przeglądarki dokumentów), pasku wprowadzania
służącym do wydawania poleceń oraz pasku stanu udostępniającym
użytkownikowi aktualne informacje. girara została zaprojektowana w
celu zastąpienia i rozszerzenia interfejsu użytkownika używanego przez
aplikacje zathura i jumanji, a także innych funkcji dzielonych przez
te aplikacje.

%package devel
Summary:	Header files for girara library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki girara
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50.0
Requires:	gtk+3-devel >= 3.20
Requires:	json-glib-devel
Requires:	libnotify-devel >= 0.7.0
Requires:	pango-devel >= 1:1.14

%description devel
Header files for girara library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki girara.

%package static
Summary:	Girara static library
Summary(pl.UTF-8):	Statyczna biblioteka girara
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Girara static library.

%description static -l pl.UTF-8
Statyczna biblioteka girara.

%prep
%setup -q

%build
%meson build \
	-Dnotify=enabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{fa_IR,fa}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{uk_UA,uk}

%find_lang libgirara-gtk3-3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgirara-gtk3-3.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgirara-gtk3.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgirara-gtk3.so
%{_includedir}/girara
%{_pkgconfigdir}/girara-gtk3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgirara-gtk3.a
