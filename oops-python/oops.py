

# class className 
# class  Car:
#     name="civic"
#     model=2024
    
# # objName = ClassName()
# car1 = Car()
# print(car1.name,car1.model)
# # print(car1.model)

    
    
# class  Car:
#     name=None
#     model=None
    
#     # def set_name(self,name):
#     #     self.name=name
        
#     # def get_name(self):
#     #     return self.name   
    
#     # def set_model(self,model):
#     #     self.model=model
        
#     # def get_model(self):
#     #     return self.model  
    


# # car_name=input("Enter your car name here :")
# # mode_name=input("Enter your model car  here :")

# # car1.set_name(car_name)
# # print(car1.get_name())

# # car1.set_model(mode_name)
# # print(car1.get_model())

# # print("\n")

# # car2.set_name("toyota")
# # print(car2.get_name())

# # car2.set_model(2025)
# # print(car2.get_model())



# class  Car:
#     name=None
#     model=None
    
#     def __init__(self , name , model):
#         print("object is created ")
#         self.name=name
#         self.model =model

# car1 = Car("civic",2024)
# car2= Car("toyota",2025)

# car3 = Car()

# print(car1.name)
# print(car1.model)
# print("\n")    
# print(car2.name)
# print(car2.model)


class Stutent:
    name=None
    age=None
    stdId=None
    
    def __init__(self , name , age ,stdId):
        self.name=name
        self.age=age
        self.stdId=stdId
        
    def __init__(self , name , age ):
        self.name=name
        self.age=age
      
    def __init__(self , name ):
        self.name=name
        
        
#     def eating(self):
#         print(f"Student {self.name} can eat")
        
#     def stdLearn(self):
#         print(f"student {self.name} can rata the books")        
        
s1 = Stutent("ali")
# s2 = Stutent("hamza",10,76543)

print(s1.name , s1.age ,s1.stdId)
# print(s2.name , s2.age ,s2.stdId)
# print(s1.eating())
# print(s1.stdLearn())
    
    
    
