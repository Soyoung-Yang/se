# 게임 다시 시작하기
import random

# def myfunc(n):
#     n = input("One more? [yes/no] ")
#     return n

while True:
    answer = random.randint(1, 100)

    while True:
        user = int(input("Enter the number: "))
        if user > answer:
            print("Down")
        elif user == answer:
            print("Correct! The answer is", answer)
            break
        else:
            print("Up")

    m = input("One more? [yes/no] ")
    if m == "yes":
        continue
    elif m == "no":
        print("The End")
        break
    else:
        print("Enter yes or no")
        # 다른 거 입력했을 때 어떻게 해야 다시 입력하는 거 될지 모르겠다..


    # if myfunc(m) == "yes":
    #         continue
    # elif myfunc(m) == "no":
    #     print("The End")
    #     break
    # else:
    #     print("Enter yes or no")
    #     myfunc(m)