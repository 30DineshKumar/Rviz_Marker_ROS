import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker, MarkerArray


class MarkerArrayPublisher(Node):
    def __init__(self):
        super().__init__('marker_array_publisher')
        self.publisher_ = self.create_publisher(MarkerArray, 'marker_array', 10)
        self.timer_period = 1.0  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        marker_array = MarkerArray()

        # Cylinder Marker
        cylinder_marker = Marker()
        cylinder_marker.header.frame_id = "map"
        cylinder_marker.header.stamp = self.get_clock().now().to_msg()
        cylinder_marker.ns = "cylinder"
        cylinder_marker.id = 0
        cylinder_marker.type = Marker.CYLINDER
        cylinder_marker.action = Marker.ADD
        cylinder_marker.pose.position.x = 0.0
        cylinder_marker.pose.position.y = 0.0
        cylinder_marker.pose.position.z = 0.5
        cylinder_marker.pose.orientation.x = 0.0
        cylinder_marker.pose.orientation.y = 0.0
        cylinder_marker.pose.orientation.z = 0.0
        cylinder_marker.pose.orientation.w = 1.0
        cylinder_marker.scale.x = 1.0
        cylinder_marker.scale.y = 1.0
        cylinder_marker.scale.z = 1.0
        cylinder_marker.color.a = 1.0
        cylinder_marker.color.r = 0.0
        cylinder_marker.color.g = 1.0
        cylinder_marker.color.b = 0.0

        marker_array.markers.append(cylinder_marker)

        # Sphere List Marker
        sphere_marker = Marker()
        sphere_marker.header.frame_id = "map"
        sphere_marker.header.stamp = self.get_clock().now().to_msg()
        sphere_marker.ns = "spheres"
        sphere_marker.id = 1
        sphere_marker.type = Marker.SPHERE_LIST
        sphere_marker.action = Marker.ADD
        sphere_marker.pose.orientation.w = 1.0
        sphere_marker.scale.x = 0.2
        sphere_marker.scale.y = 0.2
        sphere_marker.scale.z = 0.2

        for _ in range(10):
            p = Point()
            p.x = random.random() * 4 - 2
            p.y = random.random() * 4 - 2
            p.z = random.random() * 4 - 2
            sphere_marker.points.append(p)
            sphere_marker.colors.append(ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0))

        marker_array.markers.append(sphere_marker)

        self.publisher_.publish(marker_array)


def main(args=None):
    rclpy.init(args=args)
    marker_array_publisher = MarkerArrayPublisher()
    rclpy.spin(marker_array_publisher)
    marker_array_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()