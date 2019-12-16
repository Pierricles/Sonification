from copy import deepcopy
from heapq import heappush, heappop
from itertools import count

import Plus_cour_chemin as Dj

def find_fastest(my_graph, debut, fin):
    size, way = Dj.dij_rec(my_graph, debut, fin)
    if size != False:
        path_roade = []
        path_node = []
        for i in range(len(way)):
            path_node.append(my_graph[way[i]])
            if way[i] != fin:
                path_roade.append(my_graph[way[i]][way[i + 1]])

        return size,  path_node
    else:
        return False, False


def k_shortest_paths(G, source, target, k=1, weight='weight'):
    """Returns the k-shortest paths from source to target in a weighted graph G.
    Parameters
    ----------
    G : NetworkX graph
    source : int
       Starting int
    target : int
       Ending int

    k : integer, optional (default=1)
        The number of shortest paths to find
    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight
    Returns
    -------
    lengths, paths : lists
       Returns a tuple with two lists.
       The first list stores the length of each k-shortest path.
       The second list stores each k-shortest path.
    Raises
    ------
    NetworkXNoPath
       If no path exists between source and target.
    Examples
    --------

    ([1, 2, 2, 2], [[0, 4], [0, 1, 4], [0, 2, 4], [0, 3, 4]])
    Notes
    ------
    Edge weight attributes must be numerical and non-negative.
    Distances are calculated as sums of weighted edges traversed.
    """
    if source == target:
        return [0], [[source]]
    length=[]
    path=[]
    for i in range(len(G)):
        size, way = find_fastest(G, source, i)

        length.append(size)
        path.append(way)

    lengths = [length[target]]
    paths = [path[target]]

    c = count()
    B = []
    G_original = G.copy()

    for i in range(1, k):
        for j in range(len(paths[-1]) - 1):
            spur_node = paths[-1][j]
            root_path = paths[-1][:j + 1]

            edges_removed = []
            for c_path in paths:
                if len(c_path) > j and root_path == c_path[:j + 1]:
                    u = c_path[j]
                    v = c_path[j + 1]
                    indice_u=u[next(iter(u))].start
                    indice_v=v[next(iter(v))].start
                    if G.get(indice_u, False) and G[indice_u].get(indice_v, False):
                        edge = G[indice_u][indice_v]
                        edges_removed.append(G[edge.start][edge.end])
                        edges_removed.append(G[edge.end][edge.start])
                        del G[edge.start][edge.end]
                        del G[edge.end][edge.start]


            for n in range(len(root_path) -1):
                node = root_path[n]
                # out-edges
                G_bis=deepcopy(G)
                indice_node=node[next(iter(node))].start
                for edge in (G_bis[indice_node]):
                    edges_removed.append(G[indice_node][edge])
                    edges_removed.append(G[edge][indice_node])
                    del G[indice_node][edge]
                    del G[edge][indice_node]

                    ''' if G.is_directed():
                    # in-edges
                    for u, v, edge_attr in G.in_edges_iter(node, data=True):
                        G.remove_edge(u, v)
                        edges_removed.append((u, v, edge_attr))'''
            spur_path_length = []
            spur_path = []
            for i in range(len(G)):
                size, way = find_fastest(G,spur_node[next(iter(spur_node))].start, i)

                spur_path_length.append(size)
                spur_path.append(way)
            #spur_path_length, spur_path = Dj.dij_rec(G, spur_node, target)
            if spur_path[target]!=False:
                if len(spur_path[target])!=0:
                    total_path = root_path[:-1] + spur_path[target]
                    total_path_length = get_path_length(G_original, root_path, weight) + spur_path_length[target]
                    heappush(B, (total_path_length, next(c), total_path))

            for e in edges_removed:
                G[e.start][e.end] = e


        if B:
            (l, _, p) = heappop(B)
            lengths.append(l)
            paths.append(p)
        else:
            break

    return lengths, paths


def get_path_length(G, path, weight='weight'):
    length = 0
    if len(path) >= 1:
        for i in path[0]:
            length += path[0][i].length

    return length
