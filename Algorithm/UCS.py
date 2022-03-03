# Import required libraries and classes
from queue import PriorityQueue
from Classes.Data import result_to_txt

# Uniform-Cost Search Algorithm
def search(Data, has_energy_constraint):
    # Number of paths that did not satisfy energy constraint
    fail_count = 0
    # File name based on whether there is energy constraint
    if has_energy_constraint:
        file_name = "Task2_ucs_with_energy_constraint"
    else:
        file_name = "Task1_ucs_without_energy_constraint"
    # Start Uniform-Cost Search
    print("Initialising Uniform-Cost Search...")
    # List of paths aka frontier - priority given to lowest distance
    paths = PriorityQueue()
    # Structure of Queue (Distance, Cost, Node) so paths will be automatically sorted according to the shortest distance
    paths.put((0, 0, Data.start_node))
    # Empty list to initialise list of nodes that have been explored
    explored = []
    # Start the search
    print("Starting Uniform-Cost Search...")
    # As long as priority queue has vertices
    while paths:
        # Shortest path in the priority queue
        curr_distance, curr_cost, curr_path = paths.get()
        # Get the last node added to the path
        curr_node = curr_path[-1]
        # Mark the node as explored since the shortest path to this node has been found
        explored.append(curr_node)

        # Destination Reached - Store results to output
        if curr_node == Data.end_node:
            path = '->'.join(curr_path)
            print("Shortest path: " + path + '.')
            distance = Data.calculate_distance(curr_path)
            print("Shortest distance: " + str(distance) + '.')
            print("Total energy cost: " + str(curr_cost) + '.')
            print("Creating output file...")
            result_to_txt(file_name, path, distance, curr_cost)
            print("Number of path explored before finding shortest path: " + str(fail_count))
            return "UCS COMPLETE"

        for neighbour in Data.graph[curr_node]:
            # If neighbour has not been explored, explore the path
            if neighbour not in explored:
                # Create a new path using the current path it is exploring
                new_path = list(curr_path)
                # Add current neighbour as new node on path
                new_path.append(neighbour)
                # Get the distance between the current node and its neighbour
                node_pair = curr_node + ',' + new_path[-1]
                distance = Data.dist[node_pair]
                # New total distance traversed after adding neighobur
                new_distance = distance + curr_distance
                # Energy cost of neighbour
                cost = Data.cost[node_pair]
                # New total energy cost after adding cost of neighbour
                new_cost = cost + curr_cost
                # Check if there is energy constraint
                if has_energy_constraint:
                    # Check if cost is within the energy constraint
                    if new_cost <= Data.energy_budget:
                        paths.put((new_distance, new_cost, new_path))
                    # Add to failed path if path exceeds energy cost
                    else:
                        fail_count += 1
                # If there is no energy constraint, check is not needed
                else:
                    paths.put((new_distance, new_cost, new_path))

    # No valid path if no more vertices are in the Priority Queue
    return "No path found from " + Data.start_node + " to " + Data.end_node
