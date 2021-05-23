print("2016112220 Yang Soyoung")

data_type = ['str', 'int', 'float', 'complex', 'list', 'tuple', 'dict']
print(data_type)

for x in data_type: # data_type 리스트에 있는 각 항목에 대해서 반복
    if x == "complex":
        continue # loop의 현재 반복을 중단하고 다음을 계속
    if x == "dict":
        break # 중단
    print(x)