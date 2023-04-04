import logging
import threading
import time
import random
import math

# https://realpython.com/intro-to-python-threading/

TEMP_RANGE = 40


class SensorMeasurement:

    def __init__(self):
        self.temperature = None;

    def set_temperature(self, newvalue):
        self.temperature = newvalue

    def get_temperature(self):
        return self.temperature


    def to_json(self):
        pass


class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement()

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:

            temp = math.sin(time.time() / 10) * TEMP_RANGE

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(temp)

            time.sleep(2)

    def client(self):

        logging.info(f"Client {self.did} starting")

        while True:

            logging.info(f"Client {self.did} {self.measurement.get_temperature()}:")
            time.sleep(4)

        logging.info(f"Client {self.did} finishing")

    def run(self):

        # start thread simulating physical temperature sensor
        sensor_thread = threading.Thread(target=self.simulator)
        sensor_thread.start()

        # start thread sending temperature to the cloud
        client_thread = threading.Thread(target=self.client)
        client_thread.start()



