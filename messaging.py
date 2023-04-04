import json


class SensorMeasurement:

    def __init__(self, init_value):
        self.value = init_value;

    def set_temperature(self, new_value):
        self.value = new_value

    def get_temperature(self):
        return self.value

    def to_json(self):
        sensor_measurement_encoded = json.dumps(self.__dict__)
        return sensor_measurement_encoded


class ActuatorState:

    def __init__(self, init_state):
        self.state = init_state

    @staticmethod
    def json_decoder(json_actuator_state_dict):
        return ActuatorState(json_actuator_state_dict['state'])

    @staticmethod
    def from_json(json_gps_point_str: str):

        json_actuator_state_dict = json.loads(json_gps_point_str)
        actuator_state = ActuatorState.json_decoder(json_actuator_state_dict)

        return actuator_state
