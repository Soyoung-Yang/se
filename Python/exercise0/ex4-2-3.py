# 게임 다시 시작하기
import random

while True:
    answer = random.randint(1, 100)

    while True:
        user = int(input("Enter the number: "))
        if user > answer:
            print("Down")
        elif user == answer:
            print("Correct! The answer is", answer)
            break
        elif user == 0:
            print("Quit")
            break
        else:
            print("Up")

    m = input("End = Enter 'no' / Restart = Enter any key : ")
    if m == "no":
        print("The End")
        break
    else:
        continue # 해당 명령어 아래쪽 소스를 실행하지 않고 다시 반복문 위쪽으로 올라가서 다시 실행하는 것
    # 아무 키나 눌러도 재시작하는 멘트로 해결 ^^