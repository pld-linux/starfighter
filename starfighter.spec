%define		fversion	%(echo %{version} |tr r -)
%define		mversion	%(echo %{version} |cut -f 1 -d r)
Summary:	Starfighter - an old school 2D shoot 'em up
Summary(pl.UTF-8):	Starfighter - strzelanka 2D w starym stylu
Name:		starfighter
Version:	1.1r1
Release:	1
License:	GPL v.2
Group:		Applications/Games
Source0:	%{name}-%{fversion}.tar.gz
# Source0-md5:	6a4b704dbc83c7403842b936f95ee958
URL:		http://www.parallelrealities.co.uk/starfighter.php
BuildRequires:	SDL-devel >= 1.2.7-1
BuildRequires:	SDL_mixer-devel >= 1.2.5-2
BuildRequires:	SDL_image-devel >= 1.2.3-2
BuildRequires:	libstdc++-devel >= 3.3.4-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Starfighter is an old school 2D shoot 'em up.

%description -l pl.UTF-8
Starfighter jest strzelanką 2D w starym stylu.

%prep
%setup -q -n %{name}-%{mversion}
cat makefile |sed -e 's@-O3@@g' >Makefile
rm -f makefile

%build
%{__make} \
	BINDIR=%{_bindir} \
 	DOCDIR=%{_docdir}/%{name}-%{version} \
	DATADIR=%{_datadir}/%{name}/ \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -Wall -DLINUX"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.pak $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.pak

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gif docs/*.png docs/*html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
