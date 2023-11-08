from Sensor import Sensor
from System import System
from Location import Location
import Registry
import random
from visualizePlotly import see_map


def main():
    s = System()
    sensors = Registry.AVAILABLE_SENSORS
    cities = Registry.AVAILABLE_CITIES

    print("Available sensors:", end=" ")
    print(sensors, end="\n\n")

    print("Available locations:", end=" ")
    print(cities, end="\n\n")

    print("Deploying sensors to Chicago, New York, Fort Worth, Columbus and Phoenix")
    s.deploySensor(Sensor('sensor#0'), Location('Chicago'), (random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#1'), Location('New York'), (random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#2'), Location('Phoenix'), (random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#3'), Location('Fort Worth'), (random.randint(-40, 40)))
    s.deploySensor(Sensor('sensor#4'), Location('Columbus'), (random.randint(-40, 40)))

    print("Deploying sensors to Montreal (Montreal is not a valid location)")
    s.deploySensor(Sensor('sensor#5'), Location('Montreal'), (random.randint(-40, 40)))

    print("Redeploying sensor to Chicago (Chicago already has a sensor)")
    s.deploySensor(Sensor('sensor#6'), Location('Chicago'), (random.randint(-40, 40)))

    print("Deploying sensor to Los Angeles (sensor#0 is already taken)")
    s.deploySensor(Sensor('sensor#0'), Location('Los Angeles'), (random.randint(-40, 40)))

    print("Deploying sensor to Los Angeles (sensor#100 does not exist)")
    s.deploySensor(Sensor('sensor#100'), Location('Los Angeles'), (random.randint(-40, 40)))

    print("Reading temperature at Chicago")

    print("Reading sensor temperatures")
    see_map(s)

    print("Reading Location Montreal that dosen't have a sensor")
    s.readTemperature('Montreal')

    # print("Deploying 10 sensors in random cities:\n")
    # for i in range(10):
    #     newSensor = Sensor('sensor#'+ str(random.randint(0, len(sensors)+20)))
    #     index = random.randint(0, len(cities)-1)
    #     newLocation = Location(cities[index])
    #     if newSensor.ID:
    #         s.deploySensor(newSensor, newLocation, (random.randint(-40, 40)))

    # print("\nReading all citites temperatures:\n")
    # for c in cities:
    #     s.readTemperature(c)

    # # visualize_sensor_data(s.locations.deployments, s.temperatures)
    # see_map(s,["err init string", "err init sensor","err init string", "err init sensor","err init string", "err init sensor"])

    # # err1: deploying sensor to taken location
    # # err2: sensor already deployed
    # # err3: location dne
    # # err4: sensor dne


if __name__ == "__main__":
    main()