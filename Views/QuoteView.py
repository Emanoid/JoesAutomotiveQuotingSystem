import os

class QuoteView:
    def __init__(self, quote):
        self.quote = quote

    def display(self):
        print("------------------------JOES AUTOMOTIVE QUOTE------------------------")
        print("Quote ID: ",self.quote.id)
        print("Customer Information-----------------------------")
        print("Customer Name: ",self.quote.customer.fullName)
        print("Customer Phone Number: ",self.quote.customer.telephone)
        print("Quote Information---------------------------------------------------")
        PartCost = 0 
        LaborCost = 0
        TotalCost = 0
        for car in self.quote.customer.cars:
            print("For Car ID:",car.id,"-------------------------------")
            print("Car Make:",car.make)   
            print("Car Model:",car.model)  
            print("Car Year:",car.year)        
            partCost = 0 
            laborCost = 0  
            totalCost = 0
            for service in self.quote.services:
                print("For Service ID:",service.id,"-------")
                print("Service Name:",service.name)
                print("Parts:------------------")
                prtCost = 0
                for part in service.parts:
                    print("Part Name:",part.name)
                    print("Part Charge: $",part.cost)
                    print("_________")
                    prtCost = prtCost + part.cost
                partCost = partCost + prtCost
                laborCost = laborCost + service.laborCost                
                totalCost = totalCost + partCost + laborCost
            print("Total Charges for CAR ID:",car.id,"---")
            print("Total Estimated Part(s) Cost: $",partCost)
            print("Total Estimated Labor Cost: $",laborCost)
            print("Total Estimated Charges: $",totalCost)
            LaborCost = LaborCost + laborCost
            PartCost = PartCost + partCost
            TotalCost = TotalCost + totalCost
        print()         
        print("------TOTAL FOR ALL CARS-------")
        print("Total Estimated Part(s) Cost: $",PartCost)
        print("Total Estimated Labor Cost: $",LaborCost)
        print("Total Estimated Charges: $",TotalCost)
        print("------------------------QUOTE END------------------------")
        print()

    def displayAll(self):
        print("------------------------JOES AUTOMOTIVE QUOTE------------------------")
        print("Quote ID: ",self.quote.id)
        print("Customer Information-----------------------------")
        print("Customer Name: ",self.quote.customer.fullName)
        print("Customer Phone Number: ",self.quote.customer.telephone)
        print("Customer Address: ",self.quote.customer.address)
        print("Quote Information---------------------------------------------------")
        PartCost = 0 
        LaborCost = 0
        SalesTax = 0       
        TotalCost = 0
        for car in self.quote.customer.cars:
            print("For Car ID:",car.id,"-------------------------------")
            print("Car Make:",car.make)   
            print("Car Model:",car.model)        
            partCost = 0 
            laborCost = 0
            salesTax = 0       
            totalCost = 0
            for service in self.quote.services:
                print("For Service ID:",service.id,"-------")
                print("Service Name:",service.name)
                print("Parts:------------------")
                prtCost = 0
                for part in service.parts:
                    print("Part Name:",part.name)
                    print("Part Charge: $",part.cost)
                    print("_________")
                    prtCost = prtCost + part.cost
                partCost = partCost + prtCost
                salesTax = salesTax + (prtCost * 0.05) #5% of the Part Cost
                laborCost = laborCost + service.laborCost                
                totalCost = totalCost + salesTax + partCost + laborCost
            print("Total Charges for CAR ID:",car.id,"---")
            print("Total Part(s) Cost: $",partCost)
            print("Total Labor Cost: $",laborCost)
            print("Total Sales Tax: $",salesTax)
            print("Total Charges: $",totalCost)
            SalesTax = SalesTax + salesTax
            LaborCost = LaborCost + laborCost
            PartCost = PartCost + partCost
            TotalCost = TotalCost + totalCost
        print()         
        print("------TOTAL FOR ALL CARS-------")
        print("Total Part(s) Cost: $",PartCost)
        print("Total Labor Cost: $",LaborCost)
        print("Total Sales Tax: $",SalesTax)
        print("Total Charges: $",TotalCost)
        print("------------------------QUOTE END------------------------")
        print()

    def print(self):
        with open("Quote"+str(self.quote.id)+"For"+self.quote.customer.firstName+".txt", 'w') as f:
            f.write("------------------------JOES AUTOMOTIVE QUOTE------------------------"); f.write('\n')
            f.write("Quote ID: "+str(self.quote.id)); f.write('\n')
            f.write("Customer Information-----------------------------"); f.write('\n')
            f.write("Customer Name: "+self.quote.customer.fullName); f.write('\n')
            f.write("Customer Phone Number: "+self.quote.customer.telephone); f.write('\n')
            f.write("Customer Address: "+self.quote.customer.address); f.write('\n')
            f.write("Quote Information---------------------------------------------------"); f.write('\n')
            PartCost = 0 
            LaborCost = 0
            SalesTax = 0       
            TotalCost = 0
            for car in self.quote.customer.cars:
                f.write("For Car ID:"+str(car.id)+"-------------------------------"); f.write('\n')
                f.write("Car Make:"+car.make); f.write('\n')
                f.write("Car Model:"+car.model); f.write('\n')        
                partCost = 0 
                laborCost = 0
                salesTax = 0       
                totalCost = 0
                for service in self.quote.services:
                    f.write("For Service ID:"+str(service.id)+"-------"); f.write('\n')
                    f.write("Service Name:"+service.name); f.write('\n')
                    f.write("Parts:------------------"); f.write('\n')
                    prtCost = 0
                    for part in service.parts:
                        f.write("Part Name:"+part.name); f.write('\n')
                        f.write("Part Charge: $"+str(part.cost)); f.write('\n')
                        f.write("_________"); f.write('\n')
                        prtCost = prtCost + part.cost
                    partCost = partCost + prtCost
                    salesTax = salesTax + (prtCost * 0.05) #5% of the Part Cost
                    laborCost = laborCost + service.laborCost                
                    totalCost = totalCost + salesTax + partCost + laborCost
                f.write("Total Charges for CAR ID:"+str(car.id)+"---"); f.write('\n')
                f.write("Total Part(s) Cost: $"+str(partCost)); f.write('\n')
                f.write("Total Labor Cost: $"+str(laborCost)); f.write('\n')
                f.write("Total Sales Tax: $"+str(salesTax)); f.write('\n')
                f.write("Total Charges: $"+str(totalCost)); f.write('\n')
                SalesTax = SalesTax + salesTax
                LaborCost = LaborCost + laborCost
                PartCost = PartCost + partCost
                TotalCost = TotalCost + totalCost
            f.write('\n')        
            f.write("------TOTAL FOR ALL CARS-------"); f.write('\n')
            f.write("Total Part(s) Cost: $"+str(PartCost)); f.write('\n')
            f.write("Total Labor Cost: $"+str(LaborCost)); f.write('\n')
            f.write("Total Sales Tax: $"+str(SalesTax)); f.write('\n')
            f.write("Total Charges: $"+str(TotalCost)); f.write('\n')
            f.write("------------------------QUOTE END------------------------"); f.write('\n')
            f.write('\n')
        os.system("Quote"+str(self.quote.id)+"For"+self.quote.customer.firstName+".txt")



            

