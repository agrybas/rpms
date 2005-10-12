# $Id$
# Authority: dries
# Upstream: Roland Giersig <RGiersig$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Tty

Summary: Interface to pseudo Tty
Name: perl-IO-Tty
Version: 1.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Tty/

Source: http://www.cpan.org/modules/by-module/IO/IO-Tty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
IO::Tty and IO::Pty provide an interface to pseudo ttys.

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
%doc README
%{_mandir}/man3/*
%dir %{perl_vendorarch}/IO/
%{perl_vendorarch}/IO/Pty.pm
%{perl_vendorarch}/IO/Tty.pm
%{perl_vendorarch}/IO/Tty/
%dir %{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/auto/IO/Tty/

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
