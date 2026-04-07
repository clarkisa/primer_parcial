import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt

from robot_a.kinematics import calcular_angulos


class ControlGUI(Node):

    def __init__(self):
        super().__init__('control_gui')

        self.publisher = self.create_publisher(JointState, '/joint_states', 10)

    def mover_robot(self, x, y, z):
        t1, t2, t3 = calcular_angulos(x, y, z)

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['q1', 'q2', 'q3']
        msg.position = [t1, t2, t3]

        self.publisher.publish(msg)


class GUI(QWidget):

    def __init__(self, node):
        super().__init__()

        self.node = node

        self.setWindowTitle("Control XYZ Robot")

        layout = QVBoxLayout()

        self.label = QLabel("X: 1.0  Y: 0.0  Z: 1.5")
        layout.addWidget(self.label)

        self.slider_x = self.crear_slider(layout, "X")
        self.slider_y = self.crear_slider(layout, "Y")
        self.slider_z = self.crear_slider(layout, "Z")

        self.setLayout(layout)

    def crear_slider(self, layout, nombre):
        label = QLabel(nombre)
        layout.addWidget(label)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(300)  # escala 0 → 3.0
        slider.setValue(100)

        slider.valueChanged.connect(self.actualizar)

        layout.addWidget(slider)
        return slider

    def actualizar(self):
        x = self.slider_x.value() / 100.0
        y = self.slider_y.value() / 100.0
        z = self.slider_z.value() / 100.0

        self.label.setText(f"X: {x:.2f}  Y: {y:.2f}  Z: {z:.2f}")

        self.node.mover_robot(x, y, z)


def main():
    rclpy.init()

    node = ControlGUI()

    app = QApplication(sys.argv)
    gui = GUI(node)
    gui.show()

    sys.exit(app.exec_())