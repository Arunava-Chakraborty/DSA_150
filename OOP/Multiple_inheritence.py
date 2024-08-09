class Human:
    def __init__(self, no_heart):
        self.no_nose = 1
        self.no_eyes = 2
        self.no_heart = no_heart
    def eat(self):
        print("I can Eat")
    def work(self):
        print("work from class Human")

class Male:
    def __init__(self , language):
        self.age = 20
        self.lang = language

    def drink(self):
        print("I drink whisky")
    def work(self):
        print("work from class Male")

class Boy(Human , Male):                   # The order of passing the parameter matters here the human gets more # priority than Male.
    def __init__(self , heart , langu):
        Human.__init__(self , heart)
        Male.__init__(self , langu)
    def work(self):
        print("work from class Boy")

boy_1 = Boy(1,"python")
print(boy_1.no_nose)
print(boy_1.lang)
# IF there are 3 same methods in both parents and child then we can access them in the below way.
#  boy_1.work() ------->>> this will prioritize the work present in Boy
#  Human.work(boy_1)---->> this will prioritize  the work() present in Human
#  Male.work(boy_1)----->>>this will prioritize  the work() present in Human

#*** There is something called 'mro' -> Method Resolution Order which show the priority order of the methods
#print(Boy.mro())
