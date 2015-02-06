Summary:	Simple podcast aggregator
Name:		podget
Version: 	0.6.18
Release: 	3
License:	GPLv2+
Group:		Networking/News
URL:		http://podget.sourceforge.net/
Source0:	http://sourceforge.net/projects/podget/files/podget/podget-0.6.18/%{name}-%{version}.tar.gz

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
