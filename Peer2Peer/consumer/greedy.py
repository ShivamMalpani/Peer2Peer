import math


class Greedy:
    def euclidean_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def nearest_unvisited_customer(self, depot, unvisited_customers, customer_locations):
        depot_location = depot
        nearest_distance = float('inf')
        nearest_customer = None

        for customer in unvisited_customers:
            distance = self.euclidean_distance(depot_location, customer_locations[customer])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_customer = customer

        return nearest_customer

    def nearest_neighbor_mtsp(self, depot_locations, customer_locations):
        num_depots = len(depot_locations)
        num_customers = len(customer_locations)
        num_drivers = num_depots
        unvisited_customers = set(range(num_customers))
        routes = [[] for _ in range(num_drivers)]

        for driver in range(num_drivers):
            current_depot = driver
            current_route = routes[driver]
            current_route.append(current_depot)

            while unvisited_customers:
                nearest_customer = self.nearest_unvisited_customer(
                    depot_locations[current_depot], unvisited_customers, customer_locations
                )
                if nearest_customer is not None:
                    current_route.append(nearest_customer)
                    unvisited_customers.remove(nearest_customer)
                    current_depot = nearest_customer
            current_route.append(driver)

        return routes

    # Example usage
    def find_route(self, depot_locations, customer_locations):
        depot_locations = [(0, 0), (10, 10)]
        customer_locations = [(1, 1), (2, 2), (4, 4), (6, 6), (8, 8)]
        routes = self.nearest_neighbor_mtsp(depot_locations, customer_locations)
