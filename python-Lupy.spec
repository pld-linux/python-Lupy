
%define 	module	Lupy

Summary:	Full-text indexer and search engine
Summary(pl):	Silnik pe�notekstowego wyszukiwania i indeksowania dokument�w
Name:		python-%{module}
Version:	0.2.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/lupy/%{module}-%{version}.tar.gz
# Source0-md5:	515ea0b4aab8dd8299480cb9a0da6068
URL:		http://www.divmod.org/Home/Projects/Lupy/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lupy is a full-text indexer and search engine written in Python. It is
a port of Jakarta Lucene 1.2 to Python. Specifically, it reads and
writes indexes in Lucene binary format.

%description -l pl
Lupy jest silnikiem umo�liwiaj�cym pe�notekstowe przeszukiwanie i
indeksowanie dokument�w. Lupy jest portem systemu Jakarta Lucene 1.2
do Pythona. Zapisuje i odczytuje indeksy w binarnym formacie Lucene.

%prep
%setup -q -n %{module}-%{version}

%build
# Build it without warnings
mv setup.py blah.blah
sed 's/platform/platforms/' < blah.blah > setup.py

python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt changelog.txt examples PKG-INFO
%{py_sitescriptdir}/lupy