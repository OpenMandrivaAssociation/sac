Summary:	Java standard interface for CSS parser
Name:		sac
Version:	1.3
Release:	13
License:	W3C
Group:		System/Libraries
Url:		http://www.w3.org/Style/CSS/SAC/
Source0:	http://www.w3.org/2002/06/%{name}java-%{version}.zip
Source1:	%{name}-build.xml
Source2:	%{name}-MANIFEST.MF
Source3:	http://mirrors.ibiblio.org/pub/mirrors/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	java-devel
BuildRequires:	jpackage-utils
BuildRequires:	java-rpmbuild
BuildRequires:	zip
Requires:	java
Requires:	jpackage-utils

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc
Group:		Development/Java
Summary:	Javadoc for %{name}

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

mkdir -p %{buildroot}%{_javadir}
cp -p ./build/lib/sac.jar %{buildroot}%{_javadir}/sac.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}

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
%doc COPYRIGHT.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

