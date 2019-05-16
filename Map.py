from Wall import *
from Tank import *

class Map:

    def __init__(self, file):
        self.__playerTank = []
        self.__course = []
        self.__walls = []
        self.__enemyTanks = []

        with open(file) as f:
            strips = f.read().splitlines()

        for n in range(0, 9):
            row = []
            tick = 0
            for r in strips[n]:
                tick += 1
                row.append(r)
                if (r == "X"):
                    wall = Wall(47*(tick-1), 45*n)
                    self.__walls.append(wall)
                if (r == "Z"):
                    carl = Tank(45*(tick-.5), 45*(n+.5))
                    self.__playerTank.append(carl)
                if (r == "A"):
                    carrie = Tank(45*(tick-.5), 45*(n+.5))
                    self.__enemyTanks.append(carrie)
            self.__course.append(row)

    def loadNextMap(self):
        pass

    def getPlayerTank(self):
        return self.__playerTank[0]

    def getCourse(self):
        return self.__course

    def getWalls(self):
        return self.__walls

    def getEnemyTanks(self):
        return self.__enemyTanks
