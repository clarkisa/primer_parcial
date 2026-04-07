import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from robot_a.kinematics import calcular_angulos
from builtin_interfaces.msg import Time


class ControlRobot(Node):

    def __init__(self):
        super().__init__('control_robot')

        self.publisher = self.create_publisher(JointState, '/joint_states', 10)

        self.timer = self.create_timer(1.0, self.move_robot)

    def move_robot(self):
        x, y, z = 2.0, 1.0, 3.0

        t1, t2, t3 = calcular_angulos(x, y, z)

        msg = JointState()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base'   

        msg.name = ['q1', 'q2', 'q3']
        msg.position = [t1, t2, t3]

        self.publisher.publish(msg)

        self.get_logger().info(f'Angles: {t1:.2f}, {t2:.2f}, {t3:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = ControlRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()