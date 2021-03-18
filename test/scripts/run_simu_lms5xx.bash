#!/bin/bash
printf "\033c"
pushd ../../../..
source /opt/ros/melodic/setup.bash
source ./install/setup.bash

echo -e "run_simu_lms5xx.bash: starting lms5xx emulation\n"

# Start roscore if not yet running
roscore_running=`(ps -elf | grep roscore | grep -v grep | wc -l)`
if [ $roscore_running -lt 1 ] ; then 
  roscore &
  sleep 3
fi

# Start sick_scan emulator
roslaunch sick_scan emulator_lms5xx.launch &
sleep 1

# Start rviz
# Note: Due to a bug in opengl 3 in combination with rviz and VMware, opengl 2 should be used by rviz option --opengl 210
# See https://github.com/ros-visualization/rviz/issues/1444 and https://github.com/ros-visualization/rviz/issues/1508 for further details

# rosrun rviz rviz -d ./src/sick_scan/test/emulator/config/rviz_lms5xx.rviz &
rosrun rviz rviz -d ./src/sick_scan/test/emulator/config/rviz_emulator_cfg_lms5xx.rviz --opengl 210 &
sleep 1

# Start sick_scan driver for lms5xx
echo -e "Launching sick_scan sick_lms_5xx.launch\n"
# roslaunch sick_scan sick_lms_5xx.launch hostname:=192.168.0.151 &
roslaunch sick_scan sick_lms_5xx.launch hostname:=127.0.0.1 &
sleep 1

# Wait for 'q' or 'Q' to exit or until rviz is closed
while true ; do  
  echo -e "lms5xx emulation running. Close rviz or press 'q' to exit..." ; read -t 1.0 -n1 -s key
  if [[ $key = "q" ]] || [[ $key = "Q" ]]; then break ; fi
  rviz_running=`(ps -elf | grep rviz | grep -v grep | wc -l)`
  if [ $rviz_running -lt 1 ] ; then break ; fi
done

# Shutdown
echo -e "Finishing lms5xx emulation, shutdown ros nodes\n"
rosnode kill -a ; sleep 1
killall sick_generic_caller ; sleep 1
killall sick_scan_emulator ; sleep 1
popd

