%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	IDEA
Summary:	Crypt::IDEA Perl module
Summary(cs):	Modul Crypt::IDEA pro Perl
Summary(da):	Perlmodul Crypt::IDEA
Summary(de):	Crypt::IDEA Perl Modul
Summary(es):	Módulo de Perl Crypt::IDEA
Summary(fr):	Module Perl Crypt::IDEA
Summary(it):	Modulo di Perl Crypt::IDEA
Summary(ja):	Crypt::IDEA Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::IDEA ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::IDEA
Summary(pl):	Modu³ Perla Crypt::IDEA
Summary(pt):	Módulo de Perl Crypt::IDEA
Summary(pt_BR):	Módulo Perl Crypt::IDEA
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::IDEA
Summary(sv):	Crypt::IDEA Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::IDEA
Summary(zh_CN):	Crypt::IDEA Perl Ä£¿é
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
Crypt::IDEA - Perl interface to IDEA block cipher.

%description -l pl
Crypt::IDEA - modu³ obs³uguj±cy algorytm szyfrowania IDEA.

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
