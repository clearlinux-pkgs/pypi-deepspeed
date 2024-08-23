#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v18
# autospec commit: f35655a
#
Name     : pypi-deepspeed
Version  : 0.15.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/13/14/5cde975724b07a70ef6cf58cf15efe8505c7c4dbf0a3d9e6ef36adc48775/deepspeed-0.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/14/5cde975724b07a70ef6cf58cf15efe8505c7c4dbf0a3d9e6ef36adc48775/deepspeed-0.15.0.tar.gz
Summary  : DeepSpeed library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-deepspeed-bin = %{version}-%{release}
Requires: pypi-deepspeed-license = %{version}-%{release}
Requires: pypi-deepspeed-python = %{version}-%{release}
Requires: pypi-deepspeed-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hjson)
BuildRequires : pypi(ninja)
BuildRequires : pypi(numpy)
BuildRequires : pypi(packaging)
BuildRequires : pypi(psutil)
BuildRequires : pypi(py_cpuinfo)
BuildRequires : pypi(pydantic)
BuildRequires : pypi(torch)
BuildRequires : pypi(tqdm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![License Apache 2.0](https://badgen.net/badge/license/apache2.0/blue)](https://github.com/Microsoft/DeepSpeed/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/deepspeed.svg)](https://pypi.org/project/deepspeed/)
[![Downloads](https://static.pepy.tech/badge/deepspeed)](https://pepy.tech/project/deepspeed)
[![Build](https://badgen.net/badge/build/check-status/blue)](#build-pipeline-status)
[![Twitter](https://img.shields.io/twitter/follow/MSFTDeepSpeed)](https://twitter.com/intent/follow?screen_name=MSFTDeepSpeed)
[![Japanese Twitter](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9ETwitter-%40MSFTDeepSpeedJP-blue)](https://twitter.com/MSFTDeepSpeedJP)
[![Chinese Zhihu](https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-%E5%BE%AE%E8%BD%AFDeepSpeed-blue)](https://www.zhihu.com/people/deepspeed)

%package bin
Summary: bin components for the pypi-deepspeed package.
Group: Binaries
Requires: pypi-deepspeed-license = %{version}-%{release}

%description bin
bin components for the pypi-deepspeed package.


%package dev
Summary: dev components for the pypi-deepspeed package.
Group: Development
Requires: pypi-deepspeed-bin = %{version}-%{release}
Provides: pypi-deepspeed-devel = %{version}-%{release}
Requires: pypi-deepspeed = %{version}-%{release}

%description dev
dev components for the pypi-deepspeed package.


%package license
Summary: license components for the pypi-deepspeed package.
Group: Default

%description license
license components for the pypi-deepspeed package.


%package python
Summary: python components for the pypi-deepspeed package.
Group: Default
Requires: pypi-deepspeed-python3 = %{version}-%{release}

%description python
python components for the pypi-deepspeed package.


%package python3
Summary: python3 components for the pypi-deepspeed package.
Group: Default
Requires: python3-core
Provides: pypi(deepspeed)
Requires: pypi(hjson)
Requires: pypi(ninja)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(psutil)
Requires: pypi(py_cpuinfo)
Requires: pypi(pydantic)
Requires: pypi(torch)
Requires: pypi(tqdm)

%description python3
python3 components for the pypi-deepspeed package.


%prep
%setup -q -n deepspeed-0.15.0
cd %{_builddir}/deepspeed-0.15.0
pushd ..
cp -a deepspeed-0.15.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724378478
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-deepspeed
cp %{_builddir}/deepspeed-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-deepspeed/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/deepspeed
/usr/bin/deepspeed.pt
/usr/bin/ds
/usr/bin/ds_bench
/usr/bin/ds_elastic
/usr/bin/ds_report
/usr/bin/ds_ssh
/usr/bin/dsr

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.12/site-packages/deepspeed/inference/v2/kernels/core_ops/cuda_linear/include/configs.h
/usr/lib/python3.12/site-packages/deepspeed/inference/v2/kernels/core_ops/cuda_linear/include/weight_prepacking.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-deepspeed/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
