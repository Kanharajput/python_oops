class A:
    def feature1(self):
        print("this is feature one ")


class B(A):
    def feature2(self):
        print("this is feature two")



obj1 = A()
obj1.feature1()

obj2 = B()
obj2.feature2()

print("printing from obj2",end=' '), obj2.feature1()