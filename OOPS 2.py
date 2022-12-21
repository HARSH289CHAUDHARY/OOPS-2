# class Student:
#     def __init__(self,python,web,math):
#         self.subject1 = python
#         self.subject2 = web
#         self.subject3 = math

#         print((python+web+math)/3)

# s1=Student(4,7,8)       
# s2=Student(9,6,7)



class Student:
    def __init__(self,python,web,math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
    def avg(self,python,web,math):
        print((python+web+math)/3)

s1=Student(4,7,8)       
s1.avg(4,7,8)
s2=Student(9,6,7)
s2.avg(9,6,7)