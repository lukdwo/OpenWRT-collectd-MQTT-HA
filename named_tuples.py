from typing import NamedTuple


class Device(NamedTuple):
    identifiers: str
    name: str
    model: str
    manufacturer: str


class Sensor(NamedTuple):
    name: str
    unique_id: str
    topic: str


# Some topics report multiple values so IndexedSensor has an index field that can be used to identify which part of the topic belongs to the sensor. The load sensors are an example.
class IndexedSensor(NamedTuple):
    name: str
    unique_id: str
    topic: str
    index: int

