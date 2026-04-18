import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Commander(Node):
    def __init__(self):
        super().__init__('commander')
        self.publisher_ = self.create_publisher(String, '/cmd', 10)
        self.get_logger().info('Commander Node Started.')
        self.get_logger().info('Enter commands: forward, backward, turn left, turn right')
        self.run_loop()

    def run_loop(self):
        while rclpy.ok():
            user_input = input("Enter Command: ").lower().strip()
            if user_input in ['forward', 'backward', 'turn left', 'turn right']:
                msg = String()
                msg.data = user_input
                self.publisher_.publish(msg)
            else:
                print("Invalid command! Try again.")

def main(args=None):
    rclpy.init(args=args)
    node = Commander()
    # No spin() here because we are using a manual input loop
    rclpy.shutdown()
