# random 숫자 맞히기
import random

answer = random.randint(1, 100)

while True:
    user = int(input("Enter the number: "))

    if user > answer:
        print("Down")
    elif user == answer:
        print("Correct! The answer is " + str(answer))
        print("Correct! The answer is", answer)
        print("Correct! The answer is {}".format(answer))
        break
    else:
        print("Up")

