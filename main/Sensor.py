import Registry


class Sensor():
    def __init__(self, ID):
        if (ID in Registry.AVAILABLE_SENSORS):
            self.ID = ID
        else:
            self.ID = None
            print("Sensor: " + ID+" does not exist")
