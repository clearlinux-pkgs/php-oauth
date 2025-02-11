#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : php-oauth
Version  : 2.0.9
Release  : 78
URL      : https://pecl.php.net/get/oauth-2.0.9.tgz
Source0  : https://pecl.php.net/get/oauth-2.0.9.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-oauth-lib = %{version}-%{release}
Requires: php-oauth-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
BuildRequires : pcre2-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=== CONFIGURATION ===
2 things need updated with information from the OAuth service provider:
* config.inc.php
* the URL's of the providers resources (to get tokens, manipulate user info, etc.)

%package lib
Summary: lib components for the php-oauth package.
Group: Libraries
Requires: php-oauth-license = %{version}-%{release}

%description lib
lib components for the php-oauth package.


%package license
Summary: license components for the php-oauth package.
Group: Default

%description license
license components for the php-oauth package.


%prep
%setup -q -n oauth-2.0.9
cd %{_builddir}/oauth-2.0.9
pushd ..
cp -a oauth-2.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-oauth
cp %{_builddir}/oauth-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-oauth/d81a5c337700619a652174bdd2b685639f4fb3a4 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20240924/oauth.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-oauth/d81a5c337700619a652174bdd2b685639f4fb3a4
