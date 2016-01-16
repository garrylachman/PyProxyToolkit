
class Proxy:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.isValid = False

    @property
    def isValid(self):
        return self.__isValid

    @isValid.setter
    def isValid(self, value):
        self.__isValid = value