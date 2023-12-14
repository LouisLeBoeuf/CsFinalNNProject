import geneticalgorithms as ga
import realtimeviewer as rtv
from shipsims import drone
from shipsims import gimbaldrone
from shipsims import ship
from shipsims import spinship
import numpy as np

######################################################
#You can change the drone type to 
#sim_class = ship.Ship
#sim_class = spinship.SpinShip
#sim_class = drone.Drone
#sim_class = gimbaldrone.GimbalDrone
#make sure to change the layer sizes to specific drone input and output
#You can change the generation_limit to howver many generations to train
#You can also change pop mode "generate" to "read" to continue previous simulation or generate a fresh population
######################################################


np.random.seed(42);

# population, generation = run_evolution(
#     populate_func=partial(generate_population, size=10, layer_sizes=layer_sizes),
#     fitness_limit = 50000,
#     generation_limit = 200
# )


#ship can thrust in any direction without worry of angles Must have 4 inputs and 2 outputs [4,4,2]
#spinship is one thruster ship  with angle control must have 5 inputs and 2 outputs [5,4,2]
#drone is a 2 thruster ship they can thrust up and down extremely unstable must have 5 inputs and 2 outputs [5,4,2]
#gimbaldrone is a 2 gimballed thruster ship must have 5 inputs and 4 outputs [5,4,4]

ls = [5,4,2] #size of the neural network to use
sim_class = drone.Drone #define which drone type to use spinship. ie gimbaldrone.GimbalDrone
ps = 1/30.0

population, generation = ga.run_evolution(
    # populate_func=partial(read_population),
    sim_class = sim_class,
    pop_mode = "generate", # Generate new genomes or read from previous trial "generate" or "read"
    pop_file = "savedgenome.txt",
    max_time = 15, #max time to allow per generation
    fitness_limit = 50000, #max fitness one goal is worth 10,000
    generation_limit = 500, #how many generations to run
    layer_sizes = ls 
)

view = rtv.RealtimeViewer(population[0], ls, sim_class, ps)
view.start()