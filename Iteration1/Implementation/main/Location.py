import Registry

class Location():
    def __init__(self, name):
        if name in Registry.AVAILABLE_CITIES:
            self.name = name
        else:
            print("Location does not exist")
