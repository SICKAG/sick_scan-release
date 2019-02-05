Name:           ros-melodic-sick-scan
Version:        0.0.15
Release:        0%{?dist}
Summary:        ROS sick_scan package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/sick_scan
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-pcl-conversions
Requires:       ros-melodic-pcl-ros
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-visualization-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-pcl-conversions
BuildRequires:  ros-melodic-pcl-ros
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-visualization-msgs

%description
A ROS driver for the SICK TiM and SICK MRS series of laser scanners. This
package is based on the original sick_tim-repository of Martin Günther et al.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Feb 05 2019 Michael Lehning <michael.lehning@lehning.de> - 0.0.15-0
- Autogenerated by Bloom

* Thu Jan 31 2019 Michael Lehning <michael.lehning@lehning.de> - 0.0.14-0
- Autogenerated by Bloom

