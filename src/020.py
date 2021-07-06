
class A:
    def __init__(self, val):
        self.val = val

    def __add__(self, other): # self는 자기 자신(a1), other는 상대(a2)가 돼서, a1+a2가 됨.
        return self.val + other.val

    def __mul__(self, other):
        return "__mul__"

a1 = A("a")
a2 = A("b")
print(al.val + a2.val)
print(a1 + a2)
print(a1 * a2)







'''
val1 = "Bio"
val2 = "Informatics"
result = val1 + val2

print(result)
'''
