Summary:	C++ template library for linear algebra
Name:		eigen
Version:	3.2.1
Release:	1
License:	LGPL v3+ or GPL v2+
Group:		Development/Libraries
Source0:	http://bitbucket.org/eigen/eigen/get/%{version}.tar.bz2
# Source0-md5:	ece1dbf64a49753218ce951624f4c487
Patch0:		%{name}-buildtype.patch
URL:		http://eigen.tuxfamily.org/
BuildRequires:	cmake
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eigen is a C++ template library for linear algebra: vectors, matrices,
and related algorithms. It is versatile, fast, elegant and
compiler-friendly.

%prep
%setup -qn eigen-eigen-6b38706d90a9
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/eigen3
%{_npkgconfigdir}/eigen3.pc

