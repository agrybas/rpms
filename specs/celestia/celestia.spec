# $Id$

%define desktop_vendor freshrpms

Summary: An OpenGL real-time visual space simulation.
Name: celestia
Version: 1.3.0
Release: 2.fr
License: GPL
Group: Amusements/Graphics
Source0: http://dl.sf.net/celestia/%{name}-%{version}.tar.bz2
Source1: http://www.shatters.net/celestia/files/minormoons.ssc
Source2: http://www.shatters.net/celestia/files/numberedmoons.ssc
URL: http://www.shatters.net/celestia/
BuildRoot: %{_tmppath}/%{name}-root
Requires: glut, gtkglarea, libpng, libjpeg
BuildRequires: glut-devel, gtkglarea, gnome-libs-devel
BuildRequires: libpng-devel, libjpeg-devel
BuildRequires: desktop-file-utils, unzip, gcc-c++, libstdc++-devel

%description
Celestia is a free real-time space simulation that lets you experience our
universe in three dimensions. Unlike most planetarium software, Celestia
doesn't confine you to the surface of the Earth. You can travel throughout
the solar system, to any of over 100,000 stars, or even beyond the galaxy.
All travel in Celestia is seamless; the exponential zoom feature lets you
explore space across a huge range of scales, from galaxy clusters down to
spacecraft only a few meters across. A 'point-and-goto' interface makes it
simple to navigate through the universe to the object you want to visit.

%prep
%setup -q

%build
%configure  --disable-debug --with-gtk
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/%{name}/extras/minormoons.ssc
install -m 644 %{SOURCE2} \
        %{buildroot}%{_datadir}/%{name}/extras/numberedmoons.ssc
install -m 644 -D src/celestia/kde/data/hi48-app-celestia.png \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png

cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Celestia
Comment=An OpenGL real-time visual space simulation
Icon=%{name}.png
Exec=%{name}
Terminal=false
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category X-Red-Hat-Extras               \
  --add-category Application                    \
  --add-category Graphics                       \
  %{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%dir %{_datadir}/%{name}
%config %{_datadir}/%{name}/celestia.cfg
%doc %{_datadir}/%{name}/controls.txt
%doc %{_datadir}/%{name}/COPYING
%{_datadir}/%{name}/*.cel
%{_datadir}/%{name}/data
%{_datadir}/%{name}/extras
%{_datadir}/%{name}/fonts
%doc %{_datadir}/%{name}/manual
%{_datadir}/%{name}/models
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/textures
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3.0-2.fr
- Rebuild for Fedora Core 1.

* Thu Apr 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.3.0.
- Added numberedmoons.ssc addon.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Jan 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.5.
- Included "Minor Moons of the Giant Planets" extra file.
- New icon from the KDE part of the source.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New style menu entry.

* Wed Jul  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt to remove the NVidia dependency (oops!).

* Wed May 15 2002 Matthias Saou <http://freshrpms.net/>
- Sorry, I'm a maniac ;-)

* Tue May 14 2002 Julien MOUTTE <julien@moutte.net>
- Initial RPM release.

