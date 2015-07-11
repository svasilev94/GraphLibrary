import unittest

from graphlibrary import graph


G = graph.Graph()
G.vertices = {1: [3], 2: [3, 4], 3: [1, 2, 4], 4: [2, 3]}
G.edges = {(1, 3): [], (2, 3): [], (2, 4): [], (3, 4): []}
G.nodes = {}


class TestGraph(unittest.TestCase):

    def test_contains(self):
        self.assertTrue(1 in G)
        self.assertFalse(5 in G)

    def test_len(self):
        K = graph.Graph()
        K.vertices = {1: [3], 2: [3, 4], 3: [1, 2, 4], 4: [2, 3]}
        K.edges = {(1, 3): [], (2, 3): [], (2, 4): [], (3, 4): []}
        K.nodes = {}
        self.assertEqual(len(K), 4)
        self.assertNotEqual(len(K), 5)

    def test_get_item(self):
        self.assertIs(G[2], G.vertices[2])
        self.assertIsNot(G[3], G.vertices[4])

    def test_add_vertex(self):
        G.add_vertex(6)
        self.assertTrue(6 in G)
        G.add_vertex(7, weight='50')
        self.assertTrue(7 in G)
        self.assertEqual(G.nodes[7], {'weight': '50'})

    def test_add_edge(self):
        G.add_edge(6, 7)
        self.assertTrue((6, 7) in G.edges)
        G.add_edge(1, 2, weight='50')
        self.assertTrue((1, 2) in G.edges)
        self.assertEqual(G.edges[(1, 2)], {'weight': '50'})

    def test_remove_vertex(self):
        G.remove_vertex(4)
        self.assertFalse(4 in G.vertices)
        self.assertFalse((2, 4) in G.edges)
        self.assertRaises(graph.GraphInsertError, G.remove_vertex, 9)

    def test_remove_edge(self):
        G.remove_edge(1, 2)
        self.assertFalse((1, 2) in G.edges)
        self.assertRaises(graph.GraphInsertError, G.remove_edge, 1, 8)

    def test_is_edge(self):
        self.assertTrue(G.is_edge(2, 3))
        self.assertFalse(G.is_edge(1, 4))

    def test_degree(self):
        K = graph.Graph()
        K.vertices = {1: [3], 2: [3, 4], 3: [1, 2, 4], 4: [2, 3]}
        K.edges = {(1, 3): [], (2, 3): [], (2, 4): [], (3, 4): []}
        K.nodes = {}
        self.assertEqual(K.degree(3), 3)
        self.assertRaises(graph.GraphInsertError, G.degree, 5)


if __name__ == '__main__':
    unittest.main()
