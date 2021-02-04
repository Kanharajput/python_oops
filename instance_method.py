class ulu:
    def __init__(self,one,two):
        self.one = one
        self.two = two

    def get_one(self):
        return self.one               # accesor method

    def get_two(self):
        return self.two

    def set_one(self,value):           # motatar method
        self.one = value
        return self.one

    def set_two(self,value):
        self.two = value
        return self.two


nahi = ulu("kanha", "tomar")
print(nahi.get_one())
print(nahi.set_two(420))
