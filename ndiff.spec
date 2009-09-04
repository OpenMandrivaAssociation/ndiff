%define release %mkrel 5

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

%files
%defattr(-,root,root)
%doc COPYING README* INSTALL 
%{_bindir}/ndiff*
%{_mandir}/man1/ndiff.1*
%{_datadir}/lib/%{name}/%{name}-%{version}/ndiff.awk

%clean
[ %buildroot != '/' ] && rm -fr %buildroot

