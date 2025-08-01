#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	IDEA
Summary:	Crypt::IDEA - Perl interface to IDEA block cipher
Summary(pl.UTF-8):	Crypt::IDEA - interfejs perlowy do szyfru blokowego IDEA
Name:		perl-Crypt-IDEA
Version:	1.10
Release:	8
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0284334d0d3e18543f178111130aa00d
Patch0:		%{name}-paths.patch
Patch1:		%{name}-5.6.0.patch
URL:		http://search.cpan.org/dist/Crypt-IDEA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::IDEA Perl extension is an implementation of the IDEA block
cipher algorithm.

%description -l pl.UTF-8
Rozszerzenie Perla Crypt::IDEA stanowi implementację algorytmu
szyfrowania blokowego IDEA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p0
%patch -P1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Crypt/IDEA.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT
%{perl_vendorarch}/Crypt/IDEA.pm
%dir %{perl_vendorarch}/auto/Crypt/IDEA
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/IDEA/IDEA.so
%{_mandir}/man3/Crypt::IDEA.3pm*
