import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import tkinter as tk

from robot_bio.kinematics import calcular_angulos


class GUIControl(Node):

    def __init__(self):
        super().__init__('gui_control')

        self.publisher = self.create_publisher(JointState, '/joint_states', 10)

        self.root = tk.Tk()
        self.root.title("Control por Posición (Cinemática Inversa)")

        # SLIDER X (auto mueve)
        self.x_slider = tk.Scale(
            self.root, from_=-0.2, to=0.2,
            resolution=0.01, orient=tk.HORIZONTAL,
            label="X", command=self.auto_mover
        )
        self.x_slider.pack()

        # SLIDER Y (auto mueve)
        self.y_slider = tk.Scale(
            self.root, from_=-0.2, to=0.2,
            resolution=0.01, orient=tk.HORIZONTAL,
            label="Y", command=self.auto_mover
        )
        self.y_slider.pack()

        # SLIDER q4 (para hacerlo más vistoso)
        self.q4_slider = tk.Scale(
            self.root, from_=-3.14, to=3.14,
            resolution=0.01, orient=tk.HORIZONTAL,
            label="q4 (orientación)"
        )
        self.q4_slider.pack()

    # se ejecuta automáticamente al mover sliders
    def auto_mover(self, value):
        self.mover_robot()

    def mover_robot(self):
        x = self.x_slider.get()
        y = self.y_slider.get()
        q4 = self.q4_slider.get()

        # cinemática inversa
        q1, q2, q3 = calcular_angulos(x, y, 0)

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['q1', 'q2', 'q3', 'q4']
        msg.position = [q1, q2, q3, q4]

        self.publisher.publish(msg)

        self.get_logger().info(
            f"X:{x:.2f} Y:{y:.2f} → Angles: {q1:.2f}, {q2:.2f}, {q3:.2f}, {q4:.2f}"
        )

    def run(self):
        self.root.mainloop()


def main(args=None):
    rclpy.init(args=args)
    node = GUIControl()

    import threading

    #  ROS en paralelo
    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()

    #  GUI
    node.run()

    node.destroy_node()
    rclpy.shutdown()