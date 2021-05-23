def myfunc(n):
    return abs(n - 50)
numlist = [100, 50, 65, 82, 23]
numlist.sort()
print(numlist)
numlist.sort(key=myfunc)
print(numlist)