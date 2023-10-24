class SensorLocations():
    def __init__(self):
        self.deployments = []

    def add(self,sensor, location):
        self.deployments.append((sensor,location))
    
    def findSensor(self, sensorID):
        for deployed in self.deployments:
            if deployed[0].ID == sensorID:
                return deployed[0]
    def findLocation(self,name):
        for deployed in self.deployments:
            if deployed[1].name == name:
                return deployed[1]
    def fromLocation(self,name):
        for deployed in self.deployments:
            if deployed[1].name == name:
                return deployed[0]