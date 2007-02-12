Summary:	An X Window System based CPU state monitor
Summary(pl.UTF-8):   Monitor stanu procesora pod X Window System
Name:		xcpustate
Version:	2.5
Release:	6
License:	freely distributable
Group:		Applications/System
Source0:	ftp://ftp.cs.toronto.edu/pub/jdd/xcpustate/%{name}-%{version}.tar.gz
# Source0-md5:	a40054e91c694b8a87be8f5819d8ad09
Patch0:		%{name}-%{version}-nlist.patch
Patch1:		%{name}-%{version}-alpha.patch
Patch2:		%{name}-%{version}-6.0.patch
BuildRequires:	libelf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The xcpustate utility is an X Window System based monitor which shows
the amount of time that the CPU is spending in different states. On a
Linux system, xcpustate displays a bar that indicates the amounts of
idle, user, nice and system time (from left to right) used by the CPU.

Install the xcpustate package if you'd like to use a horizontal bar
style CPU state monitor.

%description -l pl.UTF-8
Narzędzie xcpustate jest działającym pod X Window System monitorem
pokazującym jak dużo czasu procesor spędza w poszczególnych stanach.
Pod Linuksem xcpustate rysuje wykres czasu idle, user, nice i system.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%ifarch alpha
%patch1 -p1
%endif

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xcpustate
%{_mandir}/man1/xcpustate.1x*
