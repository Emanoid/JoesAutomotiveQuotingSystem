from Models.Quote import Quote

class QuotesController:
    def __init__(self,baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    #Creates a New Quote
    def createQuote(self, customer):
        quoteId = self.baseController.generateQuoteId()
        services = []
        newQuote = Quote(quoteId, customer, services)
        self.baseController.quotes[customer.telephone] = newQuote
        return newQuote

    #Add a Service to a Quote
    def addService(self, quote, service):
        quote.services.append(service)

    #To get a Quote by customerTelephone
    def getQuote(self,customerTelephone):
        if customerTelephone in self.baseController.quotes:
            return self.baseController.quotes[customerTelephone]
        else: print("Quote with Customer Telephone",customerTelephone,"not found")

    #To return all Saved Quotes
    def getQuotes(self):
        return self.baseController.quotes.values()
    
    #To remove a Quote by customerTelephone
    def removeQuote(self, customerTelephone):
        if customerTelephone in self.baseController.quotes:
            self.baseController.quotes.pop(customerTelephone)
        else: print("Quote with Customer Telephone",customerTelephone,"not found")






    


