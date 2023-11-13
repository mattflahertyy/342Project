import Registries.LocationRegistry as LocationRegistry
import Registries.SensorRegistry as SensorRegistry
from Objects.Location import Location
from Objects.Read import Read
from Objects.Map import Map
from Objects.Sensor import Sensor
from Objects.LocationTemperature import LocationTemperature


class TempMonitor():
    def __init__(self):
        self.map = Map()
        self.read = Read()

    def deploySensor(self, sensor, location, temperature):
        if not location.name in LocationRegistry.AVAILABLE_CITIES:
            print(f"\033[91m    Location {location.name} does not exist\033[0m")
            return
        if not sensor.sensorID in SensorRegistry.AVAILABLE_SENSORS:
            print(f"\033[91m    Sensor {sensor.sensorID} does not exist\033[0m")
            return
        s = self.map.findSensorByID(sensor.sensorID)
        l = self.map.findLocationByName(location.name)
        if s is not None:
            print(f"\033[91m    Sensor {sensor.sensorID} already deployed\033[0m")
            return
        if l is not None:
            print(f"\033[91m    Location {location.name} already covered\033[0m")
            return None
        self.map.add(sensor, location)
        self.read.add(sensor, temperature)
        print(" Sensor " + sensor.sensorID + " deployed at " + location.name + ": ok")

    def readTemperature(self, name):
        l = self.map.findLocationByName(name)
        if not l:
            print(f"\033[91m    Location {name} not covered\033[0m")
            return
        sensor = self.map.fromLocation(name)
        temperature = self.read.findTemperature(sensor.sensorID).value
        print("Temperature at " + l.name + " is " + str(temperature) + ": ok")
        return temperature

    def replaceSensor(self, oldID, newID):
        #check if sensors exists
        if not oldID in SensorRegistry.AVAILABLE_SENSORS:
            print(f"\033[91m    Old Sensor {oldID} does not exist\033[0m")
            return
        if not newID in SensorRegistry.AVAILABLE_SENSORS:
            print(f"\033[91m    New Sensor {newID} does not exist\033[0m")
            return
        s1 = self.map.findSensorByID(oldID)
        if not s1:
            print(f"\033[91m    Old Sensor {oldID} not deployed\033[0m")
            return
        s2 = self.map.findSensorByID(newID)
        if s2:
            print(f"\033[91m    New Sensor {newID} already deployed\033[0m")
            return

        self.deploySensor(Sensor(newID), self.map.pop(oldID).location, self.read.pop(oldID).temperature)
        print("Sensor " + oldID + " replaced by " + newID + ": ok")

    def getAllLocationTemperatures(self):
        locationTemperature = []
        for deployment in self.map.deployments:
            t = self.read.findTemperature(deployment.sensor.sensorID)
            if t is None:
                print(f"\033[91m    Location {deployment.location.name} has no temperature\033[0m")
                continue

            locationTemperature.append(LocationTemperature(deployment.location, t))
        return locationTemperature

