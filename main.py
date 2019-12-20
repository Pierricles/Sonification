
import Graph
from Yen import YenKSP


my_graph = Graph.Graph()
my_graph.create_rand(100)#generation d'un graph de 100 noeuds
debut = 0
fin = 9
path=YenKSP(my_graph, debut, fin,K=10) # algorithme de Yen
path_all_road=[]
for j in path:# creation d'un chemin d'arc a partire d'un chemin de noeuds
    path_roade = []
    for i in range(len(j)):
        if j[i].name != fin:
            path_roade.append(my_graph.network[j[i].name][j[i + 1].name])
    path_all_road.append(path_roade)


fichier = open("data_way.txt", "w")# ouverture du fichier pour l'ecriture


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
        str(round(total_length)) + " " + str(round(mean_speed/total_length)) + " " + str(round(total_trafficJamsSize)) + " " + str(round(total_toll))  + " " + str(
            round(total_tunnel)) +"\n")

fichier.close()
print(0)
