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

"""
@brief 生成LaunchDescrption类对象
@detail 描述详细信息
"""
def generate_launch_description():
    moveit_package_prefix = get_package_share_directory('my_robot_config')
    robot_description_config = LaunchConfiguration('robot_description_config')
    move_group_config = LaunchConfiguration('move_group_config')
    trajectory_execution_config = LaunchConfiguration('trajectory_execution_config')

    robot_description_config_default = moveit_package_prefix + '/configs/robot_description.yaml'
    move_group_config_default = moveit_package_prefix + '/configs/move_group.yaml'
    trajectory_execution_config_default = moveit_package_prefix + '/configs/trajectory_execution.yaml'

    robot_description_config = LaunchConfiguration('robot_description_config', default=robot_description_config_default)
    move_group_config = LaunchConfiguration('move_group_config', default=move_group_config_default)
    trajectory_execution_config = LaunchConfiguration('trajectory_execution_config', default=trajectory_execution_config_default)

    moveit_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([moveit_package_prefix +'/launch/move_group.launch.py']),
    launch_arguments={
    robot_description_config': robot_description_config,
    'move_group_config': move_group_config,
    'trajectory_execution_config': trajectory_execution_config
    }.items ())

    return LaunchDescription([moveit_launch])

    