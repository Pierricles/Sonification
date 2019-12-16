import random
from copy import deepcopy

import node
import road
import Graph
import Plus_cour_chemin as Dj
from Yen import YenKSP



def find_fastest(my_graph, debut, fin):
    size, way = Dj.dij_rec(my_graph.network, debut, fin)
    if size != False:
        path_node = []
        path_roade = []
        for i in range(len(way)):
            path_node.append(my_graph.node[way[i]])
            if way[i] != fin:
                path_roade.append(my_graph.network[way[i]][way[i + 1]])

        return path_node, path_roade, size
    else:
        return False, False, False


def find_min(All_way):
    min = 4 * [0]
    min[2] = 10000
    for i in All_way:
        if i[2] < min[2] and i[3]:
            min = deepcopy(i)
    min[3] = False
    return min


def isin(All_way, way):
    for i in All_way:
        if i[0] == way:
            return True


my_graph = Graph.Graph()
All_way = []
my_graph.create_rand(100)
debut = 0
fin = 9
path=YenKSP(my_graph, debut, fin,K=10)
path_all_road=[]
for j in path:
    path_roade = []
    for i in range(len(j)):
        if j[i].name != fin:
            path_roade.append(my_graph.network[j[i].name][j[i + 1].name])
    path_all_road.append(path_roade)

'''
i = 0
a, best, size = find_fastest(my_graph, debut, fin)
if a != False:
    All_way.append([])
    All_way[i].append(a)
    All_way[i].append(best)
    All_way[i].append(size)
    All_way[i].append(True)
    i += 1
    while i < 20:
        best = find_min(All_way)
        for r in best[1]:
            new_graph = deepcopy(my_graph)
            del new_graph.network[r.end][r.start]
            del new_graph.network[r.start][r.end]
            a, b, size = find_fastest(new_graph, debut, fin)
            if a != False and not isin(All_way, a):
                All_way.append([])
                All_way[i].append(a)
                All_way[i].append(b)
                All_way[i].append(size)
                All_way[i].append(True)
                i += 1

else:
    print("no way")
'''
fichier = open("data_way.txt", "w")

for i in path_all_road:
    total_length = 0
    mean_speed = 0
    total_trafficJamsSize = 0
    mean_trafficJamsSpeed = 0
    total_accident = 0
    mean_winding = 0
    total_toll = 0
    wild = False
    total_stop = 0
    total_tunnel = 0
    total_bridge = 0
    mean_montaine = 0
    for j in i:
        total_length += j.length
        mean_speed += j.maxSpeed * j.length
        total_trafficJamsSize += j.trafficJamsSize
        mean_trafficJamsSpeed += j.trafficJamsSpeed
        total_accident += j.accident
        mean_winding += j.winding * j.length
        total_toll += j.toll
        total_stop += j.stop
        total_tunnel += j.tunnel
        total_bridge += j.tunnel
        mean_montaine += j.montaine * j.length
    mean_speed = mean_speed / total_length
    mean_trafficJamsSpeed = mean_trafficJamsSpeed / (total_trafficJamsSize+1)
    mean_winding = mean_winding / total_length
    mean_montaine = mean_montaine / total_length
    fichier.write(
        str(round(total_length)) + " " + str(round(mean_speed)) + " " + str(round(total_trafficJamsSize)) + " " + str(
            round(mean_trafficJamsSpeed)) + " " + str(round(total_accident)) + " " + str(
            round(mean_winding)) + " " + str(round(total_toll)) + " " + str(round(total_stop)) + " " + str(
            round(total_tunnel)) + " " + str(round(total_bridge)) + " " + str(round(mean_montaine))+"\n")

fichier.close()
print(0)
