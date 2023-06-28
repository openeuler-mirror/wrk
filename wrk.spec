Name:                wrk
Version:             4.1.0
Release:             3
Summary:             Modern HTTP benchmarking tool
License:             Apache-2.0
URL:                 https://github.com/wg/wrk
Source0:             https://github.com/wg/wrk/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:              Make-the-debug-package-compile.patch 
Patch1:              fix-wrk-version-or-v-error.patch 
Patch2:              fix-clang.patch
BuildRequires:       pkgconf openssl-devel
%description
wrk is a modern HTTP benchmarking tool capable of generating significant
load when run on a single multi-core CPU. It combines a multithreaded
design with scalable event notification systems such as epoll and kqueue.
An optional LuaJIT script can perform HTTP request generation, response
processing, and custom reporting. Several example scripts are located in
scripts.

%prep
%autosetup -p1

%build
%make_build OPTFLAGS="%{optflags}" WITH_OPENSSL=%{_prefix}

%install
install -D -m 0755 wrk %{buildroot}%{_bindir}/wrk

%files
%license LICENSE
%doc README.md NOTICE scripts/
%{_bindir}/wrk

%changelog
* Tue Jun 27 2023 yoo <sunyuechi@iscas.ac.cn> - 4.1.0-3
- fix clang build error

* Thu Oct 14 2021 wangyue <wangyue92@huawei.com> - 4.1.0-2
- fix wrk --version/-v error

* Mon Jun 28 2021 huanghaitao <huanghaitao8@huawei.com> - 4.1.0-1
- Package init
