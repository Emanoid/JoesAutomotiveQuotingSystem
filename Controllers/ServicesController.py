from Models.Service import Service
from Views.ServiceView import ServiceView

class ServicesController:
    def __init__(self,baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    #Creates a new Service
    def createService(self, name, description, laborCost):
        serviceId = self.baseController.generateServiceId()
        parts = []
        newService = Service(serviceId, name, description, laborCost, parts)
        self.baseController.services[name] = newService
        return newService

    #Returns the a Service from a given Service Name
    def getService(self, name):
        if name in self.baseController.services:
            ServiceView(self.baseController.services[name]).display()
            return self.baseController.services[name]
        else: print("Service with name",name,"not found")
    
    #Returns a View of all Saved Services
    def getServices(self):
        for name in self.baseController.services:
            service = self.baseController.services[name]
            ServiceView(service).display()

    #Removes Service with given Service Name
    def removeService(self, name):
        self.baseController.services.pop(name)

    #Add Part to given Service
    def addPart(self, service, part):
        service.parts.append(part)

    #Removes given Part from given Service
    def removePart(self, service, part):
        service.parts.remove(part)
          




    




    


