Summary: An X Window System based CPU state monitor.
Name: xcpustate
%define version	2.5
Version: %{version}
Release: 5
Copyright: Freely redistributable
Group: Applications/System
Source: ftp://ftp.cs.toronto.edu/pub/jdd/xcpustate/xcpustate-%{version}.tar.gz
Patch0: xcpustate-%{version}-nlist.patch
Patch1: xcpustate-%{version}-alpha.patch
Patch2: xcpustate-%{version}-6.0.patch
BuildRoot: /var/tmp/xcpustate-root

%description
The xcpustate utility is an X Window System based monitor which shows
the amount of time that the CPU is spending in different states.  On a
Linux system, xcpustate displays a bar that indicates the amounts of idle,
user, nice and system time (from left to right) used by the CPU.

Install the xcpustate package if you'd like to use a horizontal bar style
CPU state monitor.

%prep
%setup -q
%patch0 -p1 -b .nlist
%patch2 -p1 -b .glibc
%ifarch alpha
%patch1 -p1 -b .alpha
%endif

%build
xmkmf
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,root) /usr/X11R6/bin/xcpustate
%attr(0644,root,root) /usr/X11R6/man/man1/xcpustate.1x
