"""
@file moveit_node.py
@mainpage rclpy库 geomtry_msgs/msg下的Port类型 moveit2库中的PlanningCompoent类 
@brief 基于moveit2以python代码实现从一个点移动到另一个点
@authon yekong6663
@version 1.0
@date 25-2-22
@note ...
"""
import moveit2 
import moveit2.moveit_py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
"""
@brief MoveNode_t类,用于实现核心功能
@detail 描述详细信息
"""
class MoveNode_t(Node):
    """
    @brief 类初始化
    @detail 初始化MoveGroupCommander类对象,目标位置Pose对象
    """ 
    def __init__(self,target_pose:Pose):
        super().__init__("move_node")
        self.moveit=moveit2.moveit_py("move_node")
        self.group=self.moveit.get__planning_component("whole")
        self.target_pose=target_pose
        self.target_pose.orientation.w=1.0
    

