"""
class People:
    def __init__(self,name,age,favoritefood):
        self.name = name
        self.age = age
        self.favoritefood = favoritefood
    def intro(self,name,age,favoritefood):
        print("I am "+str(name)+", I'm "+str(age)+" years old, and I like",str(favoritefood))
    def talk(self,content):
        print("I shout: "+ str(content))
Person = People("Yoshi",12,"icecream")
Person.intro("Yoshi",12,"icecream")
Person.talk("I don't like to do HW")
"""
"""
# Cars styles
class Cars:
    # 類別屬性
    door = 4
    # 實體方法(Instance Method)
    def drive(self):
        self.__class__.door = 5
print("Cars original door: ", Cars.door)
mazda = Cars()
mazda.drive()
print("Cars new door: ", Cars.door)
"""
"""
class health:
    healthl = "healthy"
    def getCold(self):
        self.__class__.healthl = "sick"
print("Origin: I'm", health.healthl)
Me = health()
Me.getCold()
print("After getCold(): I'm",health.healthl)
"""
"""
class Person:
    def __init__(self,eyesColor,hairColor):
        self.eyes = eyesColor
        self.hair = hairColor
    @classmethod
    def American(cls):
        return cls("blue","brown")
    @classmethod
    def Taiwanese(cls):
        return cls("black","black")
    def intro(self):
        print("My eye is "+str(self.eyes)+" and my hair is "+str(self.hair))
American = Person.American()
American.intro()
Taiwanese = Person.Taiwanese()
Taiwanese.intro()
"""
class Person:
    @staticmethod
    def hours(working_hour):
        return working_hour
work = Person()
work_time = work.hours(8)
print("working hours : ",work_time)