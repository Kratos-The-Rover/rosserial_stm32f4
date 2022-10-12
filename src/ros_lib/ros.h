#ifndef _ROS_H_
#define _ROS_H_

#include "ros/node_handle.h"
#include "STM32F4Hardware.h"

namespace ros
{
  typedef ros::NodeHandle_<STM32F4Hardware> NodeHandle;
}

#endif
