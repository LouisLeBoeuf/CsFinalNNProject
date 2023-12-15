# CS Final Project

**Abstract:**
The simulated-craft-neuralnet-main is the part of the project that will run a simulation and create, train, and spit out a txt file with the full weights of a 5:4:2 neural network. This is then copied and pasted into the controller which will be run in the lab world in webots, and through ros on the turtlebot.

**Introduction:**
The goal for this was to see if I could create and train a neural network in a simulation I wrote that would be robust enough to still control a turtlebot to a desired point.

**Related Works:**
- [Sebastian Lague: Neural Networks series](https://www.youtube.com/watch?v=bVQUSndDllU)
- [Kie Codes: Genetic Algorithm in Python](https://www.youtube.com/watch?v=nhT56blfRpE)
- John Buffer's AutoDrone project, available [here](https://github.com/johnBuffer/AutoDrone)

**Approach:**
For simulation, run Launcher.ipynb (you must have python and pygame installed). Adjust the parameters as you wish, In the config, this means choosing which drone (again I used drone and it should default to this) and turning on or off gravity and adjusting friction, training type, neural network size, etc.

In generator.py, you can adjust the maximum fitness limit, training times, and generation limit.

Once simulation is done go to the savedgenome.txt. This genome should be copied and pasted into webots_ros2_homework1_python.py, and a goal location can be chosen there Similar to homework 1, launch webots, turtlebot bringup, and then run webots_ros2_homework1_python.py as the controller on the turtlebot. You can have the start location anywhere but I would recommend doing it in challenge area 1 or 2, please adjust the goal to also be in the room. As this is very close to the custom simulation, a blank room with walls.

**Assumptions:**
- My "drone" and simulation are close enough to the webots simulated turtlebot to transfer over
- Known environment
- No obstacle avoidance needed
- "blind robot" aside from it's current pose and the goal location

**Results:**

The custom simulation worked well, the drone was much more controllable disabling gravity, occasionally spinning out of control.
I fixed this problem by lowering it's maximum thrust, similar to the turtlebot, it won't be allowed to turn quickly.
As far as putting it in webots simulation, the weights and everything transferred overed, it often undershot the goal 
and the inched towards it, I suspect due to the turtlebot being less responsive to change than the simulation. Turning also seemed to be quite an issue for it.
If I had, maybe a few years haha, I would try to get my custom simulation much more realistic.
Over multiple runs it took on average 50% longer for it to reach the first goal so long as the goal was in front of it.
If the goal was far to the right or left of it, it tended to circe it or run into a wall. Through multiple attempts it reached the goal only 11% of the time if it had 
to turn more than ~30 degrees total. It worked much better in challenge are 1 than in challenge area 2, due to it being wider.

**Conclusion:**
This project provides multiple simulated craft, each with their own unique control schemes (two bidirectional thrusters, single gimbaled thrust, dual gimbaled thrusters, etc.), neural network and genetic algorithm training modules, ability to train the neural networks to fly these craft to their 'goal destinations', and a realtime visualization module to view both the craft and the activity of the neural network.
The drone without gravity is a good enough simulation to transfer most controllability of a trained Neural Network to a turtlebot3 in webots simulation.
I am curious to see how it would do on robots with more or less controllability in webots.