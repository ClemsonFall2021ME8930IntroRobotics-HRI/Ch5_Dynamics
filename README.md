# Ch5_Dynamics

To start this simulation download the "Position_Control.ttt" and "Velocity_Control.ttt" CoppeliaSim scenes. The robotic manipulator used is an altered version of the 7 DOF redundant robot given in the CoppeliaSim software. The objects past the "redundantRob_link5" object were deleted to match the manipulator in the second example of the Lagrangian section. In both scenes, two dummy objects were setup to represent the tip of the manipulator and the target object. In the position control scene, inverse kinematics were used to cause the tip of the manipulator to track the target dummy and match it's position. This was done using an altered verison of the CoppeliaSim inverse kinematics tutorial seen in the following link: https://www.coppeliarobotics.com/helpFiles/en/inverseKinematicsTutorial.htm. The altered version used can be seen in the figure below. 

This has to be pasted into a non-threaded child script in the main object, "redundantRobot", which is at the top of the hiearchy. For the velocity control these inverse kinematics were not applied. However, for the velocity control, the control loops for each of the motors were disabled. As this is the only way to perform velocity control on the manipulator. Also, graphs were added for the coordinates for the two dummy objects in order to verify the trajectory of the manipulator tip. This was done using a modified child script from the CoppeliaSim graphs tutorial page, which is seen in the following link: https://www.coppeliarobotics.com/helpFiles/en/graphs.htm. The modified version is shown in the figure below.

With all of this known, the "Dynamics_Simulation.py" needs to also be opened. This python script is split into two different sections. One for the position control scene and one for the velocity control scene. The position control will get information of the manipulator such as link length and link angles. This is then used in the derived equations of motion for the manipulator to find the angular velocities of each link. So, to get this information, run the position control scene in CoppeliaSim. In the python code on line 39, the target objects position can be changed. However, it needs to remain within the manipulators workspace, as well as the x-z plane. It must have the same y-coordinate as the tip, as these are the conditions that the equations of motion were derived in. With the simulation running, run the first section of code by using the "Run Current Cell" button on the top toolbar. This will return all the necessary values for that particular target postion, and find the velocities of the links. Next click on the velocity control scene tab, to open it up. Start the simulation and then go to the python code. Run the velocity control section by clicking within the section and clicking the "Run Current Cell" button. This will apply the velocities found during the postion control simulation to the links
