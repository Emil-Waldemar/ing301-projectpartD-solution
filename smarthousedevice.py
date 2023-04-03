import logging
import threading
import time
import random

from messaging import SensorMeasurement

# https://realpython.com/intro-to-python-threading/


def sensor(measurement: SensorMeasurement):

    logging.info("Sensor starting")

    while True:

        temp = float(random.randint(-20, 20))

        logging.info(f"Sensor: {temp}")
        measurement.set_temperature(temp)

        time.sleep(2)


def client(measurement: SensorMeasurement):

    logging.info("Client starting")

    while True:

        logging.info(f"Client {measurement.get_temperature()}:")
        time.sleep(4)

    print("Client finishing")


if __name__ == '__main__':

    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt = "%H:%M:%S")

    measurement = SensorMeasurement(1)

    # start threads corresponding to physical device similator
    sensor_thread = threading.Thread(target=sensor, args=(measurement,))
    client_thread = threading.Thread(target=client, args=(measurement,))

    sensor_thread.start()
    client_thread.start()



