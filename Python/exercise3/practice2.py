print("2016112220 양소영")

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
        # print(result)
    # print(result)
    return result
    # print(result)
    

print("The example of recursion")
tri_recursion(6)
# tri_recursion(6) : result = 6 + tri_recursion(5) = 6+15 = 21
# tri_recursion(4) : result = 5 + tri_recursion(4) = 5+10 = 15
# tri_recursion(3) : result = 4 + tri_recursion(3) = 4+6 = 10
# tri_recursion(2) : result = 3 + tri_recursion(2) = 3+3 = 6
# tri_recursion(1) : result = 2 + tri_recursion(1) = 2+1 = 3
# tri_recursion(0) : result = 1 + tri_recursion(0) = 1+0 = 1
# tri_recursion(0) : result = 0