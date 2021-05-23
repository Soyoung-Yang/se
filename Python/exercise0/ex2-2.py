# Update tuple
# 튜플 자체의 값 변경은 불가능함
# 리스트로 변환해서 수정 후 다시 튜플로 변환
msctuple = ("math", "science", "computer")
y = list(msctuple)
print(y)
y[1] = "Software"
y.append("Algorithm")
print(y)
y.remove("computer")
msctuple = tuple(y)
print(msctuple)
del msctuple
del y

# Set
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"a", "b", "c", "d", "f"}
# x.intersection_update(y)
# print(x)
# w = x.intersection(y)
# x.symmetric_difference_update(y)
# w = x.symmetric_difference(y)
# print(w)
# w = x.difference(y)
# print(w)
# x.isdisjoint(y)

print(x.issubset(z))
print(z.issuperset(x))