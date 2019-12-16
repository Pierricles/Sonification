from copy import deepcopy

import Plus_cour_chemin as Dj

def find_fastest(my_graph, debut, fin):
    size, way = Dj.dij_rec(my_graph.network, debut, fin)
    if size != False:
        path_node = []
        path_roade = []
        for i in range(len(way)):
            path_node.append(my_graph.node[way[i]])
            if way[i] != fin:
                path_roade.append(my_graph.network[way[i]][way[i + 1]])

        return path_node
    else:
        return False


def YenKSP(my_graph, source, sink, K):
    old_graph=deepcopy(my_graph)
    way = find_fastest(my_graph,source, sink)
    a=[]
    a.append(way)
    b=[]
    remove_edge=[]
    for k in range(1,K):
        for i in range(0,len(a[k-1])-1):
            spur_node=a[k-1][i]
            root_path=[]
            for node in range(len(a[k-1])):
                if node<=i:
                    root_path.append(a[k-1][node])

            for p in a:
                isroot_path=True
                for j in range(0,i):
                    if root_path[j]!=p[j]:
                        isroot_path=False
                if isroot_path and p[i].name!=sink:
                    if my_graph.network[p[i].name].get(p[i + 1].name,False):
                        remove_edge.append(my_graph.network[p[i].name][p[i + 1].name])
                        del my_graph.network[p[i].name][p[i + 1].name]
                    if my_graph.network[p[i + 1].name].get(p[i].name, False):
                        remove_edge.append(my_graph.network[p[i + 1].name][p[i].name])
                        del my_graph.network[p[i+1].name][p[i].name]


            for root_path_node in root_path:
                if root_path_node!=spur_node :
                    for node in my_graph.network:
                        if my_graph.network[root_path_node.name].get(node,False):
                            remove_edge.append(my_graph.network[root_path_node.name][node])
                            del my_graph.network[root_path_node.name][node]

                        if my_graph.network[node].get(root_path_node.name,False):
                            remove_edge.append(my_graph.network[node][root_path_node.name])
                            del my_graph.network[node][root_path_node.name]


            spur_path=find_fastest(my_graph,spur_node.name, sink)
            if spur_path==False:
                print("no way")
            total_path=root_path+spur_path
            del total_path[i]
            b.append(total_path)
            for h in remove_edge:
                my_graph.network[h.start][h.end]=h
            remove_edge=[]
        if len(b) == 0:
            break
        quick_sort(b,0,len(b)-1,my_graph.network)
        a.append(b[0])
        suppr=b[0]
        i=0
        while i < len(b):
            if b[i] == suppr:
                del b[i]
            else :i+=1



    return a

def partition(array, start, end,graph):
    pivot = calc_length(array[start],graph)
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and calc_length(array[high],graph) >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and calc_length(array[low],graph)<= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end,graph):
    if start >= end:
        return

    p = partition(array, start, end,graph)
    quick_sort(array, start, p-1,graph)
    quick_sort(array, p+1, end,graph)

def calc_length(way,graph):
    length=0
    for i in range(len(way[:-1])):
        try:
            length+=graph[way[i].name][way[i+1].name].length
        except:print('error')

    return length