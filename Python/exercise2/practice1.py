print("2016112220 Yang Soyoung")

msclist = ["math", "science", "computer"]
print('Original List : ', msclist)

msclist.insert(1, "algorithm") # 1번 인덱스에 algorithm 삽입
print('insert(1, "algorithm") : ', msclist)

msclist.append("algorithm2") # 리스트 맨 뒤에 algorithm2 추가
print('append("algorithm2") : ', msclist)

msclist.remove("science") # 리스트 요소 중 science 제거
print('remove("science") : ', msclist)

msclist.pop() # 마지막 항목 제거
print('pop() : ', msclist)

del msclist[0] # 지정된 인덱스 제거
print('del msclist[0] : ', msclist)

msclist.clear() # 목록 비우기, 목록은 존재
print('clear() : ', msclist)