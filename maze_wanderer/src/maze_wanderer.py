import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

# Function that used publisher
def drive(left, right):
	flw_pub.publish(left)
	blw_pub.publish(left)

	frw_pub.publish(right)
	brw_pub.publish(right)

def handleNewData(data):
	midpoint = len(data.ranges)/2
	distance = data.ranges[midpoint]
	if distance > 0.5:
		drive(1.0, 1.0)
		print("Driving")
	else:
		drive(0.5, -0.5)
		print("Turning")

# Intitalize ros
rospy.init_node("maze_wanderer")

# Created publisher
flw_pub = rospy.Publisher("/front_left_wheel_controller/command", Float64, queue_size=0)
frw_pub = rospy.Publisher("/front_right_wheel_controller/command", Float64, queue_size=0)
blw_pub = rospy.Publisher("/back_left_wheel_controller/command", Float64, queue_size=0)
brw_pub = rospy.Publisher("/back_right_wheel_controller/command", Float64, queue_size=0)

laser = rospy.Subscriber("/scan", LaserScan, handleNewData)

rospy.spin()

