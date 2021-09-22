class BaseController:
    def __init__(self,path):
        self.path = path
        self.partId = 1
        self.carId = 1
        self.quoteId = 1
        self.userId = 1
        self.users = []
        self.parts = []
        self.cars = []
        self.quotes = []

    def generatePartId(self):
        res = self.partId
        self.partId += 1
        return res

    def generateCarId(self):
        res = self.carId
        self.carId += 1
        return res

    def generateQuoteId(self):
        res = self.quoteId
        self.quoteId += 1
        return res

    def generateUserId(self):
        res = self.userId
        self.userId += 1
        return res



