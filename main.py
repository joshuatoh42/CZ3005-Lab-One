# Import Required Scripts - Classes & Algorithms
from Classes.Data import Data
import Algorithm.UCS as UCS
import Algorithm.AStar as AStar

# Import Required Libraries
from time import time

# Main Function
def main():
    # Load in the data
    print("Loading data...")
    data = Data("1", "50", 287932)  # Starting Node = 1, Ending Node = 50, Energy Budget = 287932
    print("-----------------------------------------------------------------------------------------------------------------")
    # Task 1 - No Energy Constraint
    print("Commencing Task 1")
    start_time = time()
    UCS.search(data, False) # Commence Uniform-Cost Search without energy constraint
    end_time = time()
    print("Time elapsed: " + str(end_time - start_time))
    print("-----------------------------------------------------------------------------------------------------------------")
    # Task 2
    print("Commencing Task 2")
    start_time = time()
    UCS.search(data, True)  # Commence Uniform-Cost Search with energy constraint
    end_time = time()
    print("Time elapsed: " + str(end_time - start_time))
    print("-----------------------------------------------------------------------------------------------------------------")
    # Task 3 - With Energy Budget
    print("Commencing Task 3 - With Energy Budget")
    start_time = time()
    AStar.search(data, True) # Commence A-Star Search with energy constraint
    end_time = time()
    print("Time elapsed: " + str(end_time - start_time))
    print("-----------------------------------------------------------------------------------------------------------------")
    # Task 3 - Without Energy Budget
    print("Commencing Task 3 - Without Energy Budget")
    start_time = time()
    AStar.search(data, False) # Commence A-Star Search without energy constraint and weight = 1
    end_time = time()
    print("Time elapsed: " + str(end_time - start_time))
    print("-----------------------------------------------------------------------------------------------------------------")

def test(path):
    nodes = path.split("->")
    distance = 0
    cost = 0
    data = Data("1", "50", 287932)
    for node in range(len(nodes) - 1):
        pair = nodes[node] + "," + nodes[node + 1]
        distance += data.dist[pair]
        cost += data.cost[pair]
    print("Testing Path =", path)
    print("Distance =", distance)
    print("Cost =", cost)

# Run the following when the file is ran
if __name__ == "__main__":
    main()