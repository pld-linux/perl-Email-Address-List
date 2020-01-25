#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	Address-List
Summary:	Email::Address-List - RFC close address list parsing
Name:		perl-Email-Address-List
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe280aca41dd79539b17023fd8d3c6bb
URL:		http://search.cpan.org/dist/Email-Address-List/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parser for From, To, Cc, Bcc, Reply-To, Sender and previous prefixed
with Resent- (eg Resent-From) headers.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Email/Address
%{perl_vendorlib}/Email/Address/List.pm
%{_mandir}/man3/Email::Address::List.3pm*
