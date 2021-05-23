print("2016112220 Yang Soyoung")

fruitlist = ["banana", "Orange", "Kiwi", "cherry", "Apple"]
print('Original list : ', fruitlist)

fruitlist.reverse()
print("reverse() -> ", fruitlist)

fruitlist.sort()
print("sort() -> ", fruitlist)

fruitlist.sort(key=str.lower)
print("sort(key=str.lower) -> ", fruitlist)