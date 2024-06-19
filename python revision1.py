# 1 The Patient class should have attributes for name, age, and condition. It should include methods to admit a patient and discharge them.

class Patient:
    def __init__(self,name,age,conditions):
        self.name = name
        self.age = age
        self.conditions = conditions
        self.total_bill=0
    def admit_patient(self):
        print("patient has admitted")
        self.total_bill=5000
    def discharge(self):
        print("patient has discharge")
        print(f"your total bill is {self.total_bill}")

    
class Radiological_Tests(Patient):
    def __init__(self,type_of_test):
        self.type_of_test = type_of_test
        
    def radiological_test(self):
        print("perform rediological test")
        if self.type_of_test=="x_ray":
            Patient.total_bill+=500
        elif self.type_of_test=="ct_scan":
            Patient.total_bill+=2500
        elif self.type_of_test=="mri":
            Patient.total_bill+=7000
        
            
a=Patient(input("Enter the name of the patient: "),int(input("Enter the age of the patient: ")),input("Enter your discease: "))
a.admit_patient()

b=Radiological_Tests(input("Enter a name of test: "))
b.radiological_test()
a.discharge()

    
    
        



# 2 The RadiologicalTests class should have attributes for the department name, type_of_test, and cost. It should include a method to perform a radiological test.

# 3 The Billing class should manage the patient's bill. It should include methods to add charges to the bill and display the total bill amount.
# no inheritace use for this code