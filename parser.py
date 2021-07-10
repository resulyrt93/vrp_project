from dataclasses import dataclass


class MessageValidator:
    validated = False
    message_content = ["vehicles", "jobs", "matrix"]

    def __init__(self, data):
        self.raw_data = data

    def validate(self):
        for content in self.message_content:
            content_value = self.raw_data.get(content)
            if content_value is None:
                raise Exception("Message should contain {0} key!".format(content))
            if not isinstance(content_value, list):
                raise Exception("{0} should be a list instance!".format(content))
        self.validated = True
        return True

    def get_parser(self):
        if self.validated:
            return MessageParser(data=self.raw_data)
        else:
            raise Exception("Message not validated. Use .validate() method for validation.")


@dataclass
class Vehicle:
    id: int
    start_index: int
    capacity: list

    @property
    def total_capacity(self):
        return self.capacity[0] if len(self.capacity) > 0 else 0


@dataclass
class Job:
    id: int
    location_index: int
    delivery: list
    service: int

    @property
    def total_delivery(self):
        return self.delivery[0] if len(self.delivery) > 0 else 0


class MessageParser:

    def __init__(self, data):
        self.vehicles = []
        self.jobs = []
        self.matrix = []
        self.data = data
        self.parse_data()

    def parse_data(self):
        vehicle_data = self.data.get('vehicles')
        for vehicle_datum in vehicle_data:
            self.vehicles.append(Vehicle(**vehicle_datum))

        job_data = self.data.get('jobs')
        for job_datum in job_data:
            self.jobs.append(Job(**job_datum))

        self.matrix = self.add_dummy_location_to_matrix(self.data.get('matrix'))

    @staticmethod
    def add_dummy_location_to_matrix(matrix):
        matrix = [row + [0] for row in matrix]
        last_row = [0 for _ in range(len(matrix) + 1)]
        matrix.append(last_row)
        return matrix

    def get_vehicle_count(self):
        return len(self.vehicles)

    def get_capacity_list(self):
        return [vehicle.total_capacity for vehicle in self.vehicles]

    def get_start_index_list(self):
        return [vehicle.start_index for vehicle in self.vehicles]

    def get_location_count(self):
        return len(self.matrix)

    def get_vehicle_start_index(self):
        return [vehicle.start_index for vehicle in self.vehicles]

    def get_vehicle_end_index(self):
        return [len(self.matrix) - 1 for i in range(len(self.vehicles))]

    def get_vehicle_capacities(self):
        return [vehicle.total_capacity for vehicle in self.vehicles]

    @property
    def demand_list(self):
        demand_list = [0 for _ in range(len(self.matrix))]
        for job in self.jobs:
            demand_list[job.location_index] = demand_list[job.location_index] + job.total_delivery
        return demand_list

    def get_job_ids_with_location_index(self, index):
        return [job.id for job in self.jobs if job.location_index == index]
