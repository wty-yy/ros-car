#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped

class TwistConverter(Node):
  def __init__(self):
    super().__init__('twist_to_twist_stamped')
    self.sub = self.create_subscription(
      Twist,
      '/cmd_vel',
      self.callback,
      10)
    self.pub = self.create_publisher(
      TwistStamped,
      '/mecanum_controller/reference',
      10)
    self.frame_id = 'base_footprint'  # 根据实际调整坐标系

  def callback(self, msg):
    stamped_msg = TwistStamped()
    stamped_msg.header.stamp = self.get_clock().now().to_msg()
    stamped_msg.header.frame_id = self.frame_id
    stamped_msg.twist = msg
    self.pub.publish(stamped_msg)

def main(args=None):
  rclpy.init(args=args)
  node = TwistConverter()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()