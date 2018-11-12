class Student:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def get_age(self):
        return self.age

#inheritance
class Cs_student(Student):

    def __init__(self,n,a,s):
        Student.__init__(self,n,a)
        self.section_num = s

    def get_age(self):
        print("age :",str(self.age))

cs_stu1 = Cs_student("ssss",32,'a')
cs_stu1.get_age()

