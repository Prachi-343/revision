# 1. Creating a Class: Define a Python class called Person with attributes name and age. Implement a method called introduce that prints out the name and age of the person.

# class Person :
#     def print_name(self,name):
#         print("person name:",name)
#     def print_age(self,age):
#         print("person age:  ",age)
# a=Person()
# a.print_name("prachi")
# a.print_age(20)
        

# 2. Creating Objects: Create two instances of the Person class with different names and ages, and call the introduce method for each object.

# class Person:
#     def __init__(self,name, age):
#             self.name = name
#             self.age = age
#     def introduce(self):
#         print("person name: ",self.name)
#         print("person age: ",self.age)
# a=Person("prachi",20)
# b=Person("siddarth",20)
# a.introduce()
# b.introduce()


# 3. Inheritance - Single: Create a class Student that inherits from the Person class. Add an additional attribute student_id to the Student class. Override the introduce method to include the student's ID.

# class Person:
#     def __init__(self,name, age):
#             self.name = name
#             self.age = age
#     def introduce(self):
#         print("person name: ",self.name)
#         print("person age: ",self.age)
    
# class Student(Person):
#     def __init__(self,name,age,id):
#         super().__init__(name,age)
#         self.stud_id = id
#     def introduce(self):
#         super().introduce()
#         print("my id is ",self.stud_id)   
# info=Student("prachi",20,27)
# info.introduce()


# 4. Multiple Inheritance: Create two parent classes A and B. Then, create a child class C that inherits from both A and B. Add a method show_info to class C that prints "This is class C".

# class A:
#     def print_A(self):
#         print("This is class A")

# class B:
#     def print_B(self):
#         print("This is class B")

# class C(A,B):
#     def show_info(self):
#         print("This is class C")
# a=C()
# a.show_info()
    

# 5. Multilevel Inheritance: Define three classes Vehicle, Car, and ElectricCar. Car inherits from Vehicle, and ElectricCar inherits from Car. Each class should have a method drive() which prints a message specific to that class.

# class Vehicle:
#     def v_drive(self):
#         print("This is class Vehicle")
# class Car(Vehicle):
#     def print_drive(self):
#         print("This is class Car")
# class electricCar(Car):
#     def drive(self):
#         print("This is class electricCar")
# a=electricCar()
# a.drive()
# a.print_drive()
# a.v_drive()
    
    
# 6. Accessing Parent Class Methods: In a multilevel inheritance scenario similar to the previous question, add a method show_info to the Vehicle class. Then, in the ElectricCar class, call the show_info method of the Vehicle class.

# class Vehicle:
#     def v_show_info(self):
#         print("This is class Vehicle")
# class Car(Vehicle):
#     def  c_show_info(self):
#         print("This is class Car")
# class electricCar(Car):
#     def show_info(self):
#         print("This is class electricCar")
# a=electricCar()
# a.v_show_info()
# a.c_show_info()
# a.show_info()

#  7. Overriding Methods: Create a parent class Shape with a method area that returns 0. Then, create child classes Rectangle and Triangle that override the area method to calculate the area of a rectangle and a triangle, respectively.

# class Shape:
#     def area(self):
#         return 0
    
# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.l =l
#         self.w=w
#     def area (self):
#         print("Area of rectangle",self.l*self.w)


# class Triangle(Shape):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area (self):
#         print("Area of triangle",(self.b*self.h)/2)
        
# a=Rectangle(10,5) 
# b=Triangle(5,8) 
# a.area()
# b.area()


# 8. Using super(): In a multilevel inheritance scenario, modify the show_info method of the Vehicle class to print "This is a vehicle". Then, in the Car class, use super() to call the show_info method of the Vehicle class, and add "This is a car" to the output.

# class Vehicle:
#     def show_info(self):
#         print("This is class Vehicle")
# class Car(Vehicle):
#     def  show_info(self):
#         super().show_info()
#         print("This is class Car")
# class electricCar(Car):
#     def show_info(self):
#         super().show_info()
#         print("This is class electricCar")
        
# a=electricCar()
# a.show_info()



# 9. Class Variables and Methods: Create a class Employee with a class variable num_of_employees initialized to 0. Increment this variable every time a new employee is created. Implement a class method get_num_of_employees that returns the total number of employees.

# 10. Static Methods: Add a static method is_adult(age) to the Person class that takes an age as input and returns True if the age is 18 or above, otherwise False.

# 1 Create a Python class called BankAccount. Define an init() method that initializes the account_number, balance, and account_holder attributes. Create methods for deposit, withdrawal, and displaying account details.


# class BankAccount:
#     def __init__(self, account_no, balance, account_holder):
#         self.account_no = account_no
#         self.balance = balance
#         self.account_holder = account_holder
#     def deposite (self,amount):
#         print(f"{amount} deposited successfully")
#     def withdral (self,amount):
#         print(f"{amount} withdrawal successfully")
#     def displaying (self):
#         print("displaying successfully")
# a=BankAccount()


# 2 Create a subclass called SavingsAccount, inheriting from the BankAccount class. Define an init() method that also initializes the interest_rate attribute. Override the deposit method to include interest calculation.

# class BankAccount:
#     def __init__(self, account_no, balance, account_holder):
#         self.account_no = account_no
#         self.balance = balance
#         self.account_holder = account_holder
#     def deposite (self,amount):
#         print(f"{amount} deposited successfully")
#     def withdral (self,amount):
#         print(f"{amount} withdrawal successfully")
#     def displaying (self):
#         print("displaying successfully")
        
# class SavingsAccount(BankAccount):
#     def __init__ (self,account_no,balance,account_holder,interest_rate):
#         self.interest_rate = interest_rate
#         super().__init__(account_holder,account_no,balance)
#     def simple_interest(self,period,principal,amount):
#         print("your interest ",(period*principal*self.interest_rate)/100)
#         super().deposite(amount)
#         super().displaying()
        
# obj=SavingsAccount(
#     input("Enter your name: "),
#     int(input("Enter account no:")),
#     int(input("Enter account balance:")),
#     int(input("Enter rate of interest:"))
# )

# obj.simple_interest(
#     int(input("Enter loan principal:")),
#     int(input("Enter loan period:")),
#     int(input("Enter your deposite amount:")),
    
# )
        
        
# 3 Create another subclass called CheckingAccount, also inheriting from the BankAccount class. Define an init() method that also initializes the transaction_limit attribute. Override the withdrawal method to check if the withdrawal amount exceeds the transaction limit.

# class BankAccount:
#     def __init__(self, account_holder,account_no,balance):
#         self.account_no = account_no
#         self.balance = balance
#         self.account_holder = account_holder
#     def deposite (self,amount):
#         print(f"{amount} deposited successfully")
#         self.balance += amount
#     def withdrawal (self,amount):
#         print(f"{amount} withdrawal successfully")
#         self.balance -= amount
#     def displaying (self):
#         print(f"{self.account_holder} your account no is: {self.account_no}")
#         print(f"{self.balance} your balance is: {self.balance}")
        
# class CheckingAccount(BankAccount):
#     def __init__(self,account_holder,account_no,balance=10000 ,transaction_limit=8000):
#         self.transaction_limit = transaction_limit
#         super().__init__(account_holder,account_no,balance)
#     def withdrawal(self,amount):
#         if amount<self.transaction_limit and amount<self.transaction_limit:
#             self.balance-=amount
#             print(f"{amount} withdrawal successfully your current balance is:{self.balance}")
            
#         elif  self.transaction_limit<amount:
#             print(f" withdrawal amount exceeds your transaction limit")

#         else:
#             print("insufficient balance to withdraw")
            
# obj=CheckingAccount(
#     input("Enter your name:"),
#     int(input("Enter your account number:"))
# )
# obj.displaying()
# obj.withdrawal(int(input("Enter your amount:")))
            
            
# 4 Create instances of the SavingsAccount and CheckingAccount classes and demonstrate the functionality of their methods.

# 5 Create a Python class called Person. Define an init() method that initializes the name, age, and gender attributes. Create a method called display_info() that prints the name, age, and gender of the person.

# class person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def display_info(self):
#         print("your name:",self.name)
#         print("your age:",self.age)
#         print("your gender:",self.gender)
# obj=person("prachi",20,"female")
# obj.display_info()
    

# 6 Create a subclass called Student, inheriting from the Person class. Define an init() method that also initializes the student_id attribute. Override the display_info() method to also display the student ID.


# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def display_info(self):
#         print("your name:",self.name)
#         print("your age:",self.age)
#         print("your gender:",self.gender)
# class Student(Person):
#     def __init__(self,name,age,gender,student_id):
#         self.student_id = student_id
#         super().__init__(name,age,gender)

#     def display_info(self):
#         super().display_info()
#         print("your student id:",self.student_id)
# obj=Student(
#     input("Enter your name:"),
#     int(input("Enter your age:")),
#     input("Enter your gender:"),
#     int(input("Enter student_id:"))
# )   
# obj.display_info()


# 7 Create another subclass called Teacher, also inheriting from the Person class. Define an init() method that also initializes the subject attribute. Override the display_info() method to also display the subject taught.

# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def display_info(self):
#         print("your name:",self.name)
#         print("your age:",self.age)
#         print("your gender:",self.gender)

# class Teacher(Person):
#     def __init__(self,name,age,gender,subject):
#         self.subject = subject
#         super().__init__(name,age,gender)
        
#     def display_info(self):
#         super().display_info()
#         print("your subject is :",self.subject)
# obj=Teacher(
#     input("Enter your name:"),
#     int(input("Enter your age:")),
#     input("Enter your gender:"),
#     input("Enter your subject:")
# )
# obj.display_info()

# 8 Create instances of the Student and Teacher classes and demonstrate the functionality of their methods.

# 9 Create a Python class called Animal. Define an init() method that initializes the name attribute. Create a method called speak() that prints a generic message indicating the animal's sound.

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} says something")
# obj=Animal()
# obj.speak()
        
# 10 Create subclasses for specific types of animals, such as Dog, Cat, and Cow, each inheriting from the Animal class. Override the speak() method in each subclass to print the sound specific to that animal.

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} says something")    
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says bark")
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says meww")
# class Cow(Animal):
#     def speak(self):
#         print(f"{self.name} says humm")
# dog=Dog("Tommy")
# cat=Cat("Jerry")
# cow=Cow("Rani")
# dog.speak()
# cat.speak()
# cow.speak()


# 11. Design a class hierarchy for a multimedia player. Create a base class Media with attributes title and duration and methods play() and pause(). Then, create subclasses Audio and Video. Ensure that Audio can also adjust volume, and Video can seek to a specific time.

# class Media:
#     def __init__(self, title, duration):
#         self.title=title 
#         self.duration=duration
#     def play(self):
#         print(f" playing {self.title}")
#     def pause(self):
#         print(f" paused {self.title}")

# class Audio(Media):
#     def __init__(self, title, duration):
#         super().__init__(title, duration)
#     def Adjust_Volume(self, volume):
#         print(f" adjusting volume by {volume}")

# class Video(Media):
#     def __init__(self, title, duration):
#         super().__init__(title, duration)
#     def seek(self,time):
#         print(f"seeking by {time} seconds")

# audio=Audio("Teri divani",4)
# video=Video("Fighter",15)
# audio.play()
# audio.Adjust_Volume(70)
# audio.pause()
# video.play()
# video.seek(10)
# video.pause()


# 12. Implement a class DynamicObject that allows dynamic creation of attributes during runtime, but restricts the deletion of attributes to those defined in its _init_ method.

# 13. Develop a base class Animal with a method make_sound(). Create a subclass Dog that overrides make_sound() to bark. Then, create another subclass Cat that overrides make_sound() to meow. Ensure that each subclass calls the overridden method of its immediate parent using super().

# class Animal:
#     def make_sound(self):
#         pass 
# class Dog(Animal):
#     def make_sound(self):
#         super().make_sound()
#         print(f"bark")
# class Cat(Animal):
#     def make_sound(self):
#         super().make_sound()
#         print(f"meww")
# animal=Animal()
# dog=Dog()
# cat=Cat()
# animal.make_sound()
# dog.make_sound()
# cat.make_sound()    


# 14. Create a class Student with attributes name, age, and grade. Implement the _init_ method to accept name and age parameters and set grade based on age (e.g., if age < 12, grade is 'Elementary'; if age < 15, grade is 'Middle School', else 'High School').

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.grade =self.set_grade()
    
#     def set_grade(self):
#         if self.age<12:
#             return "Elementary"
#         elif self.age<15:
#             return "Middle School"
#         else :
#             return "High School"
#     def display(self):
#         print(f"{self.name} your age is  {self.age} and your grade is {self.grade}")
# student1=Student(input("Enter name: "),int(input("Enter age: ")))
# student1.display()


        
# 15. Develop a class hierarchy for a vehicle rental system. Create a base class Vehicle with attributes make, model, and year. Then, create subclasses Car, Truck, and SUV. Ensure that each subclass initializes these attributes using super() and provides additional attributes specific to the vehicle type.

# class Vehicle():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model=model
#         self.year=year
    
    
# class Car(Vehicle):
#     def __init__(self,make,model,year,seats):
#         self.seats=seats
#         super().__init__(make,model,year)
#     def display(self):
#         print("car details: ")
#         print("make: ",self.make)
#         print("model: ",self.model)
#         print("year: ",self.year)
#         print("seats: ",self.seats)        
        
# class Truck(Vehicle):
#     def __init__(self, make, model, year,load):
#         self.load=load
#         super().__init__(make, model, year)
#     def display(self):
#         print("truck details: ")
#         print("make: ",self.make)
#         print("model: ",self.model)
#         print("year: ",self.year)
#         print("load: ",self.load)        
        

# class Suv(Vehicle):
#     def __init__(self, make, model, year,power):
#         self.power=power
#         super().__init__(make, model, year)
#     def display(self):
#         print("suv details: ")
#         print("make: ",self.make)
#         print("model: ",self.model)
#         print("year: ",self.year)
#         print("power: ",self.power)        
        
    
# car=Car("suzuki","ertiga",2022,"6 seater")
# truck=Truck("tata","t-1613",2012,"4 ton")
# suv=Suv("mahindra","thar",2023,"2.5 l")
# car.display()
# truck.display()
# suv.display()


    
#16. Using super(): In a multilevel inheritance scenario, modify the show_info method of the Vehicle class to print "This is a vehicle". Then, in the Car class, use super() to call the show_info method of the Vehicle class, and add "This is a car" to the output.

# class Vehicle:
#     def __init__(self,vh_type):
#         self.vh_type = vh_type
#     def show_info(self):
#         print(f"This is a {self.vh_type}")
# class Car(Vehicle):
#     def __init__(self,car_type,vh_type):
#         self.car_type = car_type
#         super().__init__(vh_type)
#     def display(self):
#         super().show_info()
#         print(f"This is a {self.car_type}")

# obj=Car("Fortuner","xuv")
# obj.display()


# 17.Create a class bank with attribute name, account_number and balance with display() method.create a subclass trasaction and loan.transaction contains amount withdrall() and deposit() method.and loan contain amount period,rate of interrest and interest() method.object structure is first pass the data after that ask to user which functionality they want to use. 


# class Bank:
#     def __init__(self, name, account_number, balance=200000):
#         self.name = name
#         self.account_number = account_number
#         self.balance = balance

#     def display(self):
#         print(f"{self.name} your account number is: {self.account_number}")
#         print(f"{self.name} your balance is : {self.balance}")

# class Transaction(Bank):
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"{amount} withdraw successfully")
#         print(f"your current balance is {self.balance}")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited successfully")
#         print(f"your current balance is {self.balance}")

# class Loan(Bank):
#     def interest(self, amount, period, rate=3):
#         si = (amount * period * rate) / 100
#         print(f"{si}rs you have to pay for the interest")

# sbi = Bank(input("Enter your name: "),
#            int(input("Enter your account number: ")))

# ans = int(input("""for withdrawal press 1 
# for deposit press 2
# for loan press 3 
# for balance check press 4 \n
# """))

# if ans == 1:
#     withdraw = Transaction(sbi.name, sbi.account_number, sbi.balance)
#     amount = int(input("Enter your withdrawal amount: "))
#     withdraw.withdraw(amount)
# elif ans == 2:
#     deposit = Transaction(sbi.name, sbi.account_number, sbi.balance)
#     amount = int(input("Enter your deposit amount: "))
#     deposit.deposit(amount)
# elif ans == 3:
#     loan = Loan(sbi.name, sbi.account_number, sbi.balance)
#     amount = int(input("Enter your loan amount: "))
#     period = int(input("Enter your loan period: "))
#     loan.interest(amount, period)
# elif ans == 4:
#     sbi.display()
# else:
#     print("Invalid input please press a valid button")  
           

# designing a simplified hospital system that focuses on patient management, radiological tests, and billing. Implement classes for Patient, RadiologicalTests, and Billing.

# 1 The Patient class should have attributes for name, age, and condition. It should include methods to admit a patient and discharge them.

# 2 The RadiologicalTests class should have attributes for the department name, type_of_test, and cost. It should include a method to perform a radiological test.

# 3 The Billing class should manage the patient's bill. It should include methods to add charges to the bill and display the total bill amount.
# no inheritace use for this code

        
class Patient:
    def __init__(self,name,age,condition):
        self.name = name
        self.age = age
        self.condition = condition
    def admit_patient():
        pass 
    def discharge(): 
        pass 
        
            
            
 