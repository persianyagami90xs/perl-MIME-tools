#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	tools
Summary:	MIME::tools - modules for parsing (and creating!) MIME entities
Summary(pl):	MIME::tools - zestaw modu��w do operacji na danych w formacie MIME
Name:		perl-MIME-tools
Version:	5.420
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4db6505cc0132c80c5a9cc54f443a21a
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(File::Path) >= 1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-IO-stringy >= 1.211
BuildRequires:	perl-MIME-Base64 >= 2.20
BuildRequires:	perl-MailTools >= 1.05
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(Convert::BinHex)'

%description
MIME-tools is a collection of Perl5 MIME:: modules for parsing,
decoding and generating single- or multipart (even nested multipart)
MIME messages. (Yes, kids, that means you can send messages with
attached GIF files).

%description -l pl
MIME::tools to zestaw modu��w MIME:: dla Perla 5 do analizy,
dekodowania oraz tworzenia jedno- i wielocz�ciowych (a nawet
zagnie�d�onych wielocz�ciowych) wiadomo�ci MIME (tak, to znaczy, �e
mo�na wysy�a� wiadomo�ci z do��czonymi plikami GIF).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/MIME-tools/.packlist

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
