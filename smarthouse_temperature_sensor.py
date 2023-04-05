import logging
import threading
import time
import math
import requests

from messaging import SensorMeasurement

TEMP_RANGE = 40


class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:

            temp = round(math.sin(time.time() / 10) * TEMP_RANGE,1)

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(2)

    def client(self):

        logging.info(f"Sensor Client {self.did} starting")

        while True:

            logging.info(f"Sensor Client {self.did} {self.measurement.get_temperature()}")

            url = "http://localhost:8000/smarthouse/sensor/8/current"

            payload = self.measurement.to_json();

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            #print(response.text)

            time.sleep(4)

        logging.info(f"Client {self.did} finishing")

    def run(self):

        # start thread simulating physical temperature sensor
        sensor_thread = threading.Thread(target=self.simulator)
        sensor_thread.start()

        # start thread sending temperature to the cloud service
        client_thread = threading.Thread(target=self.client)
        client_thread.start()



