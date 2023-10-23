class SensorTemperatures():
    def __init__(self):
        self.measurements = []
    def add(self, sensor, temperature):
        self.measurements.append((sensor,temperature))
    def findTemperature(self,sensorID):
        for measurement in self.measurements:
            if measurement[0].ID == sensorID:
                return measurement[1]