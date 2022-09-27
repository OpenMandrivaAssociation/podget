Summary:	Simple podcast aggregator
Name:		podget
Version: 	0.9.0
Release: 	1
License:	GPLv2+
Group:		Networking/News
URL:		http://podget.sourceforge.net/
Source0:	https://github.com/dvehrs/podget/archive/refs/tags/v%{version}.tar.gz

BuildArch:	noarch
Requires:	screen
Requires:	wget

%description
Podget is a simple podcast aggregator with support for RSS and Bittorrent
feeds, folders and categories, and automatic playlist creation.

%prep
%setup -q

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name} %{buildroot}/%{_bindir}

%files
%doc README
%{_bindir}/%{name}
