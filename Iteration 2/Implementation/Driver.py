import Registries.LocationRegistry as LocationRegistry
import Registries.SensorRegistry as SensorRegistry
import random
from System.Visualize import see_map, see_location_temperatures
from Objects.Sensor import Sensor
from Objects.Location import Location
from Objects.Temperature import Temperature
from System.TempMonitor import TempMonitor

def main():
    s = TempMonitor()
    while True:
        # Get user input
        print("1. View all locations")
        print("2. View all sensors")
        print("3. Deploy a sensor")
        print("4. Read a temperature")
        print("5. Replace a sensor")
        print("6. View all location temperatures")

        user_choice = int(input("Enter your option: "))

        if user_choice == 1:
            viewAllLocations()
        elif user_choice == 2:
            viewAllSensors()
        elif user_choice == 3:
            deployASensor(s)
            see_map(s)
        elif user_choice == 4:
            readATemperature(s)
        elif user_choice == 5:
            replaceASensor(s)
            see_map(s)
        elif user_choice == 6:
            viewAllLocationTemperatures(s)
            see_location_temperatures(s)
        else:
            default_option()

def default_option():
    print("Invalid option")

def viewAllLocations():
    cities = LocationRegistry.AVAILABLE_CITIES
    print("Available locations:", end=" ")
    print(cities, end="\n\n")

def viewAllSensors():
    sensors = SensorRegistry.AVAILABLE_SENSORS
    print("Available sensors:", end=" ")
    print(sensors, end="\n\n")

def deployASensor(s):
    sensorID = input("Enter a sensor ID: ")
    location = input("Enter a location: ")
    s.deploySensor(Sensor(sensorID), Location(location), Temperature(random.randint(-40, 40)))

def readATemperature(s):
    location = input("Enter a location: ")
    s.readTemperature(location)

def replaceASensor(s):
    oldSensorID = input("Enter the ID of the sensor to be replaced: ")
    newSensorID = input("Enter the ID of the new sensor: ")
    s.replaceSensor(oldSensorID, newSensorID)

def viewAllLocationTemperatures(s):
    for lt in s.getAllLocationTemperatures():
        print("temperature in " +lt.location.name + " is: " +str(lt.temperature.value)+ " °C")

if __name__ == "__main__":
    main()
