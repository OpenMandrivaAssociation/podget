%define name	podget
%define version	0.5.8
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Simple podcast aggregator
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/podget/%{name}_%{version}.tar.bz2
URL:		http://podget.sourceforge.net/
License:	GPLv2+
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	screen wget bittorrent
BuildArch:	noarch

%description
Podget is a simple podcast aggregator with support for RSS and Bittorrent
feeds, folders and categories, and automatic playlist creation.

%prep
%setup -q -n %name
perl -pi -e 's/get_torrents\=0/get_torrents\=1/' podget.sh
	
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp %name %buildroot/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name


