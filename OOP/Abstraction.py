from abc import ABC , abstractmethod

class vehichel(ABC):
    def __init__(self , n):
        self.no_of_tires = n

    def lock(self):
        print("locks with the key")
    @abstractmethod
    def start(self):
        print("this is an abstract class do not touch it")
        ...


class bike(vehichel):
    def __init__(self , n):
        self.no_of_tires = n
    def start(self):
        print("starts with kick")

class scooty(vehichel):
    def __init__(self, n):
        self.no_of_tires = n
    def start(self):
        print("self start")

class car(vehichel):
    def __init__(self , n):
        self.no_of_tires = n
    def start(self):
        print("Start with clutch")


vehichel_1 = vehichel(5)
vehichel_1.lock()
