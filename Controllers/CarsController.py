from Models.Car import Car
from Views.PartView import PartView

class CarsController:
    def __init__(self, baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    def createCar(self, make, model, year):
        carId = self.baseController.generateCarId()
        parts = []
        newCar = Car(carId,make,model,year,parts)
        self.baseController.cars.append(newCar)
        return newCar
    
    def removeCar(self, car):
        if car in self.baseController.cars:
            self.baseController.cars.remove(car)
        else: print("Car",car.make,car.model.car.year,"not found")

    def removeCarById(self, carId):
        for car in self.baseController.cars:
            if carId == car.id:
                self.baseController.cars.remove(car)
                return
        print("Car",car.make,car.model.car.year,"not found")                

    def addPart(self, car, part):
        car.parts.append(part)

    def addPartById(self, car, partId):
        for part in self.baseController.parts:
            if partId == part.id:
                car.parts.append(part)
                return
        print("Part",partId,"not found")

    def removePart(self, car, part):
        if part in self.baseController.parts:
            car.parts.remove(part)
        else: print("Part",part,"not found")

    def removePartById(self, car, partId):
        for part in self.baseController.parts:
            if partId == part.id:
                car.parts.remove(part)
                return
        print("Part",partId,"not found")

    def getParts(self, car):
        for part in car.parts:
            PartView(part).display()
        return car.parts
