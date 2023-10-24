from SensorLocations import SensorLocations
from SensorTemperatures import SensorTemperatures

class System():
    def __init__(self):
        self.locations = SensorLocations()
        self.temperatures = SensorTemperatures()
    
    def deploySensor(self, sensor, location, temperature):
        s = self.locations.findSensor(sensor.ID)
        l = self.locations.findLocation(location.name)
        if s!=None:
            print("Sensor " + sensor.ID + " already deployed")
            return
        if l!=None:
            print("Location " + location.name + " already covered")
            return None
        self.locations.add(sensor, location)
        self.temperatures.add(sensor, temperature)
        print("Sensor " + sensor.ID + " deployed at " + location.name+ ": ok")


    def readTemperature(self, name):
        
        l = self.locations.findLocation(name)
        if not l:
            print("Location " + name + " not covered")
            return
        sensor = self.locations.fromLocation(name)
        temperature = self.temperatures.findTemperature(sensor.ID) 
        print("Temperature at " + l.name + " is " + str(temperature)+ ": ok")
        return temperature
        





