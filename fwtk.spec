Summary:	TIS FireWall ToolKit
Summary(pl):	TIS FireWall ToolKit
Name:		fwtk
Version:	2.1
Release:	1
License:	see LICENSE file (redistribution restricted)
Group:		Networking/Daemons
# How to get sources - see http://www.fwtk.org/ and http://www.tis.com/
Source0:	%{name}%{version}.tar.Z
Source1:	%{name}-doc-only.tar.Z
Source2:	http://www.fwtk.org/fwtk/patches/%{name}-summ.pl.gz
# Source2-md5:	6944963ae47ee29864d3ffd8405b8079
Patch0:		%{name}2.1-ipv6-19990423-PLD.patch
Patch1:		%{name}-ndbm.patch
Patch2:		%{name}-linux.patch
Patch3:		%{name}-massfix.patch
Patch4:		%{name}-ftp-plugin.patch
Patch5:		%{name}-config.patch
URL:		http://www.fwtk.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/%{name}

%description
Firewall Toolkit.

%description -l pl
Firewall Toolkit - narzêdzie do tworzenia firewalli.

%prep
%setup -q -n %{name}
%setup -q -a 1 -T -D -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
cp -f Makefile.config.linux Makefile.config

%build
RPM_OPT="%{rpmcflags}" %{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man{3,5,8}}
%{__make} install \
	DEST=$RPM_BUILD_ROOT%{_sbindir}

mv -f $RPM_BUILD_ROOT%{_sbindir}/netperm-table $RPM_BUILD_ROOT%{_sysconfdir}

install fwtk/doc/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install fwtk/doc/man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install fwtk/doc/man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}
gunzip $RPM_BUILD_ROOT%{_sbindir}/*.gz

rm -f config/Makefile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README fwtk/doc/*.* config/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[358]/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
