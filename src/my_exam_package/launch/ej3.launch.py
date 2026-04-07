from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_exam_package',
            executable='sensor1_pub',
            name='sensor1_pub'
        ),
        Node(
            package='my_exam_package',
            executable='sensor2_pub',
            name='sensor2_pub'
        ),
        Node(
            package='my_exam_package',
            executable='sensor3_pub',
            name='sensor3_pub'
        ),
        Node(
            package='my_exam_package',
            executable='promedio',
            name='promedio'
        ),
        Node(
            package='my_exam_package',
            executable='display',
            name='display'
        ),
    ])