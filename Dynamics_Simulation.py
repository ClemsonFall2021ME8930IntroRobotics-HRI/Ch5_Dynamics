# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

#Position Control

import math
try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')
    
    errorCode, target = sim.simxGetObjectHandle(clientID,'redundantRob_target',sim.simx_opmode_blocking)
    sim.simxSetObjectPosition(clientID, target, -1, [+3.0890e-01, -1.3035e-07, +4.9512e-01], sim.simx_opmode_blocking)
    
    errorCode, link1 = sim.simxGetObjectHandle(clientID,'redundantRob_link2',sim.simx_opmode_blocking)
    link1_min = sim.simxGetObjectFloatParameter(clientID, link1, 17, sim.simx_opmode_blocking)
    link1_max = sim.simxGetObjectFloatParameter(clientID, link1, 20, sim.simx_opmode_blocking)
    
    sim.simxSetObjectPosition(clientID, target, -1, [.25, -1.3035e-07, .1], sim.simx_opmode_blocking )
    pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_blocking)
    
    errorCode, shoulder = sim.simxGetObjectHandle(clientID,'redundantRob_joint2',sim.simx_opmode_blocking)
    x = sim.simxGetJointPosition(clientID, shoulder, sim.simx_opmode_blocking)
    shoulder_angle = x[1]*180/math.pi
    
    errorCode, elbow = sim.simxGetObjectHandle(clientID,'redundantRob_joint4',sim.simx_opmode_blocking)
    x = sim.simxGetJointPosition(clientID, elbow, sim.simx_opmode_blocking)
    elbow_angle = x[1]*180/math.pi
    
    x = sim.simxGetJointForce(clientID, shoulder, sim.simx_opmode_blocking)
    shoulder_torque = x[1]
    x = sim.simxGetJointForce(clientID, elbow, sim.simx_opmode_blocking)
    elbow_torque = x[1]
    
    link1_length = link1_max[1] - link1_min[1]
    link2_length = link1_length
    
    link1_mass = 10
    link2_mass = 20
    
    c121 = -1*link2_mass*link1_length*(link2_length/2)*math.sin(math.radians(elbow_angle))
    c112 = -1*c121
    c211 = c121
    c221 = c121
    
    g1 = (link1_mass*(link1_length/2) + link2_mass*(link1_length))*9.81*math.sin(math.radians(shoulder_angle)) + link2_mass*(link2_length/2)*9.81*math.cos(math.radians(shoulder_angle+elbow_angle))
    g2 = link2_mass*(link2_length/2)*9.81*math.cos(math.radians(shoulder_angle+elbow_angle))  
    
    link1_velocity = math.sqrt((elbow_torque-g2)/c112)
    
    a = c221
    b = (c121*link1_velocity + c211*link1_velocity)
    c = g1 - shoulder_torque
    
    d = -1*((b*b) - (4*a*c))
    
    link2_velocity1 = (-b + math.sqrt(d))/(2*a)
    link2_velocity2 = (-b - math.sqrt(d))/(2*a)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')

#%%Velocity Control

try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')
    
    errorCode, target = sim.simxGetObjectHandle(clientID,'redundantRob_target',sim.simx_opmode_blocking)
    sim.simxSetObjectPosition(clientID, target, -1, pos[1], sim.simx_opmode_blocking)
    
    errorCode, shoulder_y = sim.simxGetObjectHandle(clientID,'redundantRob_joint2',sim.simx_opmode_blocking)
    errorcode = sim.simxSetJointTargetPosition(clientID, shoulder_y, 0 ,sim.simx_opmode_streaming)
    
    errorCode, elbow_y = sim.simxGetObjectHandle(clientID,'redundantRob_joint4',sim.simx_opmode_blocking)
    errorcode = sim.simxSetJointTargetPosition(clientID, elbow_y, 0 ,sim.simx_opmode_streaming)
    
    errorCode, shoulder_y = sim.simxGetObjectHandle(clientID,'redundantRob_joint2',sim.simx_opmode_blocking)
    errorcode = sim.simxSetJointTargetVelocity(clientID, shoulder_y, -1*link1_velocity, sim.simx_opmode_streaming)
    
    errorCode, elbow_y = sim.simxGetObjectHandle(clientID,'redundantRob_joint4',sim.simx_opmode_blocking)
    errorcode = sim.simxSetJointTargetVelocity(clientID, elbow_y, link2_velocity2 ,sim.simx_opmode_streaming)
    
else:
    print ('Failed connecting to remote API server')
print ('Program ended')