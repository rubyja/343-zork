import Home
#observable
class npc:
    def __init__(self, Type, hp):
        self.type = Type
        self.hp = hp
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def update(self):
        for observer in self.observers:
            observer.update()

    def setHP(self):
        if (self.type == "Person"):
            self.hp = 100

        if (self.type == "Zombie"):
            self.hp = getRand(50, 100)

        if (self.type == "Vampire"):
            self.hp = getRand(100, 200)

        if (self.type == "Ghoul"):
            self.hp = getRand(40, 80)

        if (self.type == "Werewolf"):
            self.hp = 200