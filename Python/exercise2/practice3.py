print("2016112220 Yang Soyoung")

phonedict = {
    "brand":"Apple",
    "model":"iphone12",
    "year":2020
}
print("phonedict dictionary : ", phonedict)

phonedict["color"] = "red" # dictionary에 새 엔트리 추가
print("Add new element -> ", phonedict)

x = phonedict.get("model") # get() 메소드를 이용하여 항목에 접근
print('get("model") -> ', x)

x = phonedict.keys() # dictionary 변경 사항이 생길 시, key 목록에 바로 반영
print("keys method -> ", x)

x = phonedict.values() # dictionary에 있는 모든 values들의 목록 반환
print("values method -> ", x)

x = phonedict.items() # items() 메소드로 dictionary의 각 항목을 tuple로 변환
print("items method -> ", x)