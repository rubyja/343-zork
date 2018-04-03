import Person

def randFloat(Min, Max):
    return random.uniform(Min, Max)
    
class Weapon:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def use(self):
        if (self.name == "HK"):

            return 1
        if (self.name == "SS"):
            if (self.amt < 1):
                print ("You have none!")
                return null
            self.amt = self.amt - 1
            return randFloat(1, 1.75)

        if (self.name == "CB"):
            if (self.amt < 1):
                print ("You have none!")
                return null
            self.amt = self.amt - 1
            return randFloat(2, 2.4)

        if (self.name == "NB"):
            if (self.amt < 1):
                print ("You have none!")
                return null
            self.amt = self.amt - 1
            return randFloat(3.5, 5)