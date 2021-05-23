# dictionary - setdefault(), fromkeys()
import json

# 1. setdefault()
print("\n1. setdefault()\n")

# setdefault(키)는 딕셔너리에 키-값 쌍을 추가합니다. 
# setdefault에 키만 지정하면 값에 None을 저장합니다. 
# 다음은 키 'e'를 추가하고 값에 None을 저장합니다.
a = {'u' : 1, 'v' : 2, 'g' : 3}
a.setdefault('e')
print(a)

# setdefault(키, 기본값)처럼 키와 기본값을 지정하면 값에 기본값을 저장한 뒤 해당 값을 반환합니다.
a.setdefault('f', 100)
print(a)
print("\n\n")

# 2. fromkeys()
print("2. fromkeys()\n")

# dict.fromkeys(키리스트)는 키 리스트로 딕셔너리를 생성하며 값은 모두 None으로 저장합니다.
xlist = ["name", "age", "city"] # key list
xdict = dict.fromkeys(xlist)
print(xdict)

# dict.fromkeys(키리스트, 값)처럼 키 리스트와 값을 지정하면 해당 값이 키의 값으로 저장됩니다.
ydict = dict.fromkeys(xlist, 10) # 모든 value가 10으로 저장
print("\n", json.dumps(ydict, indent=4))


# values 할당
xdict["name"] = "Soyoung"
xdict["age"] = 24
xdict["city"] = "Seoul"

print("\n", json.dumps(xdict, indent=4))