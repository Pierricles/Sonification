import node
import road
import Graph
import Plus_cour_chemin as Dj
my_graph=Graph.Graph()
my_graph.create_rand(100)
debut=0
fin=99
size, way = Dj.dij_rec(my_graph.network,debut,fin)
path_node=[]
path_roade=[]
for i in range(len(way)):
    path_node.append(my_graph.node[way[i]])
    if way[i]!=fin:
        path_roade.append(my_graph.network[way[i]][way[i+1]])

print(0)






