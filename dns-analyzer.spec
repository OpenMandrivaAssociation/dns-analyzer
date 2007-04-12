%define name	dns-analyzer
%define version	0.3.0
%define release	%mkrel 4

Summary:	Analyze DNS traffic from tcpdump trace files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/Other
License:	GPL
URL:		http://www.nlnetlabs.nl/dns-analyzer/
Source0:	http://www.nlnetlabs.nl/dns-analyzer/%{name}-%{version}.tar.bz2
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
The DNS Analyzer is a tool to analyze DNS traffic from
tcpdump/libpcap trace files. The purpose of the DNS Analyzer is to
analyze DNS trace files from the DNS root servers to find traffic
that is unnecessary.

The DNS Analyzer can also be used to convert trace files into R data
files. R can be used to perform fine-grained statistical analysis of
the data. Some sample R functions are provided in the R/dns.R file
that can be found in the source distribution.

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

install -m0755 packet2c %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc CODING ChangeLog README
%{_bindir}/dns-analyzer
%{_bindir}/packet2c
%{_mandir}/man1/dns-analyzer.1*


