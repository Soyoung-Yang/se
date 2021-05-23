"""
try:
    f = open("demofile.txt")
    f.write("Write demofile.txt")
except:
    print("Error in handling the file")
finally:
    f.close()
"""

"""
x = -1
if x < 0:
    raise Exception("x is less than 0")
"""

username = input("Enter username: ")
print("Username is " + username)

"""
age = 24
name = "Soyoung"
year = 2021
"""
txt = "My name is {name}. {name} is {age} years old in {year}."
print(txt.format(age=24, name="Soyoung", year=2021))