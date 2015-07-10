import digraph
import graph
from queue import Queue
from exceptions import *


def connected_components(G):
    """
    Check if G is connected and return list of sets. Every
    set contains all vertices in one connected component.
    """
    result = []
    vertices = set(G.vertices)
    while vertices:
        n = vertices.pop()
        group = {n}
        queue = Queue()
        queue.put(n)
        while not queue.empty():
            n = queue.get()
            neighbors = set(G.vertices[n])
            neighbors.difference_update(group)
            vertices.difference_update(neighbors)
            group.update(neighbors)
            for element in neighbors:
                queue.put(element)
        result.append(group)
    return result


def popmin(pqueue, lowest):
    lowest = 1000
    keylowest = None
    for element in pqueue:
        if pqueue[element] < lowest:
            lowest = pqueue[element]
            keylowest = element
    del pqueue[keylowest]
    return keylowest


def prim(G, start, weight='weight'):
    """
    Algorithm for finding a minimum spanning
    tree for a weighted undirected graph.
    """
    if len(connected_components(G)) != 1:
        raise GraphInsertError("Prim algorithm work with connected graph only")
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    pred = {}
    key = {}
    pqueue = {}
    lowest = 0
    for edge in G.edges:
        if G.edges[edge][weight] > lowest:
            lowest = G.edges[edge][weight]
    for vertex in G.vertices:
        pred[vertex] = None
        key[vertex] = 2 * lowest
    key[start] = 0
    for vertex in G.vertices:
        pqueue[vertex] = key[vertex]
    while pqueue:
        current = popmin(pqueue, lowest)
        for neighbor in G.vertices[current]:
            if (neighbor in pqueue and
                    G.edges[(current, neighbor)][weight] < key[neighbor]):
                pred[neighbor] = current
                key[neighbor] = G.edges[(current, neighbor)][weight]
                pqueue[neighbor] = G.edges[(current, neighbor)][weight]
    return pred


def prim_MST(G, start):
    """
    Return an oriented tree constructed from prim algorithm starting at 'start'
    """
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    pred = prim(G, start)
    T = digraph.DiGraph()
    queue = Queue()
    queue.put(start)
    while queue.qsize() > 0:
        current = queue.get()
        for element in pred:
            if pred[element] == current:
                T.add_edge(current, element)
                queue.put(element)
    return T
