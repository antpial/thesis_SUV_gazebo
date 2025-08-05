from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='gz_bridge',
            output='screen',
            arguments=[
                '--config-file',
                'src/teleop_nav/launch/example_bridge.yaml'
            ]
        )
    ])
