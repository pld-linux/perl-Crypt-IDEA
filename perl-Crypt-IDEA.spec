%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	IDEA
Summary:	Crypt::IDEA - Perl interface to IDEA block cipher
Summary(pl):	Crypt::IDEA - interfejs perlowy do szyfru blokowego IDEA
Name:		perl-Crypt-IDEA
Version:	1.02
Release:	2
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9c453c402b1fc494faa9dd3be793a4a
Patch0:		%{name}-paths.patch
Patch1:		%{name}-5.6.0.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::IDEA Perl extension is an implementation of the IDEA block
cipher algorithm.

%description -l pl
Rozszerzenie Perla Crypt::IDEA stanowi implementacjê algorytmu
szyfrowania blokowego IDEA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT
%{perl_vendorarch}/Crypt/IDEA.pm
%dir %{perl_vendorarch}/auto/Crypt/IDEA
%{perl_vendorarch}/auto/Crypt/IDEA/IDEA.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/IDEA/IDEA.so
%{_mandir}/man3/*
