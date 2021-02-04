class bus:
    def __init__(self,dri_name):
        self.dri_name = dri_name
        self.bache_info = self.bache("kanha")    # creating obj inside the class
 
    def driver_name(self):
       return self.dri_name

    class bache:
        def __init__(self,chi_name):
            self.chi_name = chi_name

        def bache_name(self):
            return self.chi_name

jan1 = bus("mahen bhaiya")            # creating another object for bus
jan = bus("shayam bhaiya")            # creating obj of bus class
print(jan.driver_name())              # calling driver nmae
print(jan.bache_info.bache_name())
info = jan.bache_info                 # creating another object
print(info.bache_name())              # calling bache_name
print(jan1.bache_info.bache_name())   # calling banche name from another object
info1 = jan1.bache_info
print(info1.bache_name())             # calling from another object of bache class
