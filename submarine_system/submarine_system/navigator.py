import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from submarine_interfaces.msg import BotPose

class Navigator(Node):
    def __init__(self):
        super().__init__('navigator')
        self.sub = self.create_subscription(String, '/cmd', self.listener_callback, 10)
        self.pub = self.create_publisher(BotPose, '/bot_pose', 10)
        
        # Initial State
        self.x = 0.0
        self.y = 0.0
        self.direction = "North"
        self.directions = ["North", "East", "South", "West"]

    def listener_callback(self, msg):
        cmd = msg.data
        idx = self.directions.index(self.direction)

        if cmd == "turn right":
            self.direction = self.directions[(idx + 1) % 4]
        elif cmd == "turn left":
            self.direction = self.directions[(idx - 1) % 4]
        elif cmd == "forward":
            if self.direction == "North": self.y += 1.0
            elif self.direction == "South": self.y -= 1.0
            elif self.direction == "East": self.x += 1.0
            elif self.direction == "West": self.x -= 1.0
        elif cmd == "backward":
            if self.direction == "North": self.y -= 1.0
            elif self.direction == "South": self.y += 1.0
            elif self.direction == "East": self.x -= 1.0
            elif self.direction == "West": self.x += 1.0

        # Publish updated state
        pose = BotPose()
        pose.x = self.x
        pose.y = self.y
        pose.facing_direction = self.direction
        self.pub.publish(pose)
        
        self.get_logger().info(f'Pose: x={self.x}, y={self.y}, Facing={self.direction}')

def main():
    rclpy.init()
    rclpy.spin(Navigator())
    rclpy.shutdown()
