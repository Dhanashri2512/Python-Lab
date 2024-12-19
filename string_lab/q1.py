#Q1)WAP TO GET EMPLOYEE INFORMATION TO STORE HIS OFFICIAL INFORMATION(eid,designation)
class Employee:
    # Constructor to initialize class variables
    def __init__(self, name, eid):

        # Corrected 'id' to 'eid' to avoid conflict with built-in id function
        self.name = name
        self.eid = eid

    def showDetails(self):
        # Fixed the print statement for clarity and corrected 'i' to 'is'
        print(f"The name of the employee is {self.name} with Employee ID: {self.eid}")

# Creating an object of the Employee class
obj = Employee("Mohan", 40)
obj.showDetails()
