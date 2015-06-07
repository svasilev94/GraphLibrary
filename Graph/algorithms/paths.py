import digraph
import graph
from exceptions import *


# Find all paths between vertices start and end in graph.
def find_all_paths(G, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    if end not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (end,))
    paths = []
    for vertex in G.vertices[start]:
        if vertex not in path:
            newpaths = find_all_paths(G, vertex, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# Find shortest path between vertices start and end in undirectetd graph.
def find_shortest_path(G, start, end):
    if start == end:
        return []
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    if end not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (end,))
    paths = find_all_paths(G, start, end)
    shortest = list(G.vertices.keys())
    for path in paths:
        if len(path) < len(shortest):
            shortest = path
    return shortest
