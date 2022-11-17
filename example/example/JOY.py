import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from rclpy.logging import get_logger
import numpy as np


class JOY(Node):

    def __init__(self):
        super().__init__('JOY')
        self.qos = QoSProfile(depth=10)
        self.pub_twist = self.create_publisher(Twist, '/cmd_vel', self.qos)
        self.sub = self.create_subscription(Joy, '/joy', self.callback, 10)
        self.twist = Twist()
        self.header = Header()

    def callback(self, data):
        global inn
        inn=0
        self.joy = data.buttons
        self.joy2= data.axes
        if np.shape(self.joy)[0]>0:
            inn=1
            self.nemo=self.joy[3]
            self.semo=self.joy[2]
            self.one=self.joy[1]
            self.x=self.joy[0]
        if inn==1:
            vel_msg = Twist()
            if self.nemo==1:
                print("네모")
                #vel_msg.linear.x=self.linear*0.1
                #vel_msg.angular.z=self.angular*1.2

            elif self.one==1:
                print("동그라미")
                #vel_msg.linear.x=self.linear*0.22
                #vel_msg.angular.z=self.angular*2
            elif self.x==1:
                print("엑스")
                #vel_msg.linear.x=0
                #vel_msg.angular.z=0
     


    def cb_timer(self):
        self.timer_inc+=1
        if self.auto_mode == False:
            self.pub_twist.publish(self.twist)


def main(args=None):
    rclpy.init(args=args)
    #data = Joy()
    node = JOY()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


    
if __name__ == '__main__':
    main()