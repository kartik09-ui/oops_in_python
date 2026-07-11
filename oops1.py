class employee:

    def __init_(self):
        print("Started executing attribute/data")
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'

    def travel(self, destination):
        print("this travel method was called manually")
        print("Employee is now travelling to {destination}")


sam = employee()
sam.travel("Kerela")