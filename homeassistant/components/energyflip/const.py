"""Constants for the EnergyFlip integration."""
from energyflip.const import (
    SOURCE_TYPE_ELECTRICITY,
    SOURCE_TYPE_ELECTRICITY_IN,
    SOURCE_TYPE_ELECTRICITY_IN_LOW,
    SOURCE_TYPE_ELECTRICITY_OUT,
    SOURCE_TYPE_ELECTRICITY_OUT_LOW,
    SOURCE_TYPE_GAS,
)

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import ENERGY_KILO_WATT_HOUR, TIME_HOURS, VOLUME_CUBIC_METERS

DATA_COORDINATOR = "coordinator"

DOMAIN = "energyflip"

FLOW_CUBIC_METERS_PER_HOUR = f"{VOLUME_CUBIC_METERS}/{TIME_HOURS}"

"""Interval in seconds between polls to energyFlip."""
POLLING_INTERVAL = 20

"""Timeout for fetching sensor data"""
FETCH_TIMEOUT = 10

SENSOR_TYPE_RATE = "rate"
SENSOR_TYPE_THIS_DAY = "thisDay"
SENSOR_TYPE_THIS_WEEK = "thisWeek"
SENSOR_TYPE_THIS_MONTH = "thisMonth"
SENSOR_TYPE_THIS_YEAR = "thisYear"

SOURCE_TYPES = [
    SOURCE_TYPE_ELECTRICITY,
    SOURCE_TYPE_ELECTRICITY_IN,
    SOURCE_TYPE_ELECTRICITY_IN_LOW,
    SOURCE_TYPE_ELECTRICITY_OUT,
    SOURCE_TYPE_ELECTRICITY_OUT_LOW,
    SOURCE_TYPE_GAS,
]

SENSORS_INFO = [
    {
        "name": "EnergyFlip Current Power",
        "device_class": SensorDeviceClass.POWER,
        "source_type": SOURCE_TYPE_ELECTRICITY,
    },
    {
        "name": "EnergyFlip Current Power In Peak",
        "device_class": SensorDeviceClass.POWER,
        "source_type": SOURCE_TYPE_ELECTRICITY_IN,
    },
    {
        "name": "EnergyFlip Current Power In Off Peak",
        "device_class": SensorDeviceClass.POWER,
        "source_type": SOURCE_TYPE_ELECTRICITY_IN_LOW,
    },
    {
        "name": "EnergyFlip Current Power Out Peak",
        "device_class": SensorDeviceClass.POWER,
        "source_type": SOURCE_TYPE_ELECTRICITY_OUT,
    },
    {
        "name": "EnergyFlip Current Power Out Off Peak",
        "device_class": SensorDeviceClass.POWER,
        "source_type": SOURCE_TYPE_ELECTRICITY_OUT_LOW,
    },
    {
        "name": "EnergyFlip Energy Consumption Peak Today",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY_IN,
        "sensor_type": SENSOR_TYPE_THIS_DAY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "precision": 3,
    },
    {
        "name": "EnergyFlip Energy Consumption Off Peak Today",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY_IN_LOW,
        "sensor_type": SENSOR_TYPE_THIS_DAY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "precision": 3,
    },
    {
        "name": "EnergyFlip Energy Production Peak Today",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY_OUT,
        "sensor_type": SENSOR_TYPE_THIS_DAY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "precision": 3,
    },
    {
        "name": "EnergyFlip Energy Production Off Peak Today",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY_OUT_LOW,
        "sensor_type": SENSOR_TYPE_THIS_DAY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "precision": 3,
    },
    {
        "name": "EnergyFlip Energy Today",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY,
        "sensor_type": SENSOR_TYPE_THIS_DAY,
        "precision": 1,
    },
    {
        "name": "EnergyFlip Energy This Week",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY,
        "sensor_type": SENSOR_TYPE_THIS_WEEK,
        "precision": 1,
    },
    {
        "name": "EnergyFlip Energy This Month",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY,
        "sensor_type": SENSOR_TYPE_THIS_MONTH,
        "precision": 1,
    },
    {
        "name": "EnergyFlip Energy This Year",
        "device_class": SensorDeviceClass.ENERGY,
        "unit_of_measurement": ENERGY_KILO_WATT_HOUR,
        "source_type": SOURCE_TYPE_ELECTRICITY,
        "sensor_type": SENSOR_TYPE_THIS_YEAR,
        "precision": 1,
    },
    {
        "name": "EnergyFlip Current Gas",
        "unit_of_measurement": FLOW_CUBIC_METERS_PER_HOUR,
        "source_type": SOURCE_TYPE_GAS,
        "icon": "mdi:fire",
        "precision": 1,
    },
    {
        "name": "EnergyFlip Gas Today",
        "device_class": SensorDeviceClass.GAS,
        "unit_of_measurement": VOLUME_CUBIC_METERS,
        "source_type": SOURCE_TYPE_GAS,
        "sensor_type": SENSOR_TYPE_THIS_DAY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:counter",
        "precision": 1,
    },
    {
        "name": "EnergyFlip Gas This Week",
        "device_class": SensorDeviceClass.GAS,
        "unit_of_measurement": VOLUME_CUBIC_METERS,
        "source_type": SOURCE_TYPE_GAS,
        "sensor_type": SENSOR_TYPE_THIS_WEEK,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:counter",
        "precision": 1,
    },
    {
        "name": "EnergyFlip Gas This Month",
        "device_class": SensorDeviceClass.GAS,
        "unit_of_measurement": VOLUME_CUBIC_METERS,
        "source_type": SOURCE_TYPE_GAS,
        "sensor_type": SENSOR_TYPE_THIS_MONTH,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:counter",
        "precision": 1,
    },
    {
        "name": "EnergyFlip Gas This Year",
        "device_class": SensorDeviceClass.GAS,
        "unit_of_measurement": VOLUME_CUBIC_METERS,
        "source_type": SOURCE_TYPE_GAS,
        "sensor_type": SENSOR_TYPE_THIS_YEAR,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "icon": "mdi:counter",
        "precision": 1,
    },
]
