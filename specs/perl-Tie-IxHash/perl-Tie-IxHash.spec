# $Id$

# Authority: dries
# Upstream: Gurusamy Sarathy <gsar$ActiveState,com>

%define real_name Tie-IxHash
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Ordered associative arrays for Perl
Name: perl-Tie-IxHash
Version: 1.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-IxHash/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-IxHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
If you have been led to believe that associative arrays in perl
don't preserve order, and if you have ever craved for that feature,
this module is for you.  Simply declare a "tie" for the hash variable
that you want to be order-preserving, and forget that limitation
ever existed.  You can do other nifty things with the tied hash object
that you may be used to doing with arrays, like Push(), Pop() and 
Splice().

If you don't know what "tie" means, you should look at the
perltie(1) manpage in a recent perl distribution, or in the
index of one of the numerous books on perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/IxHash.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
