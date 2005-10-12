# $Id$
# Authority: dries
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name List-MoreUtils

Summary: Additions to List::Util
Name: perl-List-MoreUtils
Version: 0.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-MoreUtils/

Source: http://www.cpan.org/modules/by-module/List/List-MoreUtils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provide the missing functionality from List::Util (see
"SUGGESTED ADDITIONS" in its manpage).

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/List/
%{perl_vendorarch}/List/MoreUtils.pm
%dir %{perl_vendorarch}/auto/List/
%{perl_vendorarch}/auto/List/MoreUtils/

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
