#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-Table
Version  : 0.008
Release  : 5
URL      : http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Term-Table-0.008.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Term-Table-0.008.tar.gz
Summary  : 'Format a header and rows into a table'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Term-Table-doc
BuildRequires : perl(Importer)

%description
NAME
Term::Table - Format a header and rows into a table
DESCRIPTION
This is used by some failing tests to provide diagnostics about what
has gone wrong. This module is able to generic format rows of data into
tables.

%package doc
Summary: doc components for the perl-Term-Table package.
Group: Documentation

%description doc
doc components for the perl-Term-Table package.


%prep
%setup -q -n Term-Table-0.008

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/Term/Table.pm
/usr/lib/perl5/site_perl/5.26.0/Term/Table/Cell.pm
/usr/lib/perl5/site_perl/5.26.0/Term/Table/CellStack.pm
/usr/lib/perl5/site_perl/5.26.0/Term/Table/HashBase.pm
/usr/lib/perl5/site_perl/5.26.0/Term/Table/LineBreak.pm
/usr/lib/perl5/site_perl/5.26.0/Term/Table/Spacer.pm
/usr/lib/perl5/site_perl/5.26.0/Term/Table/Util.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
