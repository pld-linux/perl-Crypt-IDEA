%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-IDEA perl module
Summary(pl):	Modu� perla Crypt-IDEA
Name:		perl-Crypt-IDEA
Version:	1.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-IDEA-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		perl-Crypt-IDEA-5.6.0.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-IDEA - Perl interface to IDEA block cipher.

%description -l pl
Crypt-IDEA - modu� wspomagaj�cy algorytm IDEA.

%prep
%setup -q -n Crypt-IDEA-%{version}
%patch0 -p0
%patch1 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}"

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
