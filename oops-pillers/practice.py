# OOPS (Object-Oriented Programming System) in Python:

# Classes and Objects
# In Python, a class is a template for creating objects. A class defines the properties and behaviors of an object

# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model         

#     def full_name(self):
#         print(self.brand,self.model)

# c1 = Car("toyota","corolla")  
# print(c1.brand)      
# print(c1.model) 
# print(c1.full_name())

# c2 = Car("honda","civic")  
# print(c2.brand)      
# print(c2.model)  
# print(c2.full_name()) 


# Inheritance
# Inheritance allows one class to inherit the properties and behaviors of another class. 

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print(self.name ,self.age)    
        
class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color=color
        
        
dog = Dog("sam",20,"black")    
print(dog.name)
print(dog.color)
dog.info()


