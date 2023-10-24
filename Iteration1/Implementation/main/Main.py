from Sensor import Sensor
from System import System
from Location import Location
import Registry
import random

def main():
    s = System()
    sensors = Registry.AVAILABLE_SENSORS
    cities = Registry.AVAILABLE_CITIES

    print("Deploying 10 sensors in random cities:\n")
    for i in range(10):
        newSensor = Sensor('sensor#'+ str(random.randint(0, len(sensors)+20)))
        index = random.randint(0, len(cities)-1)
        newLocation = Location(cities[index])
        if newSensor.ID:
            s.deploySensor(newSensor, newLocation, (random.randint(-35, 40)))
    
    print("\nReading all citites temperatures:\n")
    for c in cities:
        s.readTemperature(c)


if __name__ == "__main__":
    main()
