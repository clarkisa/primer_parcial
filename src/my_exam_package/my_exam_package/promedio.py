import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from my_interface.msg import CamelMsg


class PromedioNode(Node):

    def __init__(self):
        super().__init__('promedio')

        self.sensor_1 = 0.0
        self.sensor_2 = 0.0
        self.sensor_3 = 0.0

        self.recibido_1 = False
        self.recibido_2 = False
        self.recibido_3 = False

        self.sub1 = self.create_subscription(
            Float32,
            '/sensor_1',
            self.callback_sensor_1,
            10
        )

        self.sub2 = self.create_subscription(
            Float32,
            '/sensor_2',
            self.callback_sensor_2,
            10
        )

        self.sub3 = self.create_subscription(
            Float32,
            '/sensor_3',
            self.callback_sensor_3,
            10
        )

        self.publisher_ = self.create_publisher(
            CamelMsg,
            '/filtered_sensor',
            10
        )

        self.timer = self.create_timer(0.5, self.publicar_promedio)

    def callback_sensor_1(self, msg):
        self.sensor_1 = msg.data
        self.recibido_1 = True

    def callback_sensor_2(self, msg):
        self.sensor_2 = msg.data
        self.recibido_2 = True

    def callback_sensor_3(self, msg):
        self.sensor_3 = msg.data
        self.recibido_3 = True

    def publicar_promedio(self):
        if not (self.recibido_1 and self.recibido_2 and self.recibido_3):
            return

        promedio = (self.sensor_1 + self.sensor_2 + self.sensor_3) / 3.0

        msg = CamelMsg()
        msg.sensor_value = promedio
        msg.name = "filtered_sensor"

        self.publisher_.publish(msg)

        self.get_logger().info(
            f's1={self.sensor_1:.2f}, s2={self.sensor_2:.2f}, s3={self.sensor_3:.2f}, promedio={promedio:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = PromedioNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()