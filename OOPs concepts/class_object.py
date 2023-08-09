#example  1
class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print ("hello,my name is", self.name)
a1=Person("priyadharshini")
a1.display()
#example 2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("my name is:",self.name)
        print("my age:",self.age)
p1=Person("priya",20)
p2=Person("dharshini",21)
p1.display()
p2.display()
#example3
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("student name:",self.name)
        print("roll number:",self.roll_no)
        print("marks:",self.marks)
a1=Student("priya",203007,100)
a2=Student("dharshini",203007,89)
a1.display()
a2.display()
#example4
class Subject:
    def __init__(self,subject_name,marks,percentage):
        self.subject_name=subject_name
        self.marks=marks
        self.percentage=percentage
    def display(self):
        print("subject name:",self.subject_name)
        print("marks:",self.marks)
        print("percentage:",self.percentage)
a1=Subject("Physics",98,'98%')
a2=Subject("chemstiry",87,'80%')
a3=Subject("maths",90,'90%')
a1.display()
a2.display()
a3.display()
#example5
class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print ("hello,my name is", self.name)
    def __del__(self):
        print("welcome",self.name)
a1=Person("priyadharshini")
a1.display()
#example6
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("student name:",self.name)
        print("roll number:",self.roll_no)
        print("marks:",self.marks)
    def __del__(self):
        print("good",self.name)
a1=Student("priya",203007,100)
a2=Student("dharshini",203007,89)
a1.display()
a2.display()
class Music:
    def __init__(self,classical,rap,melody):
        self.classical=classical
        self.rap=rap
        self.melody=melody
    def display(self):
        print("classical:",self.classical)
        print("rap:",self.rap)
        print("melody:",self.melody)
    def __del__(self):
        print("i love",self.melody)
a1=Music("chitra","aadhi","anirudh")
a2=Music("mano","harris","yuvan")
a1.display()
a2.display()

#inheritence
class Fruit:
     def fresh(self):
        print("fruits is healthy")
class Apple(Fruit):
    def red(self):
        print("Apple is red in colour")
a=Apple()
a.red()
a.fresh()
class Vehicle:
    def fuel(self):
        print("fuel is used to run the vehicle ")
class Bike:
    def wheel(self):
        print("bike has two wheel")
a=Bike()
a.wheel()
a=Vehicle()
a.fuel()
#multiple inhertience
class A:
    def display(self):
        print("I am A")
class B:
    def display(self):
        print("i am A")
    def display(self):
        print("I Am B")
class C:
    def display(self):
        print('i am A')
    def display(self):
        print("I Am C")
A()
B()
C()
#encapusulation
class Person:
    def __init__(self):
        self.A="priya"
        self._B="dharshini"
    def Printname(self):
        print(self.A)
        print(self._B)
p=Person()
p.Printname()
