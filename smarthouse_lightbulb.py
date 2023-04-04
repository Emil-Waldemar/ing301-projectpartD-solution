import logging
import threading
import time
import math

from messaging import ActuatorState


class Actuator:

    def __init__(self, did):
        self.did = did
        self.state = ActuatorState('False')

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while True:

            logging.info(f"Actuator {self.did}: {self.state.state}")

            time.sleep(1)

    def client(self):

        logging.info(f"Actuator Client {self.did} starting")

        while True:

            # TODO - read from cloud service

            logging.info(f"Actuator Client {self.did} {self.state.state}")
            time.sleep(4)

        logging.info(f"Client {self.did} finishing")

    def run(self):

        # start thread simulating physical light bulb
        sensor_thread = threading.Thread(target=self.simulator)
        sensor_thread.start()

        # start thread receiving state from the cloud
        client_thread = threading.Thread(target=self.client)
        client_thread.start()



