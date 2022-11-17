import rclpy
from serial import Serial
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import sys
from time import sleep

class USART(Node):

    def __init__(self):
        super().__init__('USART')
        qos_profile = QoSProfile(depth=10)
        self.publisher_ = self.create_publisher(String, 'USART', qos_profile)
        timer_period = 1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    
    def timer_callback(self):
        msg = String()
        if ser.readable():
            cc=str(ser.readline(), 'UTF-8')
            #b'Test\n' 과 같이 들어오기에 
            #print(cc[2:-3:])
            #print(cc)
            #sys.stdout.write(msg)
            msg.data = cc
            print(msg.data)
            self.publisher_.publish(msg)    
            #self.get_logger().info('Publishing: "%s"' % msg.data)
            ser.flush()
            ser.reset_output_buffer()
            ser.reset_input_buffer()
            cc=''
        
        #ser.write(cc)




def main(args=None):

    global ser
    ser = Serial('/dev/ttyACM0', baudrate=115200, timeout=1)

    rclpy.init(args=args)

    node = USART()
    try:
        rclpy.spin(node)
    
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()