from Objects.Deployment import Deployment


class Map():
    def __init__(self):
        self.deployments = []

    def add(self, sensor, location):
        self.deployments.append(Deployment(sensor, location))

    def findSensorByID(self, sensorID):
        for deployed in self.deployments:
            if deployed.sensor.sensorID == sensorID:
                return deployed.sensor

    def findLocationByName(self, name):
        for deployed in self.deployments:
            if deployed.location.name == name:
                return deployed.location

    def findSensorByLocation(self, location):
        for deployed in self.deployments:
            if deployed.location == location:
                return deployed.sensor

    def findLocationBySensor(self, sensor):
        for deployed in self.deployments:
            if deployed.sensor == sensor:
                return deployed.location

    def fromLocation(self, name):
        for deployed in self.deployments:
            if deployed.location.name == name:
                return deployed.sensor

    def fromSensor(self, sensorID):
        for deployed in self.deployments:
            if deployed.sensor.sensorID == sensorID:
                return deployed.location

    def pop(self, sensorID):
        for deployed in self.deployments:
            if deployed.sensor.sensorID == sensorID:
                self.deployments.remove(deployed)
                return deployed
