from api.models import Vehicle, Job


class MessageParser:
    """
    MessageParser class contains helper methods for route message.

    data :arg dictionary: raw message object
    """

    def __init__(self, data):
        self.vehicles = []
        self.jobs = []
        self.matrix = []
        self.data = data
        self.parse_data()

    def parse_data(self):
        """
        It's automatically executed when the class initialized for create Vehicle
        and Job instances and preprocessing in distance matrix.
        """
        vehicle_data = self.data.get('vehicles')
        for vehicle_datum in vehicle_data:
            self.vehicles.append(Vehicle(**vehicle_datum))

        job_data = self.data.get('jobs')
        for job_datum in job_data:
            self.jobs.append(Job(**job_datum))

        self.matrix = self.add_dummy_location_to_matrix(self.data.get('matrix'))

    @staticmethod
    def add_dummy_location_to_matrix(matrix):
        """
        Vehicles will not return to depot when their jobs is done. Therefore we need a zero cost
        location for route ending. This tricky approach is suggested on below or-tools documentation
        https://developers.google.com/optimization/routing/routing_tasks#allowing-arbitrary-start-and-end-locations
        :param matrix: list
        :return: matrix: list
        """
        matrix = [row + [0] for row in matrix]
        last_row = [0 for _ in range(len(matrix) + 1)]
        matrix.append(last_row)
        return matrix

    def get_vehicle_count(self):
        """
        Return total vehicle count
        """
        return len(self.vehicles)

    def get_location_count(self):
        """
        Return total location count
        """
        return len(self.matrix)

    def get_vehicle_start_index(self):
        """
        Return vehicles start location indexes
        """
        return [vehicle.start_index for vehicle in self.vehicles]

    def get_vehicle_end_index(self):
        """
        Return vehicles end location indexes
        """
        return [len(self.matrix) - 1 for i in range(len(self.vehicles))]

    def get_vehicle_capacities(self):
        """
        Return vehicle capacities
        """
        return [vehicle.total_capacity for vehicle in self.vehicles]

    @property
    def demand_list(self):
        """
        Return demand list
        """
        demand_list = [0 for _ in range(len(self.matrix))]
        for job in self.jobs:
            demand_list[job.location_index] = demand_list[job.location_index] + job.total_delivery
        return demand_list

    def get_job_ids_with_location_index(self, index):
        """
        Return job ids with target location index
        :param index: int
        :return job_ids: list
        """
        return [job.id for job in self.jobs if job.location_index == index]

    def get_total_service_time_with_location_index(self, index):
        """
        Return service time with target location index
        :param index:
        :return service_time: int
        """
        return sum([job.service for job in self.jobs if job.location_index == index])
