import unittest
from ..\algorithms import paths
import digraph
import graph


G = graph.Graph()
G.vertices = {1: [2, 3, 4], 2: [1, 3, 7], 3: [1, 2, 5, 6],
              4: [1], 5: [3], 6: [3], 7: [2]}
G.edges = {(1, 2): [], (1, 3): [], (1, 4): [], (2, 3): [],
           (2, 7): [], (3, 5): [], (3, 6): []}
G.nodes = {}


class TestPaths(unittest.TestCase):

    def test_find_all_paths(self):
        self.assertEqual(paths.find_all_paths(G, 1, 3),
                         [[1, 2, 3], [1, 3]])
        self.assertEqual(paths.find_all_paths(G, 1, 1), [[1]])
        self.assertRaises(paths.GraphInsertError,
                          paths.find_all_paths, G, 1, 9)
        self.assertRaises(paths.GraphInsertError,
                          paths.find_all_paths, G, 9, 1)

    def test_find_shortest_path(self):
        self.assertEqual(paths.find_shortest_path(G, 1, 3), [1, 3])
        self.assertEqual(paths.find_shortest_path(G, 1, 1), [])
        self.assertRaises(paths.GraphInsertError,
                          paths.find_shortest_path, G, 1, 9)
        self.assertRaises(paths.GraphInsertError,
                          paths.find_shortest_path, G, 9, 1)


if __name__ == '__main__':
    unittest.main()
