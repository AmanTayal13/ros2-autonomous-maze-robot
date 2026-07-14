import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node, SetParameter
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro
pkg_name = "finalProject"

def generate_launch_description():

    urdf_path = PathJoinSubstitution(
        [FindPackageShare(pkg_name), "description", "robot.urdf.xacro"]
    )

    return LaunchDescription([
        SetParameter(name='use_sim_time', value=True),

        DeclareLaunchArgument(
            'urdf_path',
            default_value=urdf_path,
            description='Path to the URDF file'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': Command(['xacro ', LaunchConfiguration('urdf_path'), ' robot_name:=robot_0'])
            }]
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
            ]),
            launch_arguments={'world': PathJoinSubstitution([FindPackageShare(pkg_name), 'world', 'maze.world'])}.items()
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'robot', '-x', '1.0', '-y', '1.0', '-z', '0.0']
        ),
    ])

