'''
overriding means same funcion in two different class
'''


class A():
    def chapo(self):
        print("dhasho, last concept of oops")


class B(A):
   ''' def chapo(self):
        print("this is last function from last class class object")
'''


obj_A = A()
obj_B = B()


obj_B.chapo()
obj_A.chapo()

'''
if ther is no function regarding we pass fo a class then the cbject call the same function from the inhereted class parent
'''

