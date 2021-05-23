class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Soyoung", "Yang")
x.printname()

# Person 클래스(부모)의 기능을 상속하는 Student 클래스(자식)
# Person 클래스(부모)를 매개변수로 보낸다.
class Student(Person): 
    pass
y = Student("Sooyoung", "Jeong")
y.printname()

# 상속 재정의 : 자식 클래스에 __init__() 함수를 추가하면, 더이상 상위 부모 클래스 함수의 __init__() 함수를 상속하지 않는다.
class Child(Person):
    def __init__(self, fname, lname):
        # 1. add properties etc.
        # self.firstname = fname
        # self.lastname = lname
        Person.__init__(self, fname, lname) # 부모의 __init__() 함수 상속 유지 -> 부모함수에 대한 호출 추가 후 __init__() 함수 사용
z = Child("Jeongmo", "Yang")
z.printname()

# super() 함수 : 자식 클래스가 부모로부터 모든 메소드와 속성 상속
# Add properties 1
class Children(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # 메소드와 속성을 상속할 상위 부모 클래스의 이름을 불러올 필요가 없다.
        self.graduationyear = 2021 # Children 클래스에 graduationyear라 불리는 property 추가
x = Children("Soyoung", "Yang")
x.printname()
print(x.graduationyear)

# Add properties 2
class Adult(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Adult("Soyoung", "Yang", 2021)
x.printname()
print(x.graduationyear)

# Add Method
class Happy(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self): # welcome 메소드를 Happy 클래스(자식)에 추가한다.
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Happy("Soyoung", "Yang", 2021)
x.welcome()
# 부모 클래스의 함수와 이름이 같은 메소드를 자식 클래스에 추가하면, 부모 메소드의 상속이 재정의된다.