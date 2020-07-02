%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-sick-scan
Version:        1.7.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS sick_scan package

License:        BSD
URL:            http://wiki.ros.org/sick_scan
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-perception-pcl
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-visualization-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A ROS driver for the SICK TiM and SICK MRS series of lidars. This package is
based on the original sick_tim-repository of Martin Günther et al.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Jul 02 2020 Michael Lehning <michael.lehning@lehning.de> - 1.7.6-1
- Autogenerated by Bloom

* Thu Jun 11 2020 Michael Lehning <michael.lehning@lehning.de> - 1.6.0-1
- Autogenerated by Bloom

