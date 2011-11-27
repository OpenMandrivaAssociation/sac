Name: sac
Version: 1.3
Release: 12
Summary: Java standard interface for CSS parser
License: W3C
Group: System/Libraries
Source0: http://www.w3.org/2002/06/%{name}java-%{version}.zip
Source1: %{name}-build.xml
Source2: %{name}-MANIFEST.MF
Source3: http://mirrors.ibiblio.org/pub/mirrors/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant, java-devel, jpackage-utils
Requires: java, jpackage-utils
BuildArch: noarch

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc
Group: Development/Java
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
rm -rf $RPM_BUILD_ROOT

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./build/lib/sac.jar $RPM_BUILD_ROOT%{_javadir}/sac.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.w3c.css sac %{version} JPP sac

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%doc COPYRIGHT.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

