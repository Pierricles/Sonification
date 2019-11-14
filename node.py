import random

class Node:
    distance = 0 #distance between node and end point
    latitude = 0
    longitude = 0
    name = ""

    def __init__(self, name=0, latitude=0, longitude=0, distance=0,):
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.name = name

    def creat_rand(self,name):
        self.name=name
        self.latitude=random.randint(0,100)
        self.longitude = random.randint(0, 100)


