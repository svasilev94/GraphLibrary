from exceptions import *


class Graph:
    """
    Class for undirected graphs
    """
    vertices = dict
    edges = dict

    def __init__(self):
        """
        Initialize undirected graph
        vertices dictionary -> {u: [neigbours], }
        edges dictionary -> {(u;v): {data: 'info', }, }
        vertex attributes dictionary -> {u: {data: 'info', }, }
        """
        self.vertices = {}
        self.edges = {}
        self.nodes = {}

    def __iter__(self):
        """
        Iterate over the vertices -> for n in G
        """
        return iter(self.vertices)

    def __contains__(self, vertex):
        """
        Check if vertex is in G.vertices -> vertex in G
        """
        try:
            return vertex in self.vertices
        except:
            return False

    def __len__(self):
        """
        Return the number of vertices -> len(G)
        """
        return len(self.vertices)

    def __getitem__(self, vertex):
        """
        Return a dict of neighbors of vertex -> G[vertex]
        """
        return self.vertices[vertex]

    def add_vertex(self, vertex, **attr):
        """
        Add vertex and update vertex attributes
        """
        self.vertices[vertex] = []
        if attr:
            self.nodes[vertex] = attr

    def add_edge(self, u, v, **attr):
        """
        Add an edge between vertices u and v and update edge attributes
        """
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        vertex = (u, v)
        self.edges[vertex] = {}
        if attr:
            self.edges[vertex].update(attr)
        self.vertices[u].append(v)
        self.vertices[v].append(u)

    def remove_vertex(self, vertex):
        """
        Remove vertex from G
        """
        try:
            self.vertices.pop(vertex)
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

    def remove_edge(self, u, v):
        """
        Remove the edge between vertices u and v
        """
        try:
            self.edges.pop((u, v))
        except KeyError:
            raise GraphInsertError("Edge %s-%s doesn't exist." % (u, v))
        self.vertices[u].remove(v)
        self.vertices[v].remove(u)

    def is_edge(self, u, v):
        """
        Check if edge between u and v exist
        """
        try:
            return (u, v) in self.edges
        except:
            return False

    def degree(self, vertex):
        """
        Return the degree of a vertex
        """
        try:
            return len(self.vertices[vertex])
        except KeyError:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))

    def is_directed(self):
        """
        Return True if graph is directed, False otherwise
        """
        return False
