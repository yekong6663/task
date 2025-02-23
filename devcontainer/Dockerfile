FROM osrf/ros:humble
WORKDIR /root/ws
RUN mkdir -p /packages
RUN cd /packages
RUN apt-get update && \
    apt-get install -y \
    ros-humble-moveit \
    ros-humble-moveit-ros-plugins \
    ros-humble-rviz2 \
    ros-humble-tf2-ros && \
    rm -rf /var/lib/apt/lists/*
RUN rosdep init && \
    rosdep update
RUN cd ../
RUN mkdir -p /src
RUN cd /src
RUN git clone https://github.com/yekong6663/task/tree/moveit2/ros_ws/src 
RUN colcon build  && \
    install/setup.bash


VOLUME ["/root/ws/src"]
CMD ["bash"]