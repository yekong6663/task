"""
@file launch.py
@mainpage launch库 ament_index_python.packages库
@brief F ...
@author
@version 1.0
@date 24-9-1
"""
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch. substitutions import LaunchConfiguration
from launch. launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory