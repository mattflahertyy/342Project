from Objects.Measurement import Measurement


class Read():
    def __init__(self):
        self.measurements = []

    def add(self, sensor, temperature):
        self.measurements.append(Measurement(sensor, temperature))

    def findTemperature(self, sensorID):
        for measurement in self.measurements:
            if measurement.sensor.sensorID == sensorID:
                return measurement.temperature
    def pop(self,sensorID):
        for measurement in self.measurements:
            if measurement.sensor.sensorID == sensorID:
                self.measurements.remove(measurement)
                return measurement