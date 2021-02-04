class choriya:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.kam = self.kamini("chori name")
        
    class kamini:
        def __init__(self,meko_ni_pata):
            self.kya = meko_ni_pata
            
        def choriya_name(self):
            return self.kya
        
oxygen = choriya("no",18)
new_obj = oxygen.kam
print(new_obj.choriya_name())
