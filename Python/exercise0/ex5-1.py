class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name + " and I am " + str(abc.age) + " years old.")
    
p1 = Person("Soyoung", 24)
# p1.age = 42 # 객체 속성 수정
# del p1.age # 객체 속성 삭제
p1.myfunc()
