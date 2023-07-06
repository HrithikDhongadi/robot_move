#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def publish_joint_trajectory():
    rospy.init_node('joint_trajectory_publisher', anonymous=True)
    pub = rospy.Publisher('/robot_arm_controller/command', JointTrajectory, queue_size=10)

    joint_trajectory = JointTrajectory()
    joint_trajectory.header.stamp = rospy.Time.now()
    joint_trajectory.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5']

    point = JointTrajectoryPoint()
    point.positions = [0.0, 0.0, 0.0, 0.0, 0.0]
    point.velocities = [0.2, 1, 0.0, 0.0, 0.0]
    point.accelerations = [0.0, 0.0, 0.0, 0.0, 0.0]
    point.effort = [0.0, 0.0, 0.0, 0.0, 0.0]
    point.time_from_start = rospy.Duration(1)

    joint_trajectory.points.append(point)

    rate = rospy.Rate(1)  # Publish at 10 Hz
    while not rospy.is_shutdown():
        pub.publish(joint_trajectory)
        rate.sleep()


if __name__ == '__main__':
    try:
        publish_joint_trajectory()
    except rospy.ROSInterruptException:
        pass
