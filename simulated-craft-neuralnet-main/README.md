# CS Final Projec

**Abstract:**
The simulated-craft-neuralnet-main is the part of the project that will run a simulation and
create, train, and spit out a txt file with the full weights of a 5:4:2 neural network. This is then copied and pasted
into the controller which will be run in the lab world in webots, and through ros on the turtlebot.

This Portion of the project is custom simulation and training for the neural network.
I used the "drone" and adjusted it to be as similar to a turtlebot as possible:
- Adjusting Friction
- Disabling Gravity

They are drone.py and looks like:
class Drone():
    max_speed = 5
    GRAVITY = 0 #effectively turns it off, default is 750
    scale = .5
    arm_length = 40 #Size from CoM to each wheel
    MAXTHRUST = 2000.0 
    MOI = 3 #moment of intertia

So for simulation you can run Launcher.ipynb (you must have python and pygame installed).
Adjust the parameters as you wish, In the config, this means choosing which drone (again I used drone and it should default to this)
and turning on or off gravity and adjusting friction, training type, neural network size, etc.

In generator.py you can adjust the maximum fitness limit, training times, and generation limit.

Once simulation is done go to the savedgenome.txt 
This genome should be copied and pasted into webots_ros2_homework1_python.py and a goal location can be chosen there
Similar to homework 1, launch webots, turtlebot bringup, and then run webots_ros2_homework1_python.py as the controller on the
turtlebot. You can have the start location anywhere but I would recommend doing it in challenge area 1 or 2, please adjust the 
goal to also be in the room. As this is very close to the custom simulation, a blank room with walls.



# simulated-craft-neuralnet
Controlling simulated spacecraft with genetic algorithm & amp; neural network

If you wish to run this project, you will need:
- pygame

Run generator.py and edit parameters within to get see how training and simulation works.

# What is this project?
This project provides:
- Multiple simlulated craft, each with their own unique control schemes (two bidirectional thrusters, single gimbaled thrust, dual gimbaled thrusters, etc.)
- Neural network and genetic algorithm training modules
- Ability to train the neural networks to fly these craft to their 'goal destinations'
- A realtime visualization module to view both the craft and the activity of the neural network



# Example
Here's the results after 500 generations of evolution:

https://user-images.githubusercontent.com/69018340/120042115-18caa000-bfcf-11eb-86e0-71c8069b70dd.mp4

As you can see, there is still some room for improvement, especially with this complex dual-thruster configuration.

This project was inspired by John Buffer's AutoDrone project, available [here](https://github.com/johnBuffer/AutoDrone)

Other resources used:

[Sebastian Lague: Neural Networks series](https://www.youtube.com/watch?v=bVQUSndDllU)

[Kie Codes: Genetic Algorithm in Python](https://www.youtube.com/watch?v=nhT56blfRpE)






# Homework 1 ROS2 Notes


### TO INSTALL PACKAGE FOR ASSIGNMENT 

1. Set up environment variables for ROS. Make sure to replace '/home/rpi/shared' with your own shared folder location
<pre>source /opt/ros/humble/setup.bash
export WEBOTS_SHARED_FOLDER=/Users/monicaherzog/shared:/home/rpi/shared
</pre>

2. Fork your own repository of f23_robotics (using web interface)

3. Clone your fork
<pre>
git clone <your github url for this repository>
</pre>

4. Make the package (for python, it really just installs the files
<pre>
cd f23_robotics
colcon build
</pre>

5. Set up variables to use the package you just created
<pre>
source install/setup.bash
</pre>

6. Start webots simulation with connect back to ROS in the virtual machine
<pre>
ros2 launch webots_ros2_homework1_python f23_robotics_1_launch.py
</pre>


### TEST THE CONNECTION BETWEEN ROS2 AND WEBOTS

Test the connection between webots and ROS, use a ROS based ASCII keyboard to move the simulated robot in Webots

1. Open another terminal

2. Redo the source commands (you can add to your bash to execute it automatically each time) 
<pre>
source /opt/ros/humble/setup.bash
source install/setup.bash
</pre>

3. Run the ROS-based keyboard
<pre>
ros2 run teleop_twist_keyboard teleop_twist_keyboard
</pre>


### TO VISUALIZE LASER DATA

1. Open another terminal

2. Redo the source commands (you can add to your bash to execute it automatically each time) 
<pre>
source /opt/ros/humble/setup.bash
source install/setup.bash
</pre>

3. Run the ROS-based keyboard
<pre>
ros2 run teleop_twist_keyboard teleop_twist_keyboard
</pre>
<pre>
  rviz2
</pre>

### RUN SAMPLE CONTROLLER

<pre>
ros2 run webots_ros2_homework1_python webots_ros2_homework1_python
</pre>



# simulated-craft-neuralnet
Controlling simulated spacecraft with genetic algorithm &amp; neural network

If you wish to run this project, you will need:
- pygame

NOTE: This is still a work in progress.
The user-friendly interface is not complete. Run generator.py and edit parameters within to get an idea of how this project works (sorry).

# What is this project?
This project provides:
- Multiple simlulated craft, each with their own unique control schemes (two bidirectional thrusters, single gimbaled thrust, dual gimbaled thrusters, etc.)
- Neural network and genetic algorithm training modules
- Ability to train the neural networks to fly these craft to their 'goal destinations'
- A realtime visualization module to view both the craft and the activity of the neural network

# Example
Here's the results after 500 generations of evolution:

https://user-images.githubusercontent.com/69018340/120042115-18caa000-bfcf-11eb-86e0-71c8069b70dd.mp4

As you can see, there is still some room for improvement, especially with this complex dual-thruster configuration.

This project was inspired by John Buffer's AutoDrone project, available [here](https://github.com/johnBuffer/AutoDrone)

Other resources used:

[Sebastian Lague: Neural Networks series](https://www.youtube.com/watch?v=bVQUSndDllU)

[Kie Codes: Genetic Algorithm in Python](https://www.youtube.com/watch?v=nhT56blfRpE)
