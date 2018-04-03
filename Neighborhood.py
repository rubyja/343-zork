import random

#observes house, updates grid when house changes
class Neighborhood(object):
    def __init__(self, height, width, house):
        self.height = height
        self.width = width
        self.house = house
        
    def update(self):
        #update grid when house changes somehow
        pass

    def makeGrid(self):
        if(self.house == True):
            grid = [["-" for i in range(10)] for i in range(5)]
            return grid
        else:
            grid = [["-" for i in range(self.width)] for i in range(self.height)]
            return grid

    def printGrid(self, grid):
        a = grid
        for row in a:
            for e in row:
                print (e, end =" ")
            print(" ")