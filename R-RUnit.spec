#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-RUnit
Version  : 0.4.33
Release  : 52
URL      : https://cran.r-project.org/src/contrib/RUnit_0.4.33.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RUnit_0.4.33.tar.gz
Summary  : R Unit Test Framework
Group    : Development/Tools
License  : GPL-2.0
Requires: R-RUnit-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
framework, with additional code inspection and report
        generation tools.

%package license
Summary: license components for the R-RUnit package.
Group: Default

%description license
license components for the R-RUnit package.


%prep
%setup -q -n RUnit
pushd ..
cp -a RUnit buildavx2
popd
pushd ..
cp -a RUnit buildavx512
popd
pushd ..
cp -a RUnit buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740099322

%install
export SOURCE_DATE_EPOCH=1740099322
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-RUnit
cp %{_builddir}/RUnit/COPYING %{buildroot}/usr/share/package-licenses/R-RUnit/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RUnit/DESCRIPTION
/usr/lib64/R/library/RUnit/INDEX
/usr/lib64/R/library/RUnit/Meta/Rd.rds
/usr/lib64/R/library/RUnit/Meta/features.rds
/usr/lib64/R/library/RUnit/Meta/hsearch.rds
/usr/lib64/R/library/RUnit/Meta/links.rds
/usr/lib64/R/library/RUnit/Meta/nsInfo.rds
/usr/lib64/R/library/RUnit/Meta/package.rds
/usr/lib64/R/library/RUnit/Meta/vignette.rds
/usr/lib64/R/library/RUnit/NAMESPACE
/usr/lib64/R/library/RUnit/NEWS
/usr/lib64/R/library/RUnit/R/RUnit
/usr/lib64/R/library/RUnit/R/RUnit.rdb
/usr/lib64/R/library/RUnit/R/RUnit.rdx
/usr/lib64/R/library/RUnit/doc/RUnit.R
/usr/lib64/R/library/RUnit/doc/RUnit.Rnw
/usr/lib64/R/library/RUnit/doc/RUnit.pdf
/usr/lib64/R/library/RUnit/doc/index.html
/usr/lib64/R/library/RUnit/examples/correctTestCase.r
/usr/lib64/R/library/RUnit/examples/runitVirtualClassTest.r
/usr/lib64/R/library/RUnit/examples/runitc2f.r
/usr/lib64/R/library/RUnit/help/AnIndex
/usr/lib64/R/library/RUnit/help/RUnit.rdb
/usr/lib64/R/library/RUnit/help/RUnit.rdx
/usr/lib64/R/library/RUnit/help/aliases.rds
/usr/lib64/R/library/RUnit/help/paths.rds
/usr/lib64/R/library/RUnit/html/00Index.html
/usr/lib64/R/library/RUnit/html/R.css
/usr/lib64/R/library/RUnit/share/R/checkCode.r
/usr/lib64/R/library/RUnit/share/R/compareRUnitTestData.r
/usr/lib64/R/library/RUnit/tests/README
/usr/lib64/R/library/RUnit/unitTests/Makefile
/usr/lib64/R/library/RUnit/unitTests/runalltests.R
/usr/lib64/R/library/RUnit/unitTests/runitHTMLProtocol.r
/usr/lib64/R/library/RUnit/unitTests/runitInspect.r
/usr/lib64/R/library/RUnit/unitTests/runitJUnitProtocol.r
/usr/lib64/R/library/RUnit/unitTests/runitPlotConnection.r
/usr/lib64/R/library/RUnit/unitTests/runitRUnit.r
/usr/lib64/R/library/RUnit/unitTests/runitS4.r
/usr/lib64/R/library/RUnit/unitTests/runitSetUp.r
/usr/lib64/R/library/RUnit/unitTests/runitTearDown.r
/usr/lib64/R/library/RUnit/unitTests/runitTestLogger.r
/usr/lib64/R/library/RUnit/unitTests/runitTextProtocol.r

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-RUnit/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
