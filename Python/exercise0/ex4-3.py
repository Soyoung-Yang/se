# format 함수 사용법

a, b = 30, 40

print("a =", a)
print("a = " + str(a))
print("b = {}".format(b))

age = 24
txt = "I am {} years old.".format(age)
print(txt)

txt2 = "I am {} years old."
print(txt.format(age))

print("I am {} years old.".format(age))
print("I am {} and {}.".format('Soyoung', age))
print("I am {0} and {1}.".format('Soyoung', age))
print("I am {1} and {0}.".format('Soyoung', age))

name = "Soyoung"
print("I am " + "Soyoung")
print("I am " + name)
print("I am", name)