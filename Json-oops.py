import json


class Employee:
    def __init__(self,Name, Id, Salary):
        self.Name = Name
        self.Id = Id
        self.Salary = Salary

    def print_info(self):
        print("Name:", self.Name)
        print("ID:",self.Id)
        print("Salary:",self.Salary)

   # if salary increese to the person

    def increment_Salary(self, increment):
        self.Salary += increment


    # if salary to decrese
    def decrement_Salary(self, decrement):
        self.Salary -= decrement

    def save_to_json(self, filename):
        employee_dict = {'Name': self.Name, 'id': self.Id, 'Salary':self.Salary}
        with open(filename, 'w') as f:
            f.write(json.dumps(employee_dict, indent =4))

    def load_to_json( self, filename):
        with open(filename, 'r') as f:
            data = json.load(f.read())

             ## To modify data/ values

            self.name = data['Name']
            self.Id = data['Id']
            self.Salary = ['data[Salary']
            f.read()


## 'e-series' is object for class 'Employee'
e1 = Employee('Akhil',12312,300000)
e2 = Employee('sai',32112,340000)
e1.print_info()
e2.print_info()



# Saving the values in-to a file name- "Data-Oops.Json"


# 'e_'.save_to_json('Data-Oops.json')
e2.save_to_json('Data-Oops.json')

## reducing the salary

e2.decrement_Salary(1000)
e2.print_info() # to print in terminal
e2.save_to_json('Data-Oops.json') # to save changes in file


# Increasing the salary for e1 object

e1.increment_Salary(2300)
e1.print_info()

# to save changes for e1 object
e1.save_to_json('Data-Oops.json')