Summary: Websockets proxy for VNC traffic
Name:    wsproxy
Version: 1.4.0
Release: 5%{?dist}
License: LGPL+linking exception
URL:     https://github.com/xapi-project/wsproxy
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/wsproxy/archive?at=v1.4.0&format=tar.gz&prefix=wsproxy-1.4.0#/wsproxy-1.4.0.tar.gz) = 57397f9dffcc59744a9565b16233102aa6c22b07
BuildRequires: xs-opam-repo

%description
Websockets proxy for VNC traffic

%prep
%autosetup -p1

%build
jbuilder build

%install
%{__install} -D -m 755 _build/install/default/bin/wsproxy %{buildroot}/opt/xensource/libexec/wsproxy

%files
/opt/xensource/libexec/wsproxy

%changelog
* Fri Jan 26 2018 Christian Lindig <christian.lindig@citrix.com> - 1.4.0-1
- CP-23210: Refactor wsproxy for unit tests
- CP-23210: Update opam file
- CP-23210: Add tests for wsproxy
- cli/wsproxy.ml: fix compilation with Lwt 3

* Thu Aug 31 2017 Marcello Seri <marcello.seri@citrix.com> - 1.3.0-1
- Major code refactor
- Use ocaml-base64 instead of a home baked implementation
- CP-24262: Do now wait on both handler threads when running the proxy
- Introduce and enable syslog logging

* Wed Aug 2 2017 Marcello Seri <marcello.seri@citrix.com> - 1.2.0-1
- Use v1.2.0 ported to jbuilder
- Fix file descriptor leak (CA-260671)
- Use more performant base64 decode sanitization
- Use upstream ocaml-base64 implementation

* Tue Mar 14 2017 Marcello Seri <marcello.seri@citrix.com> - 1.1.0-1
- Use v1.1.0 ported to oasis and ppx

* Tue Mar 14 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.0-3
- Use v1.0.0 from github mirror

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.0-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Thu Nov 3 2016 Marcello Seri <marcello.seri@citrix.com> - 1.0.0-1
- Change version number to follow semver

* Tue Aug 23 2016 Vivek Kumar Chaubey <vivekkumar.chaubey@citrix.com> - 1.0-1
- Build using transformer
