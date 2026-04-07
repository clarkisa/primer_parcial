import rclpy
from rclpy.node import Node

from my_interface.msg import CamelMsg


class SensorDisplay(Node):

    def __init__(self):
        super().__init__('sensor_display_node')

        self.subscription = self.create_subscription(
            CamelMsg,
            '/filtered_sensor',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(
            f'Promedio recibido: {msg.sensor_value:.2f} ({msg.name})'
        )


def main(args=None):
    rclpy.init(args=args)

    node = SensorDisplay()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()