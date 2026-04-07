import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class MyPublisher(Node):

    def __init__(self):
        super().__init__('sensor_3_node')
        self.publisher_ = self.create_publisher(Float32, '/sensor_3', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 10.0)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing sensor_3: {msg.data:.2f}')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MyPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()