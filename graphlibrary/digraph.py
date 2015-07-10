from graph import *
from exceptions import *


class DiGraph(Graph):
    """
    Class for directed graphs
    """

    def __init__(self):
        """
        Initialize directed graphs
        vertices dictionary -> {u: [neigbours], }
        edges dictionary -> {(u, v): {data: 'info', }, }
        vertex attributes dictionary -> {u: {data: 'info', }, }
        vertex predecessors dictionary -> {u: [predecessors], }
        vertex successors dictionary -> {u: [successors], }
        """
        self.vertices = {}
        self.edges = {}
        self.nodes = {}
        self.pred = {}
        self.succ = {}

    def add_vertex(self, vertex, **attr):
        """
        Add vertex and update vertex attributes
        """
        self.vertices[vertex] = []
        if attr:
            self.nodes[vertex] = attr
        self.pred[vertex] = []
        self.succ[vertex] = []

    def add_edge(self, u, v, **attr):
        """
        Add an edge from u to v and update edge attributes
        """
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

    def remove_vertex(self, vertex):
        """
        Remove vertex from G
        """
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

    def remove_edge(self, u, v):
        """
        Remove the edge from u to v
        """
        try:
            self.edges.pop((u, v))
        except KeyError:
            raise GraphInsertError("Edge %s-%s doesn't exist." % (u, v))
        self.vertices[u].remove(v)
        self.pred[v].remove(u)
        self.succ[u].remove(v)

    def is_directed(self):
        """
        Return True if graph is directed, False otherwise
        """
        return True

    def has_successor(self, u, v):
        """
        Check if vertex u has successor v
        """
        if u not in self.vertices:
            raise GraphInsertError("Vertex %s doesn't exist." % (u,))
        return (u in self.succ and v in self.succ[u])

    def has_predecessor(self, u, v):
        """
        Check if vertex u has predecessor v
        """
        if u not in self.vertices:
            raise GraphInsertError("Vertex %s doesn't exist." % (u,))
        return(u in self.pred and v in self.pred[u])

    def in_degree(self, vertex):
        """
        Return the in-degree of a vertex
        """
        try:
            return len(self.pred[vertex])
        except:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))

    def out_degree(self, vertex):
        """
        Return the out-degree of a vertex
        """
        try:
            return len(self.succ[vertex])
        except:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))
