from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('robot_bio')
    urdf_file = os.path.join(pkg_path, 'urdf', 'robot_bio.urdf')

    return LaunchDescription([

        # Publica el robot
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_file).read()}],
            output='screen'
        ),

        # TU GUI (cinemática inversa)
        Node(
            package='robot_bio',
            executable='gui_control',   
            output='screen'
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),
    ])