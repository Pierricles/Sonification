import math
import random
from collections import defaultdict
from copy import deepcopy

import node
import road

class Graph:
    def __init__(self):
        self.node=[]
        self.network = {}

    def create_rand(self,nb_node): # creation d'un reseau random
        #for i in range(0, nb_node): #creation du reseaux vie
         #   self.network.append(nb_node*[0])
        for j in range(0,nb_node): # creation des neuds
            my_node=node.Node()
            my_node.creat_rand(j)
            self.node.append(deepcopy(my_node))
        for nodeA in self.node: # parcourt des neuds pour les relier entre eux
            if not self.network.get(nodeA.name, False):
                self.network[nodeA.name]= {}
            for nodeB in self.node:
                if not self.network.get(nodeB.name,False):
                    self.network[nodeB.name] = {}
                if nodeA!=nodeB:
                    #if self.network[nodeA.name][nodeB.name]==0:# check si elles sont deja relié
                    if not self.network[nodeA.name].get(nodeB.name,False) :  # check si elles sont deja relié
                        if random.randint(0,100)>99:
                            lenght = round(math.sqrt((nodeA.latitude - nodeB.latitude) ** 2 + (
                                        nodeA.longitude - nodeB.longitude) ** 2))  # calcule de la distance entre les routes
                            my_road = road.Road()
                            my_road.create_rand(str(nodeA.name) + " to " + str(nodeB.name), lenght,int(nodeA.name),int(nodeB.name))
                            self.network[nodeA.name][nodeB.name]= my_road
                            self.network[nodeB.name][nodeA.name]= my_road

        for nodeA in self.node:# on verifie que aucun noeud n'est isolé

            if len (self.network[nodeA.name])==0:
                # si un noeud est isolé on le relie a un noeud random different de lui meme
                rnd = random.randint(0, nb_node-1)
                while rnd == nodeA:
                    rnd = random.randint(0, nb_node)
                nodeB = self.node[rnd]
                lenght = round(math.sqrt((nodeA.latitude - nodeB.latitude) ** 2 + (
                        nodeA.longitude - nodeB.longitude) ** 2))  # calcule de la distance entre les routes
                my_road = road.Road()
                my_road.create_rand(str(nodeA.name) + " to" + str(nodeB.name), lenght,int(nodeA.name),int(nodeB.name))
                self.network[nodeA.name][nodeB.name] = my_road
                self.network[nodeB.name][nodeA.name] = my_road







