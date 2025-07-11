################################################################
# Install:
# * python.exe -m pip install pypiwin32
# * python.exe -m pip install wmi
#
# Usage:
# * !! Make sure Openhardwaremonitor is running !!
# * python basicwmi.py
################################################################

import wmi

hwmon = wmi.WMI(namespace="root\\OpenHardwareMonitor")
sensors = hwmon.Sensor()
# sensors = hwmon.Sensor(SensorType="Temperature")

for s in sensors:
	print(s.Name, " (", s.SensorType, ") : ", s.Value)
