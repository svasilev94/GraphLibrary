from exceptions import *


# Class for undirected graphs
class Graph:
    vertices = dict
    edges = dict

    # Initialize undirected graph
    def __init__(self):
        # vertices dictionary -> {u: [neigbours], }
        self.vertices = {}
        # edges dictionary -> {(u;v): {data: 'info', }, }
        self.edges = {}
        # vertex attributes dictionary -> {u: {data: 'info', }, }
        self.nodes = {}

    # Iterate over the vertices -> for n in G
    def __iter__(self):
        return iter(self.vertices)

    # Check if vertex is in G.vertices -> vertex in G
    def __contains__(self, vertex):
        try:
            return vertex in self.vertices
        except:
            return False

    # Return the number of vertices -> len(G)
    def __len__(self):
        return len(self.vertices)

    # Return a dict of neighbors of vertex -> G[vertex]
    def __getitem__(self, vertex):
        return self.vertices[vertex]

    # Add vertex and update vertex attributes
    def add_vertex(self, vertex, **attr):
        self.vertices[vertex] = []
        if attr:
            self.nodes[vertex] = attr

    # Add an edge between vertices u and v and update edge attributes
    def add_edge(self, u, v, **attr):
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

    # Remove vertex from G
    def remove_vertex(self, vertex):
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

    # Remove the edge between vertices u and v
    def remove_edge(self, u, v):
        try:
            self.edges.pop((u, v))
        except KeyError:
            raise GraphInsertError("Edge %s-%s doesn't exist." % (u, v))
        self.vertices[u].remove(v)
        self.vertices[v].remove(u)

    # Check if edge between u and v exist
    def is_edge(self, u, v):
        try:
            return (u, v) in self.edges
        except:
            return False

    # Return the degree of a vertex
    def degree(self, vertex):
        try:
            return len(self.vertices[vertex])
        except KeyError:
            raise GraphInsertError("Vertex %s doesn't exist." % (vertex,))

    # Return True if graph is directed, False otherwise
    def is_directed(self):
        return False
