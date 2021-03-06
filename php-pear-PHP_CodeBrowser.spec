%define  upstream_name PHP_CodeBrowser
%define __noautoreq /usr/bin/php

Summary:	A code browser that augments the code with information from various QA tools

Name:		php-pear-%{upstream_name}
Version:	1.0.1
Release:	4
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHP_CodeBrowser-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides a code browser that augments the code with information
from various QA tools for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/CHANGELOG.markdown
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/README.markdown
%{_bindir}/phpcb
%{_datadir}/pear/PHP_CodeBrowser
%{_datadir}/pear/packages/PHP_CodeBrowser.xml
%{_datadir}/pear/data/PHP_CodeBrowser



