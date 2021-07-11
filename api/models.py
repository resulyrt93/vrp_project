from dataclasses import dataclass


@dataclass
class Vehicle:
    """
    Vehicle class contain vehicle model data.
    """
    id: int
    start_index: int
    capacity: list

    @property
    def total_capacity(self):
        return self.capacity[0] if len(self.capacity) > 0 else 0


@dataclass
class Job:
    """
    Job class contain job model data
    """
    id: int
    location_index: int
    delivery: list
    service: int

    @property
    def total_delivery(self):
        return self.delivery[0] if len(self.delivery) > 0 else 0
