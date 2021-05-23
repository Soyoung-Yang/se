# Ternary Operators or Conditional Expressions 삼항연산자 혹은 조건표현식
# 실행문이 하나만 있는 경우 하나는 if, 다른 하나는 같은 줄에 넣을 수 있다.
# [true_value] if [condition] else [false_value]

a = 2
b = 330

print("A yummy") if a > b else print("B yummy")

# 같은 줄에 여러 else 문을 사용할 수 있다.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

c = 5
if c > 10:
    if c > 20:
        print("10보다 크고 20보다 크다.")
    elif c == 20:
        print("20이다.")
    else:
        print("10보다 크고 20보다 작다.")
elif c == 10:
    print("10이다.")
else:
    print("10보다 작다.")


d = int(input("Enter the number: "))
if d > 10:
    print("10보다 크고 20보다 크다.") if d > 20 else print("20이다.") if d == 20 else print("10보다 크고 20보다 작다.")
elif d == 10:
    print("10이다.")
else:
    print("10보다 작다.")