#!/usr/bin/env python3
import numpy as np

target_position = np.array([0.0, 0.0, 10])
def cmd_pos(x,y,z,h):
	x=x
	y=y
	z=z
	h=h
	cmd_p = ([x,y,z,h])
	print(cmd_p)
	return cmd_p


def calculate_box():
	box_flight_plan = [[10,0,target_position[2],0],[10,10,target_position[2],0],[0,10,target_position[2],0],[0,0,target_position[2],0]]
	return box_flight_plan

flight_plan = calculate_box()

def waypoint_transition():
	
	
	return flight_plan.pop(0)



pos = waypoint_transition()
while 1 ==1 :
	cmd_pos(*pos)

	