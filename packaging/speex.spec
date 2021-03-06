Name:       speex
Summary:    A voice compression format (codec)
Version:    1.2rc1
Release:    2.23
Group:      System/Libraries
License:    BSD
URL:        http://www.speex.org/
Source0:    http://downloads.xiph.org/releases/speex/%{name}-1.2rc1.tar.gz
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)

%description
Speex is an audio codec especially designed for compressing voice at low
 bit-rates for applications such as voice over IP (VoIP). In some senses,
 it is meant to be complementary to the Vorbis codec which places a greater
 emphasis on high-quality music reproduction.
 This package contains the encoder and decoder command-line applications.


%package tools
Summary:    The tools package for %{name}
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}

%description tools
Speex is a patent-free compression format designed especially for
speech. This package contains tools files and user's manual for %{name}.


%package devel
Summary:    Development package for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}



%prep
%setup -q -n %{name}-1.2rc1


%build

%configure -disable-static \
%ifarch %arm
	--enable-arm5e-asm \
	--disable-oggtest \
	--disable-float-api \
	--disable-vbr \
	--enable-fixed-point 
%endif

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -f $RPM_BUILD_ROOT%{_docdir}/speex/manual.pdf



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig




%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libspeex*.so.*


%files tools
%defattr(-,root,root,-)
%{_bindir}/speexenc
%{_bindir}/speexdec
%doc %{_mandir}/man1/speexenc.1*
%doc %{_mandir}/man1/speexdec.1*

%files devel
%defattr(-,root,root,-)
%doc doc/manual.pdf
%{_includedir}/speex
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex*.pc
%{_libdir}/libspeex*.so

