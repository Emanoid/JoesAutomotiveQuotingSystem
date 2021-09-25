from Models.Part import Part
from Views.PartView import PartView

class PartsController:
    def __init__(self,baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    #Creates a new Part
    def createPart(self, name, mainSupplierName, cost):
        partId = self.baseController.generatePartId()
        newPart = Part(partId, name, mainSupplierName, cost)
        self.baseController.parts[name+mainSupplierName] = newPart
        return newPart

    #Returns the Cost of a given Part
    def getPartCost(self, name, mainSupplierName):
        if name+mainSupplierName in self.baseController.parts:
            print(self.baseController.parts[name+mainSupplierName].cost)
            return self.baseController.parts[name+mainSupplierName].cost
        else: print("Part with name",name,"and Main-Supplier",mainSupplierName,"not found")
    
    #Returns a View of all Saved Parts
    def getParts(self):
        for nameMainSupplierName in self.baseController.parts:
            part = self.baseController.parts[nameMainSupplierName]
            PartView(part).display()

    #Removes given Part from Saved Parts
    def removePart(self, name, mainSupplierName):
        if name+mainSupplierName in self.baseController.parts:
            self.baseController.parts.pop(name+mainSupplierName)
        else: print("Part,",name,"with Main Supplier,",mainSupplierName,"not Found")
          




    




    


