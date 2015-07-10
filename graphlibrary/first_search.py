import digraph
import graph
from exceptions import *
from queue import Queue


def BFS(G, start):
    """
    Algorithm for breadth-first searching the vertices of a graph.
    """
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    color = {}
    pred = {}
    dist = {}
    queue = Queue()
    queue.put(start)
    for vertex in G.vertices:
        color[vertex] = 'white'
        pred[vertex] = None
        dist[vertex] = 0
    while queue.qsize() > 0:
        current = queue.get()
        for neighbor in G.vertices[current]:
            if color[neighbor] == 'white':
                color[neighbor] = 'grey'
                pred[neighbor] = current
                dist[neighbor] = dist[current] + 1
                queue.put(neighbor)
        color[current] = 'black'
    return pred


def BFS_Tree(G, start):
    """
    Return an oriented tree constructed from bfs starting at 'start'.
    """
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    pred = BFS(G, start)
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


def DFS(G):
    """
    Algorithm for depth-first searching the vertices of a graph.
    """
    if not G.vertices:
        raise GraphInsertError("This graph have no vertices.")
    color = {}
    pred = {}
    reach = {}
    finish = {}

    def DFSvisit(G, current, time):
        color[current] = 'grey'
        time += 1
        reach[current] = time
        for vertex in G.vertices[current]:
            if color[vertex] == 'white':
                pred[vertex] = current
                time = DFSvisit(G, vertex, time)
        color[current] = 'black'
        time += 1
        finish[current] = time
        return time

    for vertex in G.vertices:
        color[vertex] = 'white'
        pred[vertex] = None
        reach[vertex] = 0
        finish[vertex] = 0
    time = 0
    for vertex in G.vertices:
        if color[vertex] == 'white':
            time = DFSvisit(G, vertex, time)
    # Dictionary for vertex data after DFS
    # -> vertex_data = {vertex: (predecessor, reach, finish), }
    vertex_data = {}
    for vertex in G.vertices:
        vertex_data[vertex] = (pred[vertex], reach[vertex], finish[vertex])
    return vertex_data


def DFS_Tree(G):
    """
    Return an oriented tree constructed from dfs.
    """
    if not G.vertices:
        raise GraphInsertError("This graph have no vertices.")
    pred = {}
    T = digraph.DiGraph()
    vertex_data = DFS(G)
    for vertex in vertex_data:
        pred[vertex] = vertex_data[vertex][0]
    queue = Queue()
    for vertex in pred:
        if pred[vertex] == None:
            queue.put(vertex)
    while queue.qsize() > 0:
        current = queue.get()
        for element in pred:
            if pred[element] == current:
                T.add_edge(current, element)
                queue.put(element)
    return T
