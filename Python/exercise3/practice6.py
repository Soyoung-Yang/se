print("2016112220 양소영")
import json

x = {
    "name":"Soyoung",
    "age":24,
    "attending":True,
    "discharge":True,
    # phones : list, list 각 인덱스(0,1)에 dictionary 저장
    "phones":[
        {"model":"iphone 11", "year":2020},
        {"model":"galaxy s21", "year":2021}
    ]
}

print('1. json.dumps(x)')
print(json.dumps(x)) # python 개체를 json 문자열로 변환
print('\n2. json.dumps(x, indent=4)')
print(json.dumps(x, indent=4)) # 들여쓰기: 띄어쓰기 4칸 = tab 1번
print('\n3. json.dumps(x, indent=4, separators=(". ", " = "))')
print(json.dumps(x, indent=4, separators=(". ", " = "))) # default : ",", ":"
print('\n4. json.dumps(x, indent=4, sort_keys=True)')
print(json.dumps(x, indent=4, sort_keys=True)) # 정렬(a,b,c,d... 순서대로)