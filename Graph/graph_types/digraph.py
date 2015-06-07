from graph import *
from exceptions import *


# Class for directed graphs
class DiGraph(Graph):

    # Initialize directed graphs
    def __init__(self):
        # vertices dictionary -> {u: [neigbours], }
        self.vertices = {}
        # edges dictionary -> {(u, v): {data: 'info', }, }
        self.edges = {}
        # vertex attributes dictionary -> {u: {data: 'info', }, }
        self.nodes = {}
        # vertex predecessors dictionary -> {u: [predecessors], }
        self.pred = {}
        # vertex successors dictionary -> {u: [successors], }
        self.succ = {}

    # Add vertex and update vertex attributes
    def add_vertex(self, vertex, **attr):
        self.vertices[vertex] = []
        if attr:
            self.nodes[vertex] = attr
        self.pred[vertex] = []
        self.succ[vertex] = []

    # Add an edge from u to v and update edge attributes
    def add_edge(self, u, v, **attr):
        if u not in self.vertices:
            self.vertices[u] = []
            self.pred[u] = []
            self.succ[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
            self.pred[v] = []
            self.succ[v] = []
        vertex = (u, v)
        self.edges[vertex] = {}
        self.edges[vertex].update(attr)
        self.vertices[u].append(v)
        self.pred[v].append(u)
        self.succ[u].append(v)

    # Remove vertex from G
    def remove_vertex(self, vertex):
        try:
            self.vertices.pop(vertex)
            self.succ.pop(vertex)
        except KeyError:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))
        if vertex in self.nodes:
            self.nodes.pop(vertex)
        for element in self.vertices:
            if vertex in self.vertices[element]:
                self.vertices[element].remove(vertex)
        edges = []  # List for edges that include vertex
        for element in self.edges:
            if vertex in element:
                edges.append(element)
        for element in edges:
            del self.edges[element]
        for element in self.pred:
            if vertex in self.pred[element]:
                self.pred[element].remove(vertex)
        for element in self.succ:
            if vertex in self.succ[element]:
                self.succ[element].remove(vertex)

    # Remove the edge from u to v
    def remove_edge(self, u, v):
        try:
            self.edges.pop((u, v))
        except KeyError:
            raise GraphInsertError("Edge %s-%s doesn't exist." % (u, v))
        self.vertices[u].remove(v)
        self.pred[v].remove(u)
        self.succ[u].remove(v)

    # Return True if graph is directed, False otherwise
    def is_directed(self):
        return True

    # Check if vertex u has successor v
    def has_successor(self, u, v):
        if u not in self.vertices:
            raise GraphInsertError("Vertex %s doesn't exist." % (u,))
        return (u in self.succ and v in self.succ[u])

    # Check if vertex u has predecessor v
    def has_predecessor(self, u, v):
        if u not in self.vertices:
            raise GraphInsertError("Vertex %s doesn't exist." % (u,))
        return(u in self.pred and v in self.pred[u])

    # Return the in-degree of a vertex
    def in_degree(self, vertex):
        try:
            return len(self.pred[vertex])
        except:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))

    # Return the out-degree of a vertex
    def out_degree(self, vertex):
        try:
            return len(self.succ[vertex])
        except:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))
