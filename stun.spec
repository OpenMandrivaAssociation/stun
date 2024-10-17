Summary:        STUN server and client
Name:           stun
Version:        0.96
Release:        7
License:        BSD
Group:          System/Servers
URL:            https://www.vovida.org/applications/downloads/stun/
Source0:        http://prdownloads.sourceforge.net/stun/stund_%{version}_Aug13.tar.bz2
Source1:        stun-server.init
Source2:        stun-server.sysconfig
Patch0:         stund-0.94-mdk_conf.diff
Patch1:         stund-0.94-x86_64.diff
Patch2:         stun-checkinit.diff
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	dos2unix
BuildRequires:	openssl-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The STUN (Simple Traversal of UDP through NATs (Network Address Translation))
server is an implementation of the STUN protocol that enables STUN
functionality in SIP-based systems. The STUN server tar ball also include a
client API to enable STUN functionality in SIP endpoints. In addition there is
a command line UNIX client and a graphical windows client that check what type
of NAT the user is using.

STUN is an application-layer protocol that can determine the public IP and
nature of a NAT device that sits between the STUN client and STUN server.

%package         server
Summary:         STUN server
Group:           System/Servers
Requires(post):  rpm-helper
Requires(preun): rpm-helper

%description     server
The STUN (Simple Traversal of UDP through NATs (Network Address Translation))
server is an implementation of the STUN protocol that enables STUN
functionality in SIP-based systems. The STUN server tar ball also include a
client API to enable STUN functionality in SIP endpoints. In addition there is
a command line UNIX client and a graphical windows client that check what type
of NAT the user is using.

STUN is an application-layer protocol that can determine the public IP and
nature of a NAT device that sits between the STUN client and STUN server.

This package contains the STUN server.

%package        client
Summary:        STUN client
Group:          System/Servers

%description    client
The STUN (Simple Traversal of UDP through NATs (Network Address Translation))
server is an implementation of the STUN protocol that enables STUN
functionality in SIP-based systems. The STUN server tar ball also include a
client API to enable STUN functionality in SIP endpoints. In addition there is
a command line UNIX client and a graphical windows client that check what type
of NAT the user is using.

STUN is an application-layer protocol that can determine the public IP and
nature of a NAT device that sits between the STUN client and STUN server.

This package contains the STUN client.

%prep

%setup -q -n stund
%patch0 -p1
%patch1 -p0
%patch2 -p0

# strip away annoying ^M
find -type f -exec dos2unix -U {} \;

cp %{SOURCE1} stun-server.init
cp %{SOURCE2} stun-server.sysconfig

%build

%make CXXFLAGS="%{optflags}"

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_initrddir}

install -m0755 stun-server %{buildroot}%{_sbindir}/stun-server
install -m0755 stun-client %{buildroot}%{_sbindir}/stun-client 

install -m0755 stun-server.init %{buildroot}%{_initrddir}/stun-server
install -m0644 stun-server.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/stun-server

%post server
%_post_service stun-server

%preun server
%_preun_service stun-server

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files server
%defattr(-,root,root,-)
%doc nattest nattestwarning.txt rfc3489.txt
%attr(0755,root,root) %{_initrddir}/stun-server
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/stun-server
%attr(0755,root,root) %{_sbindir}/stun-server

%files client
%defattr(-,root,root,-)
%attr(0755,root,root) %{_sbindir}/stun-client 




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.96-6mdv2010.0
+ Revision: 434139
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.96-5mdv2009.0
+ Revision: 261211
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.96-4mdv2009.0
+ Revision: 253627
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.96-2mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 27 2007 Oden Eriksson <oeriksson@mandriva.com> 0.96-2mdv2007.1
+ Revision: 148937
- added p2 by  Christofer Edvardsen "The server did not check the return
- status of stunInitServer before forking to background. This caused the
- server to silently die after start instead of failing on startup when
- for example a faulty ip address was supplied."

* Wed Oct 18 2006 Stefan van der Eijk <stefan@mandriva.org> 0.96-1mdv2007.0
+ Revision: 66058
- 0.96

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - 0.94-6mdv2007.0
    - Import stun

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.94-5mdk
- rebuilt against openssl-0.9.8a

* Thu Oct 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.94-4mdk
- Fix PreReq

* Thu Oct 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.94-3mdk
- Fix BuildRequires

* Fri May 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.94-2mdk
- make it compile on x86_64 (P1)
- use better anti ^M stripper

* Fri Apr 29 2005 Oden Eriksson <oeriksson@mandriva.com> 0.94-1mdk
- initial Mandriva package

