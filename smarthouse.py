# classes used in communication between device clients, the cloud service, and the application client

import logging

from smarthouse_temperature_sensor import Sensor
from smarthouse_lightbulb import Actuator

import common

log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt = "%H:%M:%S")

sensor = Sensor(common.TEMPERATURE_SENSOR_DID)
sensor.run()

actuator = Actuator(common.LIGHTBULB_DID)
actuator.run()

# https://realpython.com/intro-to-python-threading/