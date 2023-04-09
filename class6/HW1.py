class Lesson:
    def __init__(self,teacher,time):
        self.teacher = teacher
        self.time = time
    @classmethod
    def first(cls):
        return cls("Emma","Monday")
    @classmethod
    def second(cls):
        return cls("Peter","Thursday")
    def intro(self):
        print("This lesson is taugh by "+str(self.teacher)+" on "+str(self.time))
first = Lesson.first()
first.intro()
second = Lesson.second()
second.intro()