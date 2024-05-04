from abc import ABCMeta, abstractstaticmethod #abc stand for abstract base method


class Iperson (metaclass =ABCMeta):
    @abstractstaticmethod
    def person_method():
        """interface mathode"""

class student (Iperson):
    def __int__(self):
        self.name= "basic student"
    def person_method(self):
        print("i am a studen")

class teacher(Iperson) :
    def __int__(self):
        self.name = "basic teacher "
    def person_method(selfa):
        print("i am a teacher")

s1 = student()
s1.person_method()
s2= teacher()
s2.person_method()