class test:
    def __init__(self,first,second):
        self.ki=first
        self.ka=second
        print(self.ki)


    def new(self,new_first):
        self.ki-=new_first
        print(self.ki)


check = test(100,56)
check.new(78)