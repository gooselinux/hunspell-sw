Name: hunspell-sw
Summary: Swahili hunspell dictionaries
%define upstreamid 20050819
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Group: Applications/Text
Source: http://www.it46.se/downloads/openoffice/dictionary/dictionary_myspell_sw_TZ_1.1.tar.gz
URL: http://www.it46.se
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Swahili hunspell dictionaries.

%prep
%setup -q -c

%build
for i in README_sw_TZ.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
sw_TZ_aliases="sw_KE"
for lang in $sw_TZ_aliases; do
        ln -s sw_TZ.aff $lang.aff
        ln -s sw_TZ.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_sw_TZ.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20050819-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050819-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20050819-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050819-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20050819-1
- initial version
