class Human:
    def __init__(self , mouth):
        #mouth is another property of Human claass and we use it as femaleextra in Male class
        self.no_eyes = 2
        self.no_nose = 1
        self.no_mouth = mouth
    def talk(self):
        print("i can talk")
    def work(self):
        print("i can work")

class Male(Human):
    def __init__(self , name,femaleextra ):
        #we have to define super().__init__ to access the super class methods as the child class has its own __init__() now.

        super().__init__(femaleextra)      #in this __init__ we can not use the self parameter.
        self.parent = femaleextra
        self.no_mouth = 5
        self.abc =name

    #This is called method overriding, there the method talk() in Male override the method talk() in Human
    def talk(self):
        print("i eat coffe")

#In overriding the child class method gets priority , if we want both class we have to use the method called super
# and under the method of child which is overridng the parent method.
    def work(self):
        super().work()
        print("i can code")

male_1 = Male("Arunava" , 2 )
male_1.talk()
male_1.work()
print(male_1.no_nose)
print(male_1.abc)
print(male_1.parent)
print(male_1.no_mouth)