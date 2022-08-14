from src.ErrorSource import ErrorSource

class ErrorResponse():
    def __init__(self):
        self.status = None
        self.title = None
        self.detail = None
        self.source = ErrorSource()

    def set_status(self, val):
        self.status = val

    def get_status(self):
        return self.status
    
    def set_title(self, val):
        self.title = val

    def get_title(self):
        return self.title

    def set_detail(self, val):
        self.detail = val

    def get_detail(self):
        return self.detail

    def set_source_pointer(self, val):
        self.source.set_pointer(val)

    def get_source(self):
        return self.source