from Models.Car import Car
from Views.CarView import CarView

class CarsController:
    def __init__(self, baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    #Creates a New Car
    def createCar(self, make, model, year):
        carId = self.baseController.generateCarId()
        newCar = Car(carId,make,model,year)
        self.baseController.cars[make+model+year] = newCar
        return newCar

    #Returns a View of all Saved Cars
    def getCars(self):
        for makeModelYear in self.baseController.cars:
            car = self.baseController.cars[makeModelYear]
            CarView(car).display()


    

