from Models.Part import Part

class PartsController:
    def __init__(self,baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    def createPart(self, name, cost, laborCost, salesTax, carMakeModel):
        partId = self.baseController.generatePartId()
        totalCost = cost + laborCost + salesTax
        newPart = Part(partId, name, cost, laborCost, salesTax, totalCost, carMakeModel)
        self.baseController.parts.append(newPart)
        return newPart
    
    def removePart(self, part):
        if part in self.baseController.parts:
            self.baseController.parts.remove(part)
        else: print("Part",part.name,"not found")

    def removePartById(self, partId):
        for part in self.baseController.parts:
            if partId == part.id:
                self.baseController.parts.remove(part)
                return
        print("Part",part.name,"not found")


    




    


