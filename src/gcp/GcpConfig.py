class GcpConfig:
    def __init__(self):
        self.__project_id = None
        self.__zone = None

    def get_project_id(self):
        return self.__project_id

    def set_project_id(self, val):
        self.__project_id = val

    def get_zone(self):
        return self.__zone

    def set_zone(self, val):
        self.__zone = val