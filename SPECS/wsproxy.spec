%global package_speccommit 1d30e9b477299216e788d2f9156528c5bca66424
%global package_srccommit v1.12.0
Summary: Websockets proxy for VNC traffic
Name:    wsproxy
Version: 1.12.0
Release: 11%{?xsrel}%{?dist}
license: LGPL-2.0-only WITH OCaml-LGPL-linking-exception
URL:     https://github.com/xapi-project/wsproxy
Source0: wsproxy-1.12.0.tar.gz
BuildRequires: xs-opam-repo

Requires: libev

%description
Websockets proxy for VNC traffic

%prep
%autosetup -p1

%build
dune build --profile=release

# needs 'qcheck' in xs-opam
#%check
#dune runtest --profile=release

%install
%{__install} -D -m 755 _build/install/default/bin/wsproxy %{buildroot}/opt/xensource/libexec/wsproxy

%files
/opt/xensource/libexec/wsproxy

%changelog
* Thu Jul 20 2023 Rob Hoes <rob.hoes@citrix.com> - 1.12.0-11
- Bump release and rebuild

* Mon Jun 19 2023 Christian Lindig <christian.lindig@citrix.com> - 1.12.0-10
- Bump release and rebuild

* Thu Jun 08 2023 Christian Lindig <christian.lindig@citrix.com> - 1.12.0-9
- Bump release and rebuild

* Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.12.0-8
- Bump release and rebuild

* Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.12.0-7
- Bump release and rebuild

* Thu Feb 23 2023 Pau Ryuz Safont <pau.ruizsafont@cloud.com> - 1.12.0-6
- Fix bogus date
- Use SPDX identifier as license

* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.12.0-5
- Bump package for libev dependency

* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.12.0-4
- Bump package after xs-opam update

* Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.12.0-3
- bump packages after xs-opam update

* Wed Nov 20 2019 Pau Ruiz Safont <pau.safont@citrix.com> - 1.12.0-1
- CP-330919: Revert changes for CP-32138

* Tue Oct 29 2019 Edvin Török <edvin.torok@citrix.com> - 1.11.0-1
- CP-32138: replace deprecated Lwt_log with Logs_lwt
- CP-32138: replace deprecated recv_msg from Lwt_unix
- CP-32138: do not daemonize ourselves
- CP-32138: simplify path setup
- CP-32138: Use collaborative log reporter
- CP-32138: Generate more descriptive messages when match fails
- cli: stop logging debug-level messages by default
- CP-32138: Do not manage pid files
- CP-32138: use an already activated socket

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.10.0-2
- bump packages after xs-opam update

* Wed Jun 05 2019 Christian Lindig <christian.lindig@citrix.com> - 1.10.0-1
- Update base64 to 3.1.0

* Wed Feb 20 2019 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-1
- CA-309048 add support for domain sockets

* Mon Jan 07 2019 Christian Lindig <christian.lindig@citrix.com> - 1.8.0-1
- Ported from jbuilder to dune.

* Wed Jan 02 2019 Christian Lindig <christian.lindig@citrix.com> - 1.7.0-1
- CP-30062 update dependencies for OCaml 4.07, Lwt 4.1

* Tue May 29 2018 Christian Lindig <christian.lindig@citrix.com> - 1.6.0-1
- wsproxy: update Lwt functions invocations

* Wed Apr 11 2018 Christian Lindig <christian.lindig@citrix.com> - 1.5.0-1
- wsproxy: fix warning Re_str -> Re.Str
- helpers, lwt_support: make safe-string compliant
- helpers.ml: avoid copying the string in unmask

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
