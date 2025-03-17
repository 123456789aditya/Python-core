# # def add(x,y,z):
# #     return x+y+z

# # def display():
# #     print("hi")

# from abc import ABC,abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass

# class Laptop():
#     def one(self):
#         print("its running")
        
        
# class Program(Computer):
#     def process(self,com):
#         print("Solving Bugs")
        
        
        
# com=Computer()        
# p1=Program()
# p1.process()

class A:
    x=10
    y=20
    def home(self):
        print("have a home")
        
    def car(self):
        print("have a car")
        
class B(A):
    def newHome(self):
        print("new home")
        
obj=B()
obj.home()