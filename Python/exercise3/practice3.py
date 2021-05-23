print("2016112220 양소영")
# 람다는 다른 함수 내에서 익명 함수 (Anonymous function)로 사용될 때 유용하다.
# 필요한 곳에서 즉시 사용하고 버릴 수 있으므로 짧은 시간 동안 익명 함수가 필요한 경우 람다 함수가 많이 사용된다.

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2) # mydoubler = lambda a : a * 2
print(mydoubler(3)) # mydoubler(3) = lambda 3 : 3 * 2

mytripler = myfunc(3) # mytripler = lambda a : a * 3
print(mytripler(3)) # mytripler(3) = lambda 3 : 3 * 3