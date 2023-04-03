# classes used in communication between device clients, the cloud service, and the application client

class SensorMeasurement:

    def __init__(self, device_id):
        self.did = device_id
        self.temperature = None;

    def set_temperature(self, value):
        self.temperature = value

    def get_temperature(self):
        return self.temperature


    def to_json(self):
        pass

class ActuatorState:

    state: str

