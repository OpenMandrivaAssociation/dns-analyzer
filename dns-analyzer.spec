Summary:	Analyze DNS traffic from tcpdump trace files
Name:		dns-analyzer
Version:	0.3.0
Release:	10
Group:		Networking/Other
License:	GPL
URL:		http://www.nlnetlabs.nl/dns-analyzer/
Source0:	http://www.nlnetlabs.nl/dns-analyzer/%{name}-%{version}.tar.bz2
Patch0:		dns-analyzer-0.3.0-gcc43.diff
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall

install -m0755 packet2c %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc CODING ChangeLog README
%{_bindir}/dns-analyzer
%{_bindir}/packet2c
%{_mandir}/man1/dns-analyzer.1*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-9mdv2011.0
+ Revision: 617823
- the mass rebuild of 2010.0 packages

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-8mdv2010.0
+ Revision: 453455
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-7mdv2009.1
+ Revision: 298537
- fix build
- rebuilt against libpcap-1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3.0-4mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-4mdv2007.0
+ Revision: 101642
- Import dns-analyzer

* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-4mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Tue Jul 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-2mdk
- rebuild

* Sat Jun 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.0-1mdk
- 0.3.0
- built against new deps and with gcc v3.4.x
- fix deps
- drop P0, another fix is in there

