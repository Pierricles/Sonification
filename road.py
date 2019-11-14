import random

class Road:

    def __init__(self, maxspeed=0, name=0, trafficjamssize=0,lenght=0,  trafficjamsspeed=0, accident=0, winding=0, toll=0, wild=0, stop=0, tunnel=0, bridge=0,montaine=0):
        """

        :param maxspeed: vitesse max de la route
        :param name: nom de la route
        :param trafficjamssize: longueur du bouchon
        :param lenght: taille de la route
        :param trafficjamsspeed: vitesse dans le bouchons
        :param accident: nb d'accident
        :param winding: % de route sinueuse
        :param toll:
        :param wild: si on est en campagne
        :param stop: nb de stop ou feu
        :param tunnel: nb de tunnel
        :param bridge: nb de pont
        :param montaine: altitude de la route
        """
        self.length=lenght
        self.maxSpeed = maxspeed
        self.trafficJamsSize = trafficjamssize
        if trafficjamsspeed >= self.maxSpeed:
            self.trafficJamsSize = 0
        self.trafficJamsSpeed = trafficjamsspeed
        self.accident = accident
        self.winding = winding
        #self.animals = animals
        self.toll = toll
        self.wild = wild
        self.name = name
        self.stop=stop
        self.tunnel = tunnel
        self.bridge=bridge
        self.montaine=montaine


    def create_rand(self,name,lenght): # fonction qui  créé aleatoirement une route
        self.name = name
        self.maxSpeed = random.randint(0, 200)
        if lenght==0:
            self.length = random.randint(0, 100)
        else :
            self.length=lenght
        self.trafficJamsSize = random.randint(0, lenght)
        self.trafficJamsSpeed = random.randint(1, 200)
        if self.trafficJamsSpeed >= self.maxSpeed:
            self.trafficJamsSize = 0
        self.accident=random.randint(0, 2)
        self.winding = random.randint(0, 100)
        self.wild=random.randint(0, 1)
        self.stop=random.randint(0, 10)
        self.bridge = random.randint(0, 1)
        self.tunnel = random.randint(0, 1)
        self.montaine = random.randint(0, 1000)

