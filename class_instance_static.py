class show_off:

    var = "correct it is a class variable or static variable"

    def __init__(self,name,age):
        self.age = age
        self.name= name

    def get_name(self):                     # accessor method
        return self.name

    def set_age(self,umar):                  # mutator method
        self.age = umar
        return self.age

    @classmethod
    def class_var(cls):
        return cls.var


    @staticmethod
    def info_about_class():                  # static method and class method are two different things
        return "to show how static , classs , instance method workd"



show = show_off("kanha",17)
print(show.get_name())                    # calling getter
print(show.set_age(18))                       # calling setter
print(show_off.class_var())               # calling a class variable using class method
print(show_off.info_about_class())        # using static method

