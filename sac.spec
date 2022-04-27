Name: sac
Version: 1.3
Release: 23
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
BuildRequires: ant zip
# We need to build with OpenJDK 12 because this is used
# by LibreOffice, which can't be built with OpenJDK > 12
# because of hsqldb 1.8.x
BuildRequires: java-12-openjdk-devel
Requires: java
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
export JAVA_HOME=%{_prefix}/lib/jvm/java-12-openjdk
export PATH=$JAVA_HOME/bin:$PATH
ant jar javadoc

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/java
cp -p ./build/lib/sac.jar $RPM_BUILD_ROOT%{_datadir}/java/sac.jar

mkdir -p $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}

%files
%doc COPYRIGHT.html
%{_datadir}/java/%{name}.jar

%files javadoc
%doc COPYRIGHT.html
%{_datadir}/javadoc/%{name}
