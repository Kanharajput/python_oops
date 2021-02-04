class sum:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        #return a,b
        solve = sum(a,b)
        return solve
obj1 = sum(50,0)
obj2 = sum(100,10)
kanha = obj1 + obj2
# print(kanha)
print(kanha.a)