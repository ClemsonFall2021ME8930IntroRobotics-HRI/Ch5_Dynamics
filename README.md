# Ch5_Dynamics

# Procedure

To start this simulation download the "Position_Control.ttt" and "Velocity_Control.ttt" CoppeliaSim scenes. The robotic manipulator used is an altered version of the 7 DOF redundant robot given in the CoppeliaSim software. The objects past the "redundantRob_link5" object were deleted to match the manipulator in the second example of the Lagrangian section. In both scenes, two dummy objects were setup to represent the tip of the manipulator and the target object. In the position control scene, inverse kinematics were used to cause the tip of the manipulator to track the target dummy and match it's position. This was done using an altered verison of the CoppeliaSim inverse kinematics tutorial seen in the following link: https://www.coppeliarobotics.com/helpFiles/en/inverseKinematicsTutorial.htm. The altered version used can be seen in the figure below. 

![image](https://user-images.githubusercontent.com/95729891/147436456-1bf2d11a-ab56-4549-aec6-7e44e04652e6.png)

This had to be pasted into a non-threaded child script in the main object, "redundantRobot", which is at the top of the hiearchy. For the velocity control these inverse kinematics were not applied. However, for the velocity control, the control loops for each of the motors were disabled. As this is the only way to perform velocity control on the manipulator. Also, graphs were added for the coordinates for the two dummy objects in order to verify the trajectory of the manipulator tip. To add the graphs just right click on the scene and go to add and then graph. A child script had to be created to track the positions. This was done using a modified child script from the CoppeliaSim graphs tutorial page, which is seen in the following link: https://www.coppeliarobotics.com/helpFiles/en/graphs.htm. The modified version is shown in the figure below.

![image](https://user-images.githubusercontent.com/95729891/147436624-81c5fcc8-e91b-447f-93f8-10e51928f6b4.png)

This image represents the x-coordinate child script. For the y and z-coordinate, the graph name in line 2 was changed to the respective coordinate and also the number on lines 12 and 13. The number 2 would represent the y-coordinate, while the number 3 would represent the z-coordinate.

With all of this known, the "Dynamics_Simulation.py" needs to also be opened. This python script is split into two different sections. One for the position control scene and one for the velocity control scene. The position control will get information of the manipulator such as link length and link angles. This is then used in the derived equations of motion for the manipulator to find the angular velocities of each link. So, to get this information, run the position control scene in CoppeliaSim. In the python code on line 39, the target objects position can be changed. However, it needs to remain within the manipulators workspace, as well as the x-z plane. It must have the same y-coordinate as the tip, as these are the conditions that the equations of motion were derived in. With the simulation running, run the first section of code by using the "Run Current Cell" button on the top toolbar. This will return all the necessary values for that particular target postion, and find the velocities of the links. Next click on the velocity control scene tab, to open it up. Start the simulation and then go to the python code. Run the velocity control section by clicking within the section and clicking the "Run Current Cell" button. This will apply the velocities found during the postion control simulation to the links. The graphs can be set to only show when the simluation isn't running, which helps view the graphs better. The graphs will show that the manipulator tip and the target positions overlapped , which show the validity of the equations of motion. Below are three test positions that were performed and their resulting graphs.

# Test 1

This test was performed using a target position on the x-z plane of [.25, .1]. This target position gave the manipulator orientation seen below.

![image](https://user-images.githubusercontent.com/95729891/147511370-8f5f077b-0517-4bbf-bfdf-f250d5cb6218.png)

Applying the found velocities from this orientation to the velocity control scene, gives the graphs below.

![image](https://user-images.githubusercontent.com/95729891/147511556-64c29b01-1b66-4bd2-bd07-b661a6de27df.png)

Since the coordinates intersect simultaneously, this gives the first confirmation of the validity of the equations of motion.

# Test 2

This test was performed using a target position on the x-z plane of [.25, .25]. This target position gave the manipulator orientation seen below. 

![image](https://user-images.githubusercontent.com/95729891/147511714-b5311072-4eb5-4def-9cbd-dd7304364b78.png)

Applying the found velocities from this orientation to the velocity control scene, gives the graphs below.

![image](https://user-images.githubusercontent.com/95729891/147511777-45d70a0e-a708-44c2-9063-bb965f4bd91c.png)

Since the coordinates intersect simultaneously, this gives the second confirmation of the validity of the equations of motion.

# Test 3

This test was performed using a target position on the x-z plane of [.30, .40]. This target position gave the manipulator orientation seen below. 

![image](https://user-images.githubusercontent.com/95729891/147511891-8276c747-49c7-4247-b649-55bafe591487.png)

Applying the found velocities from this orientation to the velocity control scene, gives the graphs below.

![image](https://user-images.githubusercontent.com/95729891/147511978-12785187-9da0-41b1-b75e-9c9e81f4164b.png)

Since the coordinates intersect simultaneously, this gives the third and last confirmation of the validity of the equations of motion.

# Conclusions

Based on these three tests, the original position during the position control scene/code was able to be mimicked by the velocities found using the equations of motion. Due to this the equations of motion are shown to be a valid set of equations, and show just how powerful dynamics can be when modeling physical systems. Obviously manipulators aren't just moving on a 2-dimensional plane, so these simulations can be taken much further by deriving 3-dimensional equations of motion and applying this same method of validity. It can also be applied to mobile robots as well. No matter how far it's taken, it's still a great representation of the mathematical modeling of robots.
