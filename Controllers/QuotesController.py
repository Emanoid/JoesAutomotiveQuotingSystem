from Models.Quote import Quote

class QuotesController:
    def __init__(self,baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)  

    def createQuote(self, customer):
        quoteId = self.baseController.generateQuoteId()
        newQuote = Quote(quoteId, customer)
        self.baseController.quotes.append(newQuote)
        return newQuote
    
    def removeQuote(self, quote):
        if quote in self.baseController.quotes:
            self.baseController.quotes.remove(quote)
        else: print("Quote",quote.id,"not found")

    def removeQuoteById(self, quoteId):
        for quote in self.baseController.quotes:
            if quoteId == quote.id:
                self.baseController.quotes.remove(quote)
                return
        print("Quote",quote.id,"not found")





    


