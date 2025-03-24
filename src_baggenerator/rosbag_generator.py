#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import os
import sys

class RosbagGeneratorNode(Node):
    def __init__(self):
        super().__init__('rosbag_generator_node')

        # Publishers
        self.publisher_topic_1 = self.create_publisher(String, 'topic_1', 10)
        self.publisher_topic_2 = self.create_publisher(String, 'topic_2', 10)

        # Timer to call the publish function periodically (1Hz)
        self.timer = self.create_timer(1.0, self.publish_data)

        # Timer to stop the node after 30 seconds
        self.shutdown_timer = self.create_timer(30.0, self.stop_node)

        self.start_time = time.time()  # Record the start time

        # Counter for message distinction
        self.counter = 0

    def publish_data(self):
        self.counter += 1

        msg_1 = String()
        msg_1.data = f'Example data for topic 1, counter {self.counter}'
        self.publisher_topic_1.publish(msg_1)

        msg_2 = String()
        msg_2.data = f'Example data for topic 2, counter {self.counter}'
        self.publisher_topic_2.publish(msg_2)

        self.get_logger().info(f"Published: {msg_1.data} to topic_1, {msg_2.data} to topic_2")

    def stop_node(self):
        # Check if 30 seconds have passed
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= 30:
            self.get_logger().info("30 seconds passed. Stopping rosbag_generator_node.")
            rclpy.shutdown()  # Shutdown the ROS2 node after 30 seconds
            os._exit(0)  # Exit the Python process, which will stop the container

def main(args=None):
    rclpy.init(args=args)
    node = RosbagGeneratorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
