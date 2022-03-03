# The following file contains the class Data which has the following functions:
#       - Stores the start_node, end_node and energy_budget
#       - Import all the datasets

# Import libraries
import json

# Function to store output as txt file
def result_to_txt(name, path, distance, cost):
    with open(name + "_Output.txt", "w") as file:
        file.write("Shortest path found: " + path + '.\n')
        file.write("Shortest distance: " + str(distance) + '.\n')
        file.write("Total energy cost: " + str(cost) + '.')

# Data Class
class Data:

    # Initialise Data Class
    def __init__(self, start_node, end_node, energy_budget):
        self.start_node = start_node
        self.end_node = end_node
        self.energy_budget = energy_budget
        with open("./Data/G.json", "r") as graph:
            self.graph = json.load(graph)
        with open("./Data/Coord.json", "r") as coord:
            self.coord = json.load(coord)
        with open("./Data/Dist.json", "r") as dist:
            self.dist = json.load(dist)
        with open("./Data/Cost.json", "r") as cost:
            self.cost = json.load(cost)

    # Calculate the cost for a given path
    def calculate_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            edge = path[i] + ',' + path[i + 1]
            cost += self.cost[edge]
        return cost

    # Calculate the distance for a given path
    def calculate_distance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            edge = path[i] + ',' + path[i + 1]
            distance += self.dist[edge]
        return distance