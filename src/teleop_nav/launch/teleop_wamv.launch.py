from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Mostek ROS <-> Gazebo dla lewego silnika
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='gz_bridge_left',
            arguments=[
                '/model/wamV/joint/left_engine_propeller_joint/cmd_thrust@std_msgs/msg/Float64@gz.msgs.Double'
            ],
            output='screen'
        ),

        # Mostek ROS <-> Gazebo dla prawego silnika
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='gz_bridge_right',
            arguments=[
                '/model/wamV/joint/right_engine_propeller_joint/cmd_thrust@std_msgs/msg/Float64@gz.msgs.Double'
            ],
            output='screen'
        ),

        # Twój node teleop
        Node(
            package='teleop_nav',  # 🡐 Zmień na nazwę swojego pakietu
            executable='teleop_nav',  # 🡐 Zmień jeśli inna nazwa
            name='teleop_nav',
            output='screen',
        ),
    ])
