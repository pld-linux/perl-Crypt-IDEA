%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-IDEA perl module
Summary(pl):	Modu³ perla Crypt-IDEA
Name:		perl-Crypt-IDEA
Version:	1.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-IDEA-%{version}.tar.gz
Patch:		perl-Crypt-IDEA-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-IDEA - Perl interface to IDEA block cipher.

%description -l pl
Crypt-IDEA - modu³ wspomagaj±cy algorytm IDEA.

%prep
%setup -q -n Crypt-IDEA-%{version}
%patch0 -p0

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Crypt/IDEA/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Crypt/IDEA
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* 
        
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitearch}/Crypt/IDEA.pm

%dir %{perl_sitearch}/auto/Crypt/IDEA
%{perl_sitearch}/auto/Crypt/IDEA/.packlist
%{perl_sitearch}/auto/Crypt/IDEA/IDEA.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/IDEA/IDEA.so

%{_mandir}/man3/*
