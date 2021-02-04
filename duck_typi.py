class A:
    def show(self):
        print("to show off")


class B:
    def show(self):
        print("to show off")


class C:
    def show_func(self,show_it):
        show_it.show()


obj = B()
C_obj = C()
C_obj.show_func(obj)

