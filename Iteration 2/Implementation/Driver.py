import Registries.LocationRegistry as LocationRegistry
import Registries.SensorRegistry as SensorRegistry
import random
from System.Visualize import see_map
from Objects.Sensor import Sensor
from Objects.Location import Location
from Objects.Temperature import Temperature
from System.TempMonitor import TempMonitor


def main():
    s = TempMonitor()
    sensors = SensorRegistry.AVAILABLE_SENSORS
    cities = LocationRegistry.AVAILABLE_CITIES

    print("Available sensors:", end=" ")
    print(sensors, end="\n\n")

    print("Available locations:", end=" ")
    print(cities, end="\n\n")

    print("Deploying sensors to Chicago, New York, Fort Worth, Columbus and Phoenix")
    s.deploySensor(Sensor('sensor#0'), Location('Chicago'), Temperature(random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#1'), Location('New York'), Temperature(random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#2'), Location('Phoenix'), Temperature(random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#3'), Location('Fort Worth'), Temperature(random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#4'), Location('Columbus'), Temperature(random.randint(-40, 40)))

    print("Deploying sensors to Montreal (Montreal is not a valid location)")
    s.deploySensor(Sensor('sensor#5'), Location('Montreal'), Temperature(random.randint(-40, 40)))

    print("Redeploying sensor to Chicago (Chicago already has a sensor)")
    s.deploySensor(Sensor('sensor#6'), Location('Chicago'), Temperature(random.randint(-40, 40)))

    print("Deploying sensor to Los Angeles (sensor#0 is already taken)")
    s.deploySensor(Sensor('sensor#0'), Location('Los Angeles'), Temperature(random.randint(-40, 40)))

    print("Deploying sensor to Los Angeles (sensor#100 does not exist)")
    s.deploySensor(Sensor('sensor#100'), Location('Los Angeles'), Temperature(random.randint(-40, 40)))

    print("Reading temperature at Chicago")

    print("Reading sensor temperatures")


    print("Reading Location Montreal that dosen't have a sensor")
    s.readTemperature('Montreal')
    print("Replacing sensor#0 with sensor#3, where the new sensor is already deployed")
    s.replaceSensor('sensor#0','sensor#3')
    print("Replacing sensor#0 with sensor#3, where the new sensor is not already deployed")
    s.replaceSensor('sensor#0', 'sensor#7')

    print("Reading all location temperatures")
    for lt in s.getAllLocationTemperatures():
        print("temperature in " +lt.location.name + " is: " +str(lt.temperature.value)+ " °C")

    see_map(s)
if __name__ == "__main__":
    main()
