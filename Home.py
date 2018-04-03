import random
import Neighborhood

def getRand(Min, Max):
    return random.randint(Min, Max)
#observes npc
class Home:
    def __init__(self, numMons):
        self.numMons = numMon
        self.mons = []
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def updateGrid(self):
    	for observer in self.observers:
            observer.update()

    def update(self):
        self.numMons = self.numMons - 1;
        #need to turn mon into human somehow

    def getMons(self):
        return numMons

    def populate(self):
    	i = getRand(0, 10)
