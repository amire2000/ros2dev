import rclpy
 
from std_msgs.msg import String
 
 
def main(args=None):
    rclpy.init(args=args)
 
    node = rclpy.create_node('pub_node')
    publisher = node.create_publisher(String, 'hello_msg')
 
    msg = String()
    
    def timer_callback():
        msg.data = 'hello pub'
        node.get_logger().info('Publishing message: "%s"' % msg.data)
        publisher.publish(msg)
 
    timer_period = 0.5  # seconds
    timer = node.create_timer(timer_period, timer_callback)
 
    rclpy.spin(node)
 
    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()