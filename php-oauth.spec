#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-oauth
Version  : 2.0.4
Release  : 2
URL      : https://pecl.php.net/get/oauth-2.0.4.tgz
Source0  : https://pecl.php.net/get/oauth-2.0.4.tgz
Summary  : PHP extension to provide OAuth consumer and provider bindings.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-oauth-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre-dev

%description
WePay is a group payment service which makes managing money for groups simple.
These example scripts come with a test consumer key and secret which you can
use to test the API, but they may be rate limited or disabled entirely at any
point, so you should go to https://www.wepay.com/developer/register to register
your own consumer key and shared secret which you can put in the config.inc.php
file.

%package lib
Summary: lib components for the php-oauth package.
Group: Libraries

%description lib
lib components for the php-oauth package.


%prep
%setup -q -n oauth-2.0.4
cd %{_builddir}/oauth-2.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/oauth.so
