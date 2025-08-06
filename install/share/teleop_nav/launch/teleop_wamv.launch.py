from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    bridge_params = '/home/antoni/gazebo_maritime_ws/src/teleop_nav/launch/bridge.yaml'

    # print(pkg_path)

    # bridge_params = os.path.join(
    #     pkg_path,
    #     'launch',
    #     'bridge.yaml'
    # )

    return LaunchDescription([

        # Mostek ROS <-> Gazebo dla lewego silnika
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '--ros-args',
                '-p',
                f'config_file:={bridge_params}',
            ],
            output='screen',
        ),

    ])
