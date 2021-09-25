from Views.PartView import PartView


class ServiceView:
    def __init__(self, service):
        self.service = service

    def display(self):
        print("Service Information:")
        print("ID:",self.service.id)
        print("Name:",self.service.name)
        print("Description:",self.service.description)
        print("Labor Charge: $",self.service.laborCost)
        for part in self.service.parts:
            PartView(part).display()
        print("--------------------------------")


