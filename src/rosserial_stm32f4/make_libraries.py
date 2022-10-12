#!/usr/bin/env python3
import rospkg, rosserial_client, sys, shutil, os.path
from rosserial_client.make_library import *

THIS_PACKAGE = "rosserial_stm32f4"

__usage__ = """
make_libraries.py generates the STM32F4 rosserial library files.  It
requires the location to export the libraries to.
rosrun rosserial_stm32f4 make_libraries.py <output_path>
"""

ROS_TO_EMBEDDED_TYPES = {
    'bool'    :   ('bool',              1, PrimitiveDataType, []),
    'byte'    :   ('int8_t',            1, PrimitiveDataType, []),
    'int8'    :   ('int8_t',            1, PrimitiveDataType, []),
    'char'    :   ('uint8_t',           1, PrimitiveDataType, []),
    'uint8'   :   ('uint8_t',           1, PrimitiveDataType, []),
    'int16'   :   ('int16_t',           2, PrimitiveDataType, []),
    'uint16'  :   ('uint16_t',          2, PrimitiveDataType, []),
    'int32'   :   ('int32_t',           4, PrimitiveDataType, []),
    'uint32'  :   ('uint32_t',          4, PrimitiveDataType, []),
    'int64'   :   ('int64_t',           8, PrimitiveDataType, []),
    'uint64'  :   ('uint64_t',          8, PrimitiveDataType, []),
    'float32' :   ('float',             4, PrimitiveDataType, []),
    'float64' :   ('float',             4, PrimitiveDataType, []),
    'time'    :   ('ros::Time',         8, TimeDataType, ['ros/time']),
    'duration':   ('ros::Duration',     8, TimeDataType, ['ros/duration']),
    'string'  :   ('char*',             0, StringDataType, []),
    'Header'  :   ('std_msgs::Header',  0, MessageDataType, ['std_msgs/Header'])
}

if (len(sys.argv) < 2):
    print(__usage__)
    exit()

path = sys.argv[1]
output_path = os.path.join(sys.argv[1], "ros_lib")
print(f"\nExporting to {output_path}")

rospack = rospkg.RosPack()

shutil.rmtree(output_path, ignore_errors=True)
shutil.copytree(os.path.join(rospack.get_path(THIS_PACKAGE), "src", "ros_lib"), output_path)
rosserial_client_copy_files(rospack, output_path)

rosserial_generate(rospack, output_path, ROS_TO_EMBEDDED_TYPES)
