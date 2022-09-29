#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-oauth
Version  : 2.0.7
Release  : 29
URL      : https://pecl.php.net/get/oauth-2.0.7.tgz
Source0  : https://pecl.php.net/get/oauth-2.0.7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-oauth-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre-dev
BuildRequires : pcre2-dev

%description
=== CONFIGURATION ===
2 things need updated with information from the OAuth service provider:
* config.inc.php
* the URL's of the providers resources (to get tokens, manipulate user info, etc.)

%package lib
Summary: lib components for the php-oauth package.
Group: Libraries

%description lib
lib components for the php-oauth package.


%prep
%setup -q -n oauth-2.0.7
cd %{_builddir}/oauth-2.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/oauth.so
