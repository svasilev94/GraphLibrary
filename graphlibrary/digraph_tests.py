import unittest

from graphlibrary import digraph

G = digraph.DiGraph()
G.vertices = {1: [3], 2: [3, 4], 3: [1, 2, 4], 4: [2, 3]}
G.edges = {(1, 3): [], (2, 3): [], (2, 4): [], (3, 4): []}
G.nodes = {}
G.pred = {1: [], 2: [3], 3: [1], 4: [2, 3]}
G.succ = {1: [3], 2: [4], 3: [2, 4], 4: []}


class TestDiGraph(unittest.TestCase):

    def test_add_vertex(self):
        G.add_vertex(5)
        self.assertTrue(5 in G)
        G.add_vertex(6, weight='50')
        self.assertTrue(6 in G)
        self.assertEqual(G.nodes[6], {'weight': '50'})

    def test_add_edge(self):
        G.add_edge(3, 5)
        self.assertTrue((3, 5) in G.edges)
        self.assertTrue(3 in G.pred[5])
        self.assertTrue(3 in G.pred[5])
        self.assertTrue(5 in G.succ[3])
        G.add_edge(5, 6, weight='50')
        self.assertTrue((5, 6) in G.edges)
        self.assertEqual(G.edges[(5, 6)], {'weight': '50'})
        self.assertTrue(5 in G.pred[6])
        self.assertTrue(6 in G.succ[5])

    def test_remove_vertex(self):
        G.remove_vertex(4)
        self.assertFalse(4 in G.vertices)
        self.assertRaises(digraph.GraphInsertError, G.remove_vertex, 9)
        self.assertFalse(4 in G.succ[2])
        self.assertFalse((2, 4) in G.edges)

    def test_remove_edge(self):
        G.remove_edge(1, 3)
        self.assertFalse((1, 3) in G.edges)
        self.assertRaises(digraph.GraphInsertError, G.remove_edge, 1, 2)
        self.assertFalse(1 in G.pred[3])
        self.assertFalse(3 in G.succ[1])

    def test_has_successor(self):
        self.assertTrue(G.has_successor(3, 2))
        self.assertFalse(G.has_successor(2, 3))
        self.assertRaises(digraph.GraphInsertError, G.has_successor, 10, 11)

    def test_has_predecessor(self):
        self.assertTrue(G.has_predecessor(2, 3))
        self.assertFalse(G.has_predecessor(3, 2))
        self.assertRaises(digraph.GraphInsertError, G.has_predecessor, 10, 11)

    def test_in_degree(self):
        self.assertEqual(G.in_degree(4), 2)
        self.assertRaises(digraph.GraphInsertError, G.in_degree, 10)

    def test_out_degree(self):
        self.assertEqual(G.out_degree(3), 3)
        self.assertRaises(digraph.GraphInsertError, G.in_degree, 10)


if __name__ == '__main__':
    unittest.main()
