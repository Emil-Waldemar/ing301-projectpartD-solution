from pydantic import BaseModel


class Device (BaseModel):

    did : int
    serial_no: str
    producer: str
    product_type: str
    nickname: str


class SensorMeasurement(BaseModel):

    value: str

class Sensor(Device):

    def is_sensor(self):
        return True

    def is_actuator(self):
        return False

    @abc.abstractmethod
    def get_current_value(self):
        pass

    @abc.abstractmethod
    def set_current_value(self, value: float):
        pass

    @abc.abstractmethod
    def get_current_values(self):
        pass

    @abc.abstractmethod
    def delete_oldest_value(self):
        pass



class TemperatureSensor(Sensor):

    temperature: list[float] | None = list()
    unit: str | None = "°C"

    def get_current_value(self) -> Optional[float]:
        return self.temperature[0]

    def get_current_values(self):
        return self.temperature

    def set_current_value(self, temperature: float):
        self.temperature.insert(0, temperature)

    def delete_oldest_value(self):
        self.temperature.pop()


class HumiditySensor(Sensor):

    humidity: list[float] | None = list()
    unit: str | None = "%"

    def get_current_value(self) -> Optional[float]:
        return self.humidity[0]

    def get_current_values(self):
        return self.humidity

    def set_current_value(self, humidity: float):
        self.humidity.insert(0, humidity)

    def delete_oldest_value(self):
        self.humidity.pop()