# 1. Read Json file in Python (json.loads())
import json

# some JSON:
x = '{"name":"Soyoung", "age":"24", "city":"Seoul"}'

"""
parse x:
json 문자열이 있는 경우 json.loads() 메소드 사용하여 구문 분석하여 python으로 읽어올 수 있다.
읽어온 결과는 dictionary 형식을 따름
"""
y = json.loads(x) 

# the result is stored as a Python dictionary:
print(y["age"])

# 2. Wrtie Json file in Python (json.dumps())
# import json

# a Python object (dict):
x = {
    "name":"Soyong",
    "age":24,
    "city":"Seoul"
    }

# convert into JSON: 
# json 문자열로 변환
y = json.dumps(x)

# the result is a JSON string:
print(y) # 문자열 출력