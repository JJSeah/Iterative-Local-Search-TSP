import math
from random import shuffle, seed, randint

# Constants
X, Y = 0, 1
MAX_COORDINATES = 52
NO_IMPROVE_LIMIT = 15
MAX_ITER = 50
SEED = 0

# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt(((point1[X]-point2[X])**2) + ((point1[Y]-point2[Y])**2))

# Function to calculate total distance of a route
def calculate_route_distance(route, coordinates):
    return sum(calculate_distance(coordinates[route[i]], coordinates[route[i-1]]) for i in range(1, len(route)))

# Function to find the nearest neighbour for a given set of coordinates
def find_nearest_neighbour(coordinates):
    visited = [False]*len(coordinates)
    current_index = 1
    total_distance = 0
    order = [current_index]

    while sum(visited) < MAX_COORDINATES:
        visited[current_index] = True
        min_distance = math.inf
        for index, coordinate in enumerate(coordinates):
            if not visited[index]:
                distance = calculate_distance(coordinate, coordinates[current_index])
                if distance < min_distance:
                    min_distance = distance
                    min_distance_index = index
        current_index = min_distance_index
        order.append(min_distance_index)
        total_distance += min_distance
        visited[min_distance_index] = True
    return order, total_distance

# Function to perform 2-opt swap on a route
def perform_2_opt_swap(route, i, k):
    return route[:i] + route[i:k][::-1] + route[k:]

# Function to perform local search on a route
def perform_local_search(route, coordinates):
    total_distance = calculate_route_distance(route, coordinates)
    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            new_route = perform_2_opt_swap(route[:], i, j)
            new_distance = calculate_route_distance(new_route, coordinates)
            if new_distance < total_distance:
                total_distance = new_distance
                route = new_route
    return route

# Function to perform double bridge move on a route
def perform_double_bridge(route):
    i, j, k = [randint(0, len(route)-1)//4 for _ in range(3)]
    return route[:i] + route[k:] + route[j:k] + route[i:j]

# Function to perturb a route
def perturb_route(route):
    return perform_double_bridge(route[:])

# Function to perform Iterated Local Search
def perform_iterated_local_search(initial_route, coordinates):
    # Step 1: Initialization
    route = initial_route[:]

    # Step 2: Local Search
    route = perform_local_search(route, coordinates)
    min_distance = calculate_route_distance(route, coordinates)
    print(f"Distance after initial local search: {min_distance}")
    no_improve = 0

    for _ in range(MAX_ITER):
        # Step 3: Perturbation
        perturbed_route = perturb_route(route[:])

        # Step 2: Local Search (again)
        perturbed_route = perform_local_search(perturbed_route, coordinates)
        distance = calculate_route_distance(perturbed_route, coordinates)

        # Step 4: Acceptance Criterion
        if distance < min_distance:
            min_distance = distance
            route = perturbed_route
            no_improve = 0  # reset the counter when improvement is made
        else:
            no_improve += 1  # increment the counter when no improvement

        # Step 5: Stopping Criterion
        # In this case, the stopping criterion is simply the number of iterations.
        # You could also add other criteria, like a time limit or a minimum improvement.
        if no_improve >= NO_IMPROVE_LIMIT:
            break

    print(f"Distance after Iterated Local Search: {min_distance}")
    return route

# Reading the file containing coordinates
with open('berlin52.txt', 'r') as file:
    lines = file.readlines()

# Parsing the coordinates from the file
coordinates = [list(map(int, line.strip().split())) for line in lines]

seed(SEED)
shuffle(coordinates)

# Getting the initial route and distance using nearest neighbour
initial_route, initial_distance = find_nearest_neighbour(coordinates)
print(f"Distance from Nearest Neighbour: {initial_distance}")

# Running the Iterated Local Search
perform_iterated_local_search(initial_route, coordinates)