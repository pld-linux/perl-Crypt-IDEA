%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	IDEA
Summary:	Crypt-IDEA perl module
Summary(pl):	Modu³ perla Crypt-IDEA
Name:		perl-Crypt-IDEA
Version:	1.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-5.6.0.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-IDEA - Perl interface to IDEA block cipher.

%description -l pl
Crypt-IDEA - modu³ wspomagaj±cy algorytm IDEA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0
%patch1 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/Crypt/IDEA.pm
%dir %{perl_sitearch}/auto/Crypt/IDEA
%{perl_sitearch}/auto/Crypt/IDEA/IDEA.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/IDEA/IDEA.so

%{_mandir}/man3/*
