class Location():
    def __init__(self):
        pass

    def set_id(self, value):
        self.id = value

    def get_id(self):
        return self.id

    def set_dateCreated(self, value):
        self.dateCreated = value

    def get_dateCreated(self):
        return self.dateCreated

    def set_dateModified(self, value):
        self.dateModified = value

    def get_dateModified(self):
        return self.dateModified

    def set_preciseness(self, value):
        self.preciseness = value

    def get_preciseness(self):
        return self.preciseness

    def set_geo(self, value):
        if hasattr(value, 'latitude'):
            self.latitude = value.latitude

        if hasattr(value, 'longitude'):
            self.longitude = value.longitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def set_address(self, value):
        self.address = value

    def get_address(self):
        return self.address
