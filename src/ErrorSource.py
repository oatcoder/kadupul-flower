class ErrorSource:
    def __init__(self):
        self.pointer = None

    def set_pointer(self, val):
        self.pointer = val
    
    def get_popinter(self):
        return self.pointer