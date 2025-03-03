# class Student:
#     "student details"
# print(dir(Student))
# print(Student.__doc__)

# class Student:
#     "student details"
    
#     def __init__(self):
#         print("cons called")
#         print(id(self))
        
# obj=Student()
# print(id(obj))
#----------------------------------------------------------------------
# class Student:
#     "student details"
    
#     def __init__(self,name,roll,marks):
#         self.x=name
#         self.y=roll
#         self.z=marks
        
# obj=Student("neeraj",80,100)
# print(obj.x)
# print(obj.y)
# print(obj.z)

#-----------------------------------------------------------multiple constructor

class Student:
    "student details"
    
    def __init__(self,name,roll,marks):
        self.x=name
        self.y=roll
        self.z=marks
        
    def __init__(self):
        print("constructor called")
        
s1=Student()


