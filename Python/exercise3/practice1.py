print("2016112220 양소영")

def func(*args, **kwargs):
    for x in args:
        print(x)
    print('My Name : ', kwargs["name"], ' & My Age : ', kwargs["age"])

func(1,2,3,4, name='Soyoung', age=25)