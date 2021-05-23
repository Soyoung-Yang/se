txt = """
안녕 나는 댕소야
너는 누구니?
나는 소댕이야
그렇구나
반가워
"""
print(txt[11]) # 문자열의 요소
print(len(txt)) # 문자열 길이
print("소댕" in txt) # True
print("sodang" in txt) # False
print("유댕" not in txt) # True


a = " Hello, Soyoung! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("Hello", "Goodbye"))
print(a.split(","))

age = 24
txt = "My name is Soyoung, and I am {} years old."
print(txt.format(age))