Summary:	TIS FireWall ToolKit
Summary(pl):	TIS FireWall ToolKit
Name:		fwtk
Version:	2.1
Release:	1
Copyright:	see LICENSE file (redistribution restricted)
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
# How to get sources - see http://www.fwtk.org/ and http://www.tis.com/
Source0:	%{name}%{version}.tar.Z
Source1:	%{name}-doc-only.tar.Z
Source2:	http://www.fwtk.org/fwtk/patches/%{name}-summ.pl.gz
Patch0:		fwtk2.1-ipv6-19990423-PLD.patch
Patch1:		fwtk-ndbm.patch
Patch2:		fwtk-linux.patch
Patch3:		fwtk-massfix.patch
Patch4:		fwtk-ftp-plugin.patch
Patch5:		fwtk-config.patch
URL:		http://www.fwtk.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/%{name}

%description
Firewall Toolkit

%description -l pl
Firewall Toolkit - narz�dzie do tworzenia firewalli

%prep
%setup -q -n %{name}
%setup -q -a 1 -T -D -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
cp Makefile.config.linux Makefile.config

%build
RPM_OPT="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man{3,5,8}}
%{__make} install \
	DEST=$RPM_BUILD_ROOT%{_sbindir}
mv $RPM_BUILD_ROOT%{_sbindir}/netperm-table $RPM_BUILD_ROOT%{_sysconfdir}/

cp fwtk/doc/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3/
cp fwtk/doc/man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5/
cp fwtk/doc/man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8/

install %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}
gzip -9nf $RPM_BUILD_ROOT%{_sbindir}/*.gz

strip $RPM_BUILD_ROOT%{_sbindir}/* || :
rm -f config/Makefile
gzip -9nf CHANGES LICENSE README fwtk/doc/*.* config/* $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %doc {CHANGES,LICENSE,README}.gz fwtk/doc/*.* config/*
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man[358]/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
