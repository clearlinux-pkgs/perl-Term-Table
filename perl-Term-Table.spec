#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: 250a666
#
Name     : perl-Term-Table
Version  : 0.018
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Term-Table-0.018.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Term-Table-0.018.tar.gz
Summary  : 'Format a header and rows into a table'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Term-Table-license = %{version}-%{release}
Requires: perl-Term-Table-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Term::Table - Format a header and rows into a table
DESCRIPTION
This is used by some failing tests to provide diagnostics about what
has gone wrong. This module is able to format rows of data into tables.

%package dev
Summary: dev components for the perl-Term-Table package.
Group: Development
Provides: perl-Term-Table-devel = %{version}-%{release}
Requires: perl-Term-Table = %{version}-%{release}

%description dev
dev components for the perl-Term-Table package.


%package license
Summary: license components for the perl-Term-Table package.
Group: Default

%description license
license components for the perl-Term-Table package.


%package perl
Summary: perl components for the perl-Term-Table package.
Group: Default
Requires: perl-Term-Table = %{version}-%{release}

%description perl
perl components for the perl-Term-Table package.


%prep
%setup -q -n Term-Table-0.018
cd %{_builddir}/Term-Table-0.018

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Term-Table
cp %{_builddir}/Term-Table-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Term-Table/28e7ec7493915d0625a4d80dd3b2ad71b2ec9fdc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::Table.3
/usr/share/man/man3/Term::Table::Cell.3
/usr/share/man/man3/Term::Table::CellStack.3
/usr/share/man/man3/Term::Table::HashBase.3
/usr/share/man/man3/Term::Table::LineBreak.3
/usr/share/man/man3/Term::Table::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Term-Table/28e7ec7493915d0625a4d80dd3b2ad71b2ec9fdc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
