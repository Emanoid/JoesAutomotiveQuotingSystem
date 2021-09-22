import os

class QuoteView:
    def __init__(self, quote):
        self.quote = quote

    def display(self):
        print("------------------------JOES AUTOMOTIVE QUOTE------------------------")
        print("Quote Information")
        print("Quote ID: ",self.quote.id)
        print("Customer Name: ",self.quote.customer.fullName)
        print("Customer Address: ",self.quote.customer.address)
        print("------------------------QUOTE------------------------")
        SalesTax = 0
        LaborCost = 0
        PartCost = 0 
        TotalCost = 0
        for car in self.quote.customer.cars:
            print("Car ID:",car.id)  
            print("Car Make:",car.make)   
            print("Car Model:",car.model)
            print("Car Year:",car.year)             
            salesTax = 0
            laborCost = 0
            partCost = 0 
            totalCost = 0
            print("Car Parts for Car ID:",car.id,":")
            for part in car.parts:
                print("________________________________")
                print("Part Name:",part.name)
                print("Part Cost: $",part.cost)                
                salesTax = salesTax + part.salesTax
                partCost = partCost + part.cost
                laborCost = laborCost + part.laborCost                
                totalCost = totalCost + part.totalCost
            print("------TOTAL FOR CAR ID",car.id,"-------")
            print("Total Estimated Part(s) Cost: $",partCost)
            print("Total Estimated Labor Cost: $",laborCost)
            print("Total Estimated Sales Tax: $",salesTax)
            print("Total Estimated Charges: $",totalCost)
            SalesTax = SalesTax + salesTax
            LaborCost = LaborCost + laborCost
            PartCost = PartCost + partCost
            TotalCost = TotalCost + totalCost
            print("****************************************************")
        print()         
        print("------TOTAL FOR ALL CARS-------")
        print("Total Estimated Part(s) Cost: $",PartCost)
        print("Total Estimated Labor Cost: $",LaborCost)
        print("Total Estimated Sales Tax: $",SalesTax)
        print("Total Estimated Charges: $",TotalCost)
        print("------------------------QUOTE END------------------------")
        print()

    def print(self):
        with open("Quote"+str(self.quote.id)+"For"+self.quote.customer.fullName+".txt", 'w') as f:
            f.write("------------------------JOES AUTOMOTIVE QUOTE------------------------")
            f.write('\n')
            f.write("Quote Information"); f.write('\n')
            f.write("Quote ID: "+str(self.quote.id)); f.write('\n')
            f.write("Customer Name: "+self.quote.customer.fullName); f.write('\n')
            f.write("Customer Address: "+self.quote.customer.address); f.write('\n')
            f.write("------------------------QUOTE------------------------"); f.write('\n')
            SalesTax = 0
            LaborCost = 0
            PartCost = 0 
            TotalCost = 0
            for car in self.quote.customer.cars:
                f.write("Car ID: "+str(car.id)); f.write('\n')  
                f.write("Car Make: "+car.make); f.write('\n')   
                f.write("Car Model: "+car.model); f.write('\n')
                f.write("Car Year: "+car.year); f.write('\n')             
                salesTax = 0
                laborCost = 0
                partCost = 0 
                totalCost = 0
                f.write("Car Parts for Car ID:"+str(car.id)+":"); f.write('\n')
                for part in car.parts:
                    f.write("________________________________"); f.write('\n')
                    f.write("Part Name: "+part.name); f.write('\n')
                    f.write("Part Cost: $"+str(part.cost)); f.write('\n')                
                    salesTax = salesTax + part.salesTax
                    partCost = partCost + part.cost
                    laborCost = laborCost + part.laborCost                
                    totalCost = totalCost + part.totalCost
                f.write("------TOTAL FOR CAR ID "+str(car.id)+"-------"); f.write('\n')
                f.write("Total Estimated Part(s) Cost: $"+str(partCost)); f.write('\n')
                f.write("Total Estimated Labor Cost: $"+str(laborCost)); f.write('\n')
                f.write("Total Estimated Sales Tax: $"+str(salesTax)); f.write('\n')
                f.write("Total Estimated Charges: $"+str(totalCost)); f.write('\n')
                SalesTax = SalesTax + salesTax
                LaborCost = LaborCost + laborCost
                PartCost = PartCost + partCost
                TotalCost = TotalCost + totalCost
                f.write("****************************************************"); f.write('\n')
            f.write('\n')     
            f.write("------TOTAL FOR ALL CARS-------"); f.write('\n')
            f.write("Total Estimated Part(s) Cost: $"+str(PartCost)); f.write('\n')
            f.write("Total Estimated Labor Cost: $"+str(LaborCost)); f.write('\n')
            f.write("Total Estimated Sales Tax: $"+str(SalesTax)); f.write('\n')
            f.write("Total Estimated Charges: $"+str(TotalCost)); f.write('\n')
            f.write("------------------------QUOTE END------------------------"); f.write('\n')
        os.system("Quote"+str(self.quote.id)+"For"+self.quote.customer.fullName+".txt")



            

