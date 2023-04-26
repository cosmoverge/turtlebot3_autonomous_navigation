#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Darby Lim

import os

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world_file_name = 'turtlebot3_worlds/' + TURTLEBOT3_MODEL + '.model'
    # world_file_name = 'final_model.sdf'
    world = os.path.join(get_package_share_directory('turtlebot3_gazebo'),
                         'worlds', world_file_name)
    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # spawnRobotx = LaunchConfiguration("spawnRobotx")
    # spawnRoboty = LaunchConfiguration("spawnRoboty")
    # spawnRobotz = LaunchConfiguration("spawnRobotz")
    # spawnRobotR = LaunchConfiguration("spawnRobotR")
    # spawnRobotP = LaunchConfiguration("spawnRobotP")
    # spawnRobotY = LaunchConfiguration("spawnRobotY")
    # declare_robot_x = DeclareLaunchArgument(
    #     "spawnRobotx", default_value="0.0")
    # declare_robot_y = DeclareLaunchArgument(
    #     "spawnRoboty", default_value="0.0")
    # declare_robot_z = DeclareLaunchArgument(
    #     "spawnRobotz", default_value="0.0")
    # declare_robot_R = DeclareLaunchArgument(
    #     "spawnRobotR", default_value="0.0"
    # )
    # declare_robot_P = DeclareLaunchArgument(
    #     "spawnRobotP", default_value="0.0"
    # )
    # declare_robot_Y = DeclareLaunchArgument(
    #     "spawnRobotY", default_value="0.0"
    # )

    # robot_name = LaunchConfiguration("robot_name")
    # declare_robot_name = DeclareLaunchArgument(
    #     "robot_name", default_value="turtlebot3_burger")

    # robot_path = LaunchConfiguration("robot_path")
    # declare_robot_path = DeclareLaunchArgument(
    #     "robot_path", default_value="/home/proliant/.gazebo/models/turtlebot3_burger/model.sdf")

    # start_gazebo_spawner_cmd = Node(
    #     package="gazebo_ros",
    #     executable="spawn_entity.py",
    #     output="screen",
    #     arguments=[
    #         "-entity",
    #         robot_name,
    #         # "-topic",
    #         # "/robot_description",
    #         "-file",
    #         robot_path,
    #         "-robot_namespace",
    #         "",
    #         "-x",
    #         spawnRobotx,
    #         "-y",
    #         spawnRoboty,
    #         "-z",
    #         spawnRobotz,
    #         "-R",
    #         spawnRobotR,
    #         "-P",
    #         spawnRobotP,
    #         "-Y",
    #         spawnRobotY,
    #     ],
    # )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
            ),
            launch_arguments={'world': world}.items(),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
            ),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_file_dir, '/robot_state_publisher.launch.py']),
            launch_arguments={'use_sim_time': use_sim_time}.items(),
        ),
        # declare_robot_name,
        # declare_robot_x,
        # declare_robot_y,
        # declare_robot_z,
        # declare_robot_R,
        # declare_robot_P,
        # declare_robot_Y,
        # declare_robot_path,
        # start_gazebo_spawner_cmd
    ])
