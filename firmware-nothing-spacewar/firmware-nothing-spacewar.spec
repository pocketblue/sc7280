%global debug_package %{nil}
%global commit        428184b45f1294a0e66979f570902de84883e1fc
Name:                 firmware-nothing-spacewar
Version:              1
Release:              0%{?dist}
Summary:              firmware for nothing phone 1
License:              Unknown
URL:                  https://github.com/mainlining/firmware-nothing-spacewar
Source0:              %{url}/archive/%{commit}.tar.gz
BuildArch:            noarch
Requires:             qcom-firmware
AutoReqProv:          no

%description
firmware for nothing phone 1

%prep
%autosetup -n %{name}-%{commit}

%install
find . -type f -exec install -Dm644 {} %{buildroot}/{} ';'

%files
/lib/firmware/qcom
/usr/share/qcom

%changelog
%autochangelog
