class find:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __gt__(self,other):                     # obj2 > obj1
        if self.a > other.a:
            return True

        else:
            return False


obj1 = find(78,14)
obj2 = find(65,78)
get = obj2 > obj1
print(get.)