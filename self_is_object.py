class check:
    def __init__(self,name,blood):
        self.name = name
        self.blood_group = blood


    def check(self,ki_wala_obj):                             # self is te object whick is calling the function 

        if self.blood_group == ki_wala_obj.blood_group:
            print("same blood group")

        else:
            print("different blodd group")



ka = check("kanha", "o+")  
ki = check("laddu", "bhagwan_jane")
ka.check(ki)
print(ka.name , ka.blood_group)
print(ki.name , ki.blood_group)