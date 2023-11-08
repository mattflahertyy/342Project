from SensorLocations import SensorLocations
from SensorTemperatures import SensorTemperatures
import Registry as registry


class System():
    def __init__(self):
        self.locations = SensorLocations()
        self.temperatures = SensorTemperatures()

    def deploySensor(self, sensor, location, temperature):
        if not location.name in registry.AVAILABLE_CITIES:
            print(f"\033[91m    Location {location.name} does not exist\033[0m")
            return
        if not sensor.ID in registry.AVAILABLE_SENSORS:
            print(f"\033[91m    Sensor {sensor.ID} does not exist\033[0m")
            return
        s = self.locations.findSensor(sensor.ID)
        l = self.locations.findLocation(location.name)
        if s != None:
            print(f"\033[91m    Sensor {sensor.ID} already deployed\033[0m")
            return
        if l != None:
            print(f"\033[91m    Location {location.name} already covered\033[0m")
            return None
        self.locations.add(sensor, location)
        self.temperatures.add(sensor, temperature)
        print(" Sensor " + sensor.ID + " deployed at " + location.name + ": ok")

    def readTemperature(self, locationName):
        l = self.locations.findLocation(locationName)
        if not l:
            print(f"\033[91m    Location {locationName} not covered\033[0m")
            return
        sensor = self.locations.fromLocation(locationName)
        temperature = self.temperatures.findTemperature(sensor.ID)
        print("Temperature at " + l.name + " is " + str(temperature) + ": ok")
        return temperature
