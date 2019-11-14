import math
import random
from collections import defaultdict
from copy import deepcopy

import node
import road

class Graph:
    def __init__(self):
        self.node=[]
        self.network = []

    def create_rand(self,nb_node): # creation d'un reseau random
        for i in range(0, nb_node): #creation du reseaux vie
            self.network.append(nb_node*[0])
        for j in range(0,nb_node): # creation des neuds
            my_node=node.Node()
            my_node.creat_rand(j)
            self.node.append(deepcopy(my_node))
        for nodeA in self.node: # parcourt des neus pour les relier entre eux
            for nodeB in self.node:
                if nodeA!=nodeB:
                    if self.network[nodeA.name][nodeB.name]==0:# check si elles sont deja relié
                        if random.randint(0,10)>4:
                            lenght = round(math.sqrt((nodeA.latitude - nodeB.latitude) ** 2 + (
                                        nodeA.longitude - nodeB.longitude) ** 2))  # calcule de la distance entre les routes
                            my_road = road.Road()
                            my_road.create_rand(str(nodeA.name) + " to" + str(nodeB.name), lenght)
                            self.network[nodeA.name][nodeB.name] = my_road
                            self.network[nodeB.name][nodeA.name] = my_road



