from graphlibrary import digraph
from graphlibrary import graph
from graphlibrary.exceptions import *


def dijkstra(G, start, weight='weight'):
    """
    Compute shortest path length between satrt
    and all other reachable nodes for a weight graph.
    return -> ({vertex: weight form start, }, {vertex: predeseccor, })
    """
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    visited = {start: 0}
    path = {}
    vertices = set(G.vertices.keys())
    while vertices:
        min_vertex = None
        for vertex in vertices:
            if vertex in visited:
                if min_vertex is None or visited[vertex] < visited[min_vertex]:
                    min_vertex = vertex
        if min_vertex is None:
            break
        vertices.remove(min_vertex)
        current_weight = visited[min_vertex]
        for edge in G.vertices[min_vertex]:
            edge_weight = current_weight + G.edges[(min_vertex, edge)][weight]
            if edge not in visited or edge_weight < visited[edge]:
                visited[edge] = edge_weight
                path[edge] = min_vertex
    return visited, path


def dijkstra_single_path_length(G, start, end):
    """
    Compute shortest path length between satrt
    and end for a weight graph. return -> (length, [path])
    """
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    if end not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (end,))
    dijkstra_data = dijkstra(G, start)
    length = dijkstra_data[0][end]
    path = [end]
    current = end
    while current is not start:
        for vertex in dijkstra_data[1]:
            if vertex is current:
                path.append(dijkstra_data[1][vertex])
                current = dijkstra_data[1][vertex]
                break
    return length, path
