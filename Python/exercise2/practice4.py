print("2016112220 Yang Soyoung")

score = input("score: ") # Enter user input:
score = int(score) # 입력값을 int형으로 저장
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")