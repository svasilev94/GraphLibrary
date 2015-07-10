import unittest
import prim
import digraph
import graph


G = graph.Graph()
G.vertices = {1: [2, 3, 4], 2: [7], 3: [2, 5, 6],
              4: [], 5: [], 6: [], 7: [], 8: []}
G.edges = {(1, 2): {'weight': 500}, (1, 3): {'weight': 100},
           (1, 4): {'weight': 300}, (3, 2): {'weight': 200},
           (2, 7): {'weight': 300}, (3, 5): {'weight': 200},
           (3, 6): {'weight': 100}}
G.nodes = {}

V = graph.Graph()
V.vertices = {1: [2, 3, 4], 2: [7], 3: [2, 5, 6],
              4: [], 5: [], 6: [], 7: []}
V.edges = {(1, 2): {'weight': 500}, (1, 3): {'weight': 100},
           (1, 4): {'weight': 300}, (3, 2): {'weight': 200},
           (2, 7): {'weight': 300}, (3, 5): {'weight': 200},
           (3, 6): {'weight': 100}}
V.nodes = {}


class TestPrim(unittest.TestCase):

    def test_connected_components(self):
        self.assertEqual(prim.connected_components(G),
                         [{1, 2, 3, 4, 5, 6, 7}, {8}])

    def test_prim(self):
        self.assertEqual(prim.prim(V, 1),
                         {1: None, 2: 3, 3: 1, 4: 1, 5: 3, 6: 3, 7: 2})
        self.assertRaises(prim.GraphInsertError, prim.prim, G, 1)
        self.assertRaises(prim.GraphInsertError, prim.prim, G, 9)

    def test_prim_MST(self):
        self.assertEqual(prim.prim_MST(V, 1).vertices,
                         {1: [3, 4], 2: [7], 3: [2, 5, 6],
                          4: [], 5: [], 6: [], 7: []})
        self.assertRaises(prim.GraphInsertError, prim.prim, V, 9)


if __name__ == '__main__':
    unittest.main()
