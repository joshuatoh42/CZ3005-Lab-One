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
    # test("1->1363->1358->1357->1356->1276->1273->1277->1269->1267->1268->1284->1283->1282->1255->1253->1260->1259->1249->1246->963->964->962->1002->952->1000->998->994->995->996->987->986->979->980->969->977->989->990->991->2465->2466->2384->2382->2385->2379->2380->2445->2444->2405->2406->2398->2395->2397->2142->2141->2125->2126->2082->2080->2071->1979->1975->1967->1966->1974->1973->1971->1970->1948->1937->1939->1935->1931->1934->1673->1675->1674->1837->1671->1828->1825->1817->1815->1634->1814->1813->1632->1631->1742->1741->1740->1739->1591->1689->1585->1584->1688->1579->1679->1677->104->5680->5418->5431->5425->5424->5422->5413->5412->5411->66->5392->5391->5388->5291->5278->5289->5290->5283->5284->5280->50")