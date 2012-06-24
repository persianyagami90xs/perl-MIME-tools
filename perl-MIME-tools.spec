#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	tools
Summary:	MIME::tools Perl module
Summary(cs):	Modul MIME::tools pro Perl
Summary(da):	Perlmodul MIME::tools
Summary(de):	MIME::tools Perl Modul
Summary(es):	M�dulo de Perl MIME::tools
Summary(fr):	Module Perl MIME::tools
Summary(it):	Modulo di Perl MIME::tools
Summary(ja):	MIME::tools Perl �⥸�塼��
Summary(ko):	MIME::tools �� ����
Summary(no):	Perlmodul MIME::tools
Summary(pl):	Modu� Perla MIME::tools
Summary(pt):	M�dulo de Perl MIME::tools
Summary(pt_BR):	M�dulo Perl MIME::tools
Summary(ru):	������ ��� Perl MIME::tools
Summary(sv):	MIME::tools Perlmodul
Summary(uk):	������ ��� Perl MIME::tools
Summary(zh_CN):	MIME::tools Perl ģ��
Name:		perl-MIME-tools
Version:	5.411
Release:	8a
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}a.tar.gz
# Source0-md5:	e7cb1f8e146171103640e3a5516afb1a
BuildRequires:	perl-devel >= 5.6.1
%if %{!?_without_tests:1}%{?_without_tests:0}
BuildRequires:	perl(File::Path) >= 1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-MailTools >= 1.05
BuildRequires:	perl-MIME-Base64 >= 2.04
BuildRequires:	perl(MIME::QuotedPrint) >= 2.03
BuildRequires:	perl-IO-stringy >= 1.211
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::tools - modules for parsing (and creating!) MIME entities.

%description -l pl
MIME::tools - zestaw modu��w do operacji na danych w formacie MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_vendorlib}/MIME/*.pm
%{perl_vendorlib}/MIME/Parser
%{perl_vendorlib}/MIME/Decoder
%{perl_vendorlib}/MIME/Field
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
