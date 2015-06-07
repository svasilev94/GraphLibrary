import digraph
import graph
from queue import Queue
from exceptions import *


def connected_components(G):
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



G = digraph.DiGraph()
G.vertices = {1: [2, 3, 4], 2: [7], 3: [2, 5, 6],
              4: [], 5: [], 6: [], 7: [], 8: []}
G.edges = {(1, 2): {'weight': 500}, (1, 3): {'weight': 100},
           (1, 4): {'weight': 300}, (3, 2): {'weight': 200},
           (2, 7): {'weight': 300}, (3, 5): {'weight': 200},
           (3, 6): {'weight': 100}}
G.nodes = {}

#print(prim_MST(G, 1).vertices)

print(prim_MST(G, 1))