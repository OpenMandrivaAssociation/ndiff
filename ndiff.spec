%define release %mkrel 7

Summary: Compare putatively similar files, ignoring small numeric differences 
Name: ndiff
Version: 2.00
Release: %release
License: GPL
Group: Text tools
Source:  ftp://ftp.math.utah.edu/pub/misc/ndiff-%{version}.tar.gz
URL: http://www.math.utah.edu/~beebe/software/ndiff/
BuildRoot: %_tmppath/%name-%version-root

%description
When a numerical program is run  in  multiple  environments  (operating
systems, architectures, or compilers), assessing its consistency can be
a difficult task for a human, since small differences in numerical out-
put values are expected.
ndiff  provides a solution to this problem.  It compares two files that
are expected to be identical, or at  least,  numerically  similar.   It
assumes  that  lines  consist of whitespace-separated fields of numeric

%prep
%setup -q 

%build
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
%makeinstall
mv $RPM_BUILD_ROOT/%{_mandir}/ndiff* $RPM_BUILD_ROOT/%{_mandir}/man1

###workaround bug #52511
rm -rf $RPM_BUILD_ROOT/%{_bindir}/ndiff
mv $RPM_BUILD_ROOT/%{_datadir}/lib/%{name}/%{name}-%{version}/ndiff.awk $RPM_BUILD_ROOT/%{_datadir}/lib/%{name}/%{name}-%{version}/ndiff-2.00.awk
mv  $RPM_BUILD_ROOT/%{_mandir}/man1/ndiff.1 $RPM_BUILD_ROOT/%{_mandir}/man1/ndiff-2.00.1
###workaround bug #52511

%files
%defattr(-,root,root)
%doc COPYING README* INSTALL 
%{_bindir}/ndiff-2.00
%{_mandir}/man1/ndiff-2.00.1*
%{_datadir}/lib/%{name}/%{name}-%{version}/ndiff*

%clean
[ %buildroot != '/' ] && rm -fr %buildroot



%changelog
* Wed Jun 22 2011 Leonardo Coelho <leonardoc@mandriva.com> 2.00-7mdv2011.0
+ Revision: 686728
- changing the binary name cause conflicts with nmap/ndiff (bug report #52511)

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.00-5mdv2010.0
+ Revision: 430162
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.00-4mdv2009.0
+ Revision: 253695
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.00-2mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 21:47:50 (55185)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 21:41:41 (55182)
Import ndiff

* Tue Nov 29 2005 Olivier Thauvin <nanardon@mandriva.org> 2.00-1mdk
- By Philippe Weill <Philippe.Weill@aero.jussieu.fr>
  - initial mdk spec

