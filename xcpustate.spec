Summary:	An X Window System based CPU state monitor
Name:		xcpustate
Version:	2.5
Release:	5
Copyright:	Freely redistributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.cs.toronto.edu/pub/jdd/xcpustate/%{name}-%{version}.tar.gz
Patch0:		xcpustate-%{version}-nlist.patch
Patch1:		xcpustate-%{version}-alpha.patch
Patch2:		xcpustate-%{version}-6.0.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The xcpustate utility is an X Window System based monitor which shows
the amount of time that the CPU is spending in different states. On a
Linux system, xcpustate displays a bar that indicates the amounts of
idle, user, nice and system time (from left to right) used by the CPU.

Install the xcpustate package if you'd like to use a horizontal bar
style CPU state monitor.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%ifarch alpha
%patch1 -p1
%endif

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xcpustate
%{_mandir}/man1/xcpustate.1x.gz
