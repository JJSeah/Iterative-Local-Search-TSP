# Iterated Local Search for the Traveling Salesman Problem
This Python script implements an Iterated Local Search (ILS) algorithm to solve the Traveling Salesman Problem (TSP). The TSP is a classic algorithmic problem in the field of computer science and operations research, focusing on optimization. In this problem, a salesman is given a list of cities and must determine the shortest route that allows him to visit each city once and return to his original location.

### Features
- The script uses the 2-opt swap to perform local search and improve the route iteratively.
- The script uses a double bridge move to perturb the route.
- The script uses the nearest neighbour heuristic to generate an initial solution.
- The script uses a simple stopping criterion: the number of iterations without improvement.
### How to Run
1. Ensure that you have Python installed on your machine.
2. Download the IteratedLocalSearch.py file.
3. Prepare your data in the same format as berlin52.txt. The file should contain one city per line, with the x and y coordinates separated by a space.
4. Run the script using the command python IteratedLocalSearch.py.
### Code Structure
- `calculate_distance(point1, point2)`: Calculates the Euclidean distance between two points.
- `calculate_route_distance(route, coordinates)`: Calculates the total distance of a route.
- `find_nearest_neighbour(coordinates)`: Finds the nearest neighbour for a given set of coordinates.
- `perform_2_opt_swap(route, i, k)`: Performs a 2-opt swap on a route.
- `perform_local_search(route, coordinates)`: Performs local search on a route.
- `perform_double_bridge(route)`: Performs a double bridge move on a route.
- `perturb_route(route)`: Perturbs a route.
- `perform_iterated_local_search(initial_route, coordinates)`: Performs the Iterated Local Search algorithm.
### Note
The stopping criterion for the ILS algorithm in this code is the number of iterations without improvement. If the algorithm goes through a certain number of iterations `(defined by NO_IMPROVE_LIMIT) `without finding a better solution, it stops. Other stopping criteria could be used, such as a time limit or a minimum improvement.