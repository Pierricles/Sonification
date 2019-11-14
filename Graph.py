import math
from collections import defaultdict
from copy import deepcopy

import node
import road

class Graph:
    def __init__(self):
        self.node=[]
        self.network = []

    def create_rand(self,nb_node):
        for i in range(0, nb_node):
            self.network.append(nb_node*[0])
        for j in range(0,nb_node):
            my_node=node.Node()
            my_node.creat_rand(j)
            self.node.append(deepcopy(my_node))
        for nodeA in self.node:
            for nodeB in self.node:
                if nodeA!=nodeB:
                    if self.network[nodeA.name][nodeB.name]==0:
                        lenght=round(math.sqrt((nodeA.latitude-nodeB.latitude)**2+(nodeA.longitude-nodeB.longitude)**2))
                        my_road=road.Road()
                        my_road.create_rand(str(nodeA.name)+" to"+str(nodeB.name),lenght)
                        self.network[nodeA.name][nodeB.name]=my_road
                        self.network[nodeB.name][nodeA.name] = my_road


