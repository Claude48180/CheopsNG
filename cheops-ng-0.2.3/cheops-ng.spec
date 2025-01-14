%define name       cheops-ng
%define version    0.2.2
%define release    1
%define serial     1
%define prefix     /usr
%define sysconfdir /etc

Summary:	A Gnome network mapper, OS/port scanner, and monitoring program
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Applications/Internet
Vendor:		Priddy Good Software
Url:		http://cheops-ng.sourceforge.net/
Source:		%{name}-%{version}.tar.gz
Packager:	Brent Priddy <toopriddy@mailcity.com>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.5
Requires:   gnome-libs >= 1.2.0
Requires:   libxml >= 1.8.0
Requires:   imlib >= 1.9.0

%description
Cheops-ng is a Network management tool for mapping and monitoring your
network. It has host/network discovery functionality as well as OS detection
of hosts. Cheops-ng has the ability to probe hosts to see what services they
are running. On some services, cheops-ng is actually able to see what
program is running for a service and the version number of that program. The
future for cheops-ng includes host monitoring via various methods like ping,
grabbing a web page, logging in via ftp... whatever is needed

%prep
%setup

%build
echo "here"
CFLAGS="$RPM_OPT_FLAGS" 
./configure --prefix=%{prefix}
make 
make strip
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi;
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install
make clean

%install
make DESTDIR=$RPM_BUILD_ROOT prefix=%{prefix} sysconfdir=%{sysconfdir} install

%files
%defattr(-,root,root)
%{prefix}/bin/cheops-ng
%{prefix}/bin/cheops-agent
%{prefix}/share/pixmaps/cheops-ng.xpm
%{prefix}/share/cheops-ng/pixmaps/*
%{prefix}/share/gnome/apps/Internet/cheops-ng.desktop
%{prefix}/share/gnome/ximian/Programs/Internet/cheops-ng.desktop

%clean
rm -r $RPM_BUILD_ROOT

%changelog
