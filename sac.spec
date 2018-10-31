%{?_javapackages_macros:%_javapackages_macros}
Name: sac
Version: 1.3
Release: 20.3
Summary: Java standard interface for CSS parser
License: W3C
Group:   Development/Java
#Original source: http://www.w3.org/2002/06/%{name}java-%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source0: %{name}java-%{version}-jarsdeleted.zip
Source1: %{name}-build.xml
Source2: %{name}-MANIFEST.MF
Source3: http://mirrors.ibiblio.org/pub/mirrors/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant, java-devel, jpackage-utils, zip
Requires: java, jpackage-utils
BuildArch: noarch

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc

Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
install -m 644 %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant jar javadoc

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./build/lib/sac.jar $RPM_BUILD_ROOT%{_javadir}/sac.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc COPYRIGHT.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/*

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
* Wed Aug 21 2013 Mat Booth <fedora@matbooth.co.uk> - 1.3-17
- Update for newer guidelines, rhbz #993211

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Caolán McNamara <caolanm@redhat.com> - 1.3-14
- repack zip to drop jars

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Caolán McNamara <caolanm@redhat.com> - 1.3-11
- Resolves: rhbz#715875 FTBFS

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3-9
- Drop gcj.
- Adapt to current guidelines.

* Thu Jul 08 2010 Caolán McNamara <caolanm@redhat.com> - 1.3-8
- add COPYING to all subpackages

* Mon May 31 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.3-7
- Fix spelling of my surname in %%changelog.

* Wed Mar 24 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3-6
- Add maven pom and metadata.

* Fri Jul 24 2009 Caolán McNamara <caolanm@redhat.com> - 1.3-5
- make javadoc no-arch when building as arch-dependant aot

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 6 2009 Alexander Kurtakov <akurtako@redhat.com> 1.3-3.3
- Add osgi manifest (needed by eclipse-birt).

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.3-3.2
- drop repotag

* Fri May 09 2008 Caolán McNamara <caolanm@redhat.com> 1.3-3jpp.1
- update for guidelines

* Sat May 03 2008 Caolán McNamara <caolanm@redhat.com> 1.3-3jpp
- import from jpackage

* Fri Sep 03 2004 Fernando Nasser <fnasser@redhat.com> 1.3-3jpp
- Rebuild with Ant 1.6.2

* Tue May 06 2003 David Walluck <david@anti-microsoft.org> 1.3-2jpp
- update for JPackage 1.5

* Thu Jul 11 2002 Ville Skyttä <ville.skytta@iki.fi> 1.3-1jpp
- Update to 1.3.
- Use sed instead of bash 2 extension when symlinking jars during build.
- Add Distribution tag, fix URL, tweak Summary and description.

* Wed Feb 06 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-1jpp 
- first jpp release
