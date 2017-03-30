#!/usr/bin/env python

import rospy, tf, numpy, math
from kobuki_msgs.msg import BumperEvent
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion
# Add additional imports for each of the message types used


#drive to a goal subscribed as /move_base_simple/goal
def navToPose(goal):

	print "spin!"

	print "move!"
    
	print "spin!"
    
	print "done"
	pass


#This function sequentially calls methods to perform a trajectory.
def executeTrajectory():
    pass  # Delete this 'pass' once implemented




#This function accepts two wheel velocities in radians pers second and a time interval.
#30.5 cm
def spinWheels(u1, u2, time):
	global pub
	global pose
	
	count = time*100
	msg = Twist()	
	dis = 0.305 # Distance between wheels
	radius = 0.038 # Radius of the wheels
	
	msg.linear.x = radius * ((u1+u2) / 2) # Linear Speed the Robot 
	msg.angular.z = radius / dis * ((u1-u2)) # Linear Speed the Robot 

	while count > 0:
		pub.publish(msg)
		count = count - 1;
		rospy.sleep(0.01)
		print pose.pose.position.x
		

	


#This function accepts a speed and a distance for the robot to move in a straight line
def driveStraight(speed, distance):
    """This function accepts a speed and a distance for the robot to move in a straight line"""
    global pose

    initialX = pose.pose.position.x
   
    
#Accepts an angle and makes the robot rotate around it.
def rotate(angle):
    pass  # Delete this 'pass' once implemented



#This function works the same as rotate how ever it does not publish linear velocities.
def driveArc(radius, speed, angle):
    pass  # Delete this 'pass' once implemented





#Bumper Event Callback function
def readBumper(msg):
    if (msg.state == 1):
        # What should happen when the bumper is pressed?
        pass  # Delete this 'pass' once implemented



# (Optional) If you need something to happen repeatedly at a fixed interval, write the code here.
# Start the timer with the following line of code: 
#   rospy.Timer(rospy.Duration(.01), timerCallback)
def timerCallback(event):
    global pose
    pose = Pose()

    #(position, orientation) = odom_list.lookupTransform('...','...', rospy.Time(0)) #finds the position and oriention of two objects relative to each other (hint: this returns arrays, while Pose uses lists)
	
    pass # Delete this 'pass' once implemented

def publishTwist(linearVelocity, angularVelocity):

    global pub
    msg = Twist()
    msg.linear.x = linearVelocity
    msg.angular.z = angularVelocity
    pub.publish(msg)

def readOdom(msg):
	
    pass


# This is the program's main function
if __name__ == '__main__':
    # Change this node name to include your username
    rospy.init_node('cbriggs_lab2')
    rospy.init_node('cbriggs_lab2') 
   


    # These are global variables. Write "global <variable_name>" in any other function to gain access to these global variables 
    global pub
    global pose
    global odom_tf
    global odom_list
   
    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, None, queue_size = 10)
    sub = rospy.Subscriber('/odom', Odometry, readOdom)

    # Replace the elipses '...' in the following lines to set up the publishers and subscribers the lab requires
    #pub = rospy.Publisher('...', ...) # Publisher for commanding robot motion
    #bumper_sub = rospy.Subscriber('...', ..., readBumper, queue_size=1) # Callback function to handle bumper events

    

    # Use this object to get the robot's Odometry 
    odom_list = tf.TransformListener()
    
    # Use this command to make the program wait for some seconds
    rospy.sleep(rospy.Duration(1, 0))
    print "Starting Lab 2"

    #make the robot keep doing something...
    #rospy.Timer(rospy.Duration(...), timerCallback)

    # Make the robot do stuff...
    
    spinWheels(6, 4, 3)

    print "Lab 2 complete!"


