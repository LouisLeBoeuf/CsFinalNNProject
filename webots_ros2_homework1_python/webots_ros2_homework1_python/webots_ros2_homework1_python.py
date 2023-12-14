from turtle import position

import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
# import the Twist module from geometry_msgs interface
from geometry_msgs.msg import Twist
# import the LaserScan module from sensor_msgs interface
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
# import Quality of Service library, to set the correct profile and reliability in order to read sensor data.
from rclpy.qos import ReliabilityPolicy, QoSProfile
import math
import numpy as np

#paste the Genome in here:
nn = [0]

goal_location_x = 5
goal_location_y = 5
current_velocity_x = 0
current_velocity_y = 0
angle = 0
inputs = 0

class RandomWalk(Node):

    def __init__(self):
        # Initialize the publisher
        super().__init__('random_walk_node')
        self.scan_cleaned = []
        self.stall = False
        self.turtlebot_moving = False
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber1 = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback1,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        self.subscriber2 = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback2,
            QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        self.laser_forward = 0
        self.odom_data = 0
        timer_period = 0.5
        self.pose_saved=''
        self.cmd = Twist()
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def listener_callback1(self, msg1):
        #self.get_logger().info('scan: "%s"' % msg1.ranges)
        scan = msg1.ranges
        self.scan_cleaned = []
       
        #self.get_logger().info('scan: "%s"' % scan)
        # Assume 360 range measurements
        for reading in scan:
            if reading == float('Inf'):
                self.scan_cleaned.append(3.5)
            elif math.isnan(reading):
                self.scan_cleaned.append(0.0)
            else:
            	self.scan_cleaned.append(reading)


    def listener_callback2(self, msg2):
        position = msg2.pose.pose.position
        orientation = msg2.pose.pose.orientation
        global (posx, posy, posz) = (position.x, position.y, position.z)
        global (qx, qy, qz, qw) = (orientation.x, orientation.y, orientation.z, orientation.w)
        self.get_logger().info('self position: {},{},{}'.format(posx,posy,posz));
        # similarly for twist message if you need
        self.pose_saved=position
        return None


    def predict_outputs(inputs, weights):
        # Ensure the number of inputs matches the input layer size
        assert len(inputs) == weights[0].shape[1], "Mismatch in the number of inputs"

        # Convert inputs to a numpy array
        a = np.array(inputs).reshape((len(inputs), 1))

        # Perform forward propagation through the network
        for w in weights:
            z = np.dot(w, a)
            a = nn.activation(z)

        # The final 'a' contains the predictions
        predictions = a.flatten()

        # Assuming your network has two output neurons for linear_velocity_x and linear_velocity_y
        linear_velocity_x, linear_velocity_y = predictions[:2]

        return linear_velocity_x, linear_velocity_y

    def timer_callback(self):
        if (len(self.scan_cleaned)==0):
    	    self.turtlebot_moving = False
    	    return

        inputs = [self.linear.x, -self.linear.x, self.position.x-goal_location_x, self.position.y-goal_location_y, self.orientation.z]

        linear_velocity_x, linear_velocity_y = self.predict_outputs(inputs, nn)
        self.cmd.linear.x = linear_velocity_x
        self.cmd.linear.y = linear_velocity_y




def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    random_walk_node = RandomWalk()
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(random_walk_node)
    # Explicity destroy the node
    random_walk_node.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()



if __name__ == '__main__':
    main()
