from exceptions import SolverException
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver.routing_enums_pb2 import FirstSolutionStrategy, LocalSearchMetaheuristic



class RouteSolver:
    """
    RouteSolver use google or-tools CVRP solving flow.
    Following documentation can be use as guide.
    https://developers.google.com/optimization/routing/cvrp

    :arg parser: MessageParser
    """

    def __init__(self, parser):
        self.parser = parser

    def create_manager(self):
        """
        Collects required arguments from parser class and create index manager for use whole class
        :return manager: RoutingIndexManager
        """
        location_count = self.parser.get_location_count()
        vehicle_count = self.parser.get_vehicle_count()
        start_index = self.parser.get_vehicle_start_index()
        end_index = self.parser.get_vehicle_end_index()

        manager = pywrapcp.RoutingIndexManager(location_count, vehicle_count, start_index, end_index)
        return manager

    def distance_callback(self, from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = self.manager.IndexToNode(from_index)
        to_node = self.manager.IndexToNode(to_index)
        travel_time = self.parser.matrix[from_node][to_node]
        service_time = self.parser.get_total_service_time_with_location_index(to_index)

        return travel_time + service_time

    def demand_callback(self, from_index):
        """Returns the demand of the node."""
        from_node = self.manager.IndexToNode(from_index)
        return self.parser.demand_list[from_node]

    @property
    def search_parameters(self):
        """
        Property method contains search_parameter for solution.
        :return search_parameter: DefaultRoutingSearchParameters
        """
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        search_parameters.local_search_metaheuristic = (LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
        search_parameters.time_limit.FromSeconds(1)
        return search_parameters

    def create_routing(self):
        """
        :return routing: RoutingModel
        """
        routing = pywrapcp.RoutingModel(self.manager)

        transit_callback_index = routing.RegisterTransitCallback(self.distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        demand_callback_index = routing.RegisterUnaryTransitCallback(self.demand_callback)
        routing.AddDimensionWithVehicleCapacity(
            demand_callback_index,
            0,
            self.parser.get_vehicle_capacities(),
            True,
            'Capacity')

        return routing

    def get_routes(self, solution):
        """
        :param solution: RoutingModel_SolveWithParameters
        :return: routes: dictionary
        """
        total_duration = 0
        routes = []
        for i, vehicle in enumerate(self.parser.vehicles):
            index = self.routing.Start(i)
            route_duration = 0
            job_ids = []
            while not self.routing.IsEnd(index):
                node_index = self.manager.IndexToNode(index)
                previous_index = index
                index = solution.Value(self.routing.NextVar(index))
                route_duration += self.routing.GetArcCostForVehicle(previous_index, index, i)
                job_ids = job_ids + self.parser.get_job_ids_with_location_index(node_index)
            total_duration += route_duration
            routes.append({
                "jobs": job_ids,
                "delivery_duration": route_duration
            })
        return {
            "total_delivery_duration": total_duration,
            "routes": routes
        }

    def solve(self):
        """
        This is only method for solve problem that needs to be call from the outside of class.
        If solution is not found, return detail message.
        :return routes: dictionary
        """
        self.manager = self.create_manager()
        self.routing = self.create_routing()
        solution = self.routing.SolveWithParameters(self.search_parameters)

        if solution:
            return self.get_routes(solution)
        else:
            raise SolverException("Solution not found!")
