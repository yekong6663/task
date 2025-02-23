# ROS 2 MoveIt 2 Project
这是一个使用ROS 2 Humble和MoveIt 2的项目，演示了如何使用Docker环境从一个点移动到另一个点。
## 目录结构
|---.devcontainer
|   |---Dockerfile  docker构建文件
|   |---docker-compose.yml  docker启动文件
|---packages    docker依赖,moveit依赖,可以放其他地方
|---ros_ws      ros包工作区,里面写调包Launch文件
|   |---src
|   |   |---my_robot_config moveit2的构建文件
|   |   |---ros2_core_code  ros2功能包
|---.gitignore  git忽视文件
|---README.markdown

## 依赖项

- Docker
- Docker Compose
- Git

## 安装

1. 安装Docker和Docker Compose：
   - 对于Ubuntu，可以使用以下命令安装：
     sudo apt update
     sudo apt install docker.io docker-compose
   - 对于其他操作系统，请参考[Docker官方文档](https://docs.docker.com/get-docker/)。

2. 克隆本项目：   
   git clone https://github.com/yekong6663/task

3. 构建Docker镜像并启动容器：
   docker-compose up --build

## 使用

1. 在容器中运行launch文件：
   docker-compose exec  ros2 launch my_launch.launch.py
2. 在容器中运行功能包
   docker-compose exec ros2 run ros2_core_code move_node


## 贡献

欢迎贡献！请提交拉取请求或报告问题。

## 许可证

本项目采用MIT许可证。

## 联系

- 项目维护者：yekong663
- 邮箱：744311194@qq.com

