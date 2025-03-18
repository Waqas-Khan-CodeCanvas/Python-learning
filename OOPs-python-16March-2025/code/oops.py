# print("hello world!")
# print("how are you")


# class Student:
#     name= "waqas"
    
# s1=Student()
# print(s1.name)    

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "blue"
#     modal = 2024
    
# car1 = Car()
# print(car1.color)    
# print(car1.modal) 

# class Student:
    
#     def __init__(self,name):
#         print("New student is added to the database")
#         self.name=name
        
# s1 = Student("ali")
# print(s1.name)
# s2 = Student("waqas")
# print(s2.name)
# s3 = Student("hamza")
# print(s3.name)
# s4 = Student("sufyan")
# print(s4.name)


class Student:
    college_name="Cadet College Spinkai"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def welcome(self):
        print(f"Hey  welcome {self.name}") 
    
    def get_mraks(self):
        return self.marks    
        
s1 = Student("ali","20")
print(s1.name,s1.get_mraks())  
s1.welcome()         
        
       
