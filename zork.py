# python 3.6, ZORK!, Jacob Ruby
import random
import npc
import Weapon
import Neighborhood
import Person
import Home
      
def getRand(Min, Max):
    return random.randint(Min, Max)

class main:
    neighborhood = Neighborhood.Neighborhood(10, 50, False)
    house = Neighborhood.Neighborhood(0, 0, True)
    neighborhood.printGrid(neighborhood.makeGrid())
    house.printGrid(house.makeGrid())
    you = Person.Player(getRand(100, 125), getRand(10, 25))
    hp = you.hp
    atk = you.atk
    print(hp)
    print(atk)
