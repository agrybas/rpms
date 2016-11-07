Name:		SABnzbd	
Version: 	1.1.0	
Release:	1%{?dist}
Summary: 	An Open Source Binary Newsreader written in Python	

Group: 		Applications/Web	
License: 	GPLv3
URL: 		http://sabnzbd.org/	
Source0: 	https://github.com/sabnzbd/sabnzbd/releases/download/%{version}/%{name}-%{version}-src.tar.gz

BuildArch: 	noarch
BuildRequires: 	python2

%description
SABnzbd makes Usenet as simple and streamlined as possible by automating everything it can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction.

%prep
#%setup -q -n %{name}-%{version}
%autosetup
%define _missing_doc_files_terminate_build 0

%build
%{__python} -m compileall SABnzbd.py
%{__python} -OO SABnzbd.py -v > /dev/null

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/share/SABnzbd

cp SABnzbd.p*  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R cherrypy  	%{buildroot}%{_prefix}/share/SABnzbd
cp -R email 		%{buildroot}%{_prefix}/share/SABnzbd
cp -R gntp  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R icons  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R interfaces  	%{buildroot}%{_prefix}/share/SABnzbd
cp -R linux  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R locale  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R po  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R sabnzbd  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R scripts  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R six  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R solaris  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R tools  		%{buildroot}%{_prefix}/share/SABnzbd
cp -R util  		%{buildroot}%{_prefix}/share/SABnzbd

cat > %{buildroot}%{_bindir}/SABnzbd <<EOL
#!/bin/bash
cd %{_prefix}/share/SABnzbd/
exec ./SABnzbd.py \$*
EOL

%check
# %{__python2} setup.py test

%files
%attr(-, root, root) %{_prefix}/share/SABnzbd/SABnzbd.p*
%attr(-, root, root) %{_prefix}/share/SABnzbd/cherrypy
%attr(-, root, root) %{_prefix}/share/SABnzbd/email
%attr(-, root, root) %{_prefix}/share/SABnzbd/gntp
%attr(-, root, root) %{_prefix}/share/SABnzbd/icons
%attr(-, root, root) %{_prefix}/share/SABnzbd/interfaces
%attr(-, root, root) %{_prefix}/share/SABnzbd/linux
%attr(-, root, root) %{_prefix}/share/SABnzbd/locale
%attr(-, root, root) %{_prefix}/share/SABnzbd/po
%attr(-, root, root) %{_prefix}/share/SABnzbd/sabnzbd
%attr(-, root, root) %{_prefix}/share/SABnzbd/scripts
%attr(-, root, root) %{_prefix}/share/SABnzbd/six
%attr(-, root, root) %{_prefix}/share/SABnzbd/solaris
%attr(-, root, root) %{_prefix}/share/SABnzbd/tools
%attr(-, root, root) %{_prefix}/share/SABnzbd/util
%attr(-, root, root) %doc README.txt ABOUT.txt ISSUES.txt
%attr(-, root, root) %license LICENSE.txt COPYRIGHT.txt GPL2.txt GPL3.txt licenses
%attr(755, root, root) %{_bindir}/SABnzbd

%changelog

