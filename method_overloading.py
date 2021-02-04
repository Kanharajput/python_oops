class A:
    def show(self):
        print("cool from A")

    def show(self,a):
        print("cool from another function of A")


A_obj = A()
A_obj.show(4)

'''
python don't have the concept of function overloading
'''