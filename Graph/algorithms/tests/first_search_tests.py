import unittest
import first_search
import digraph
import graph


EmptyG = graph.Graph()
G = graph.Graph()
G.vertices = {1: [2, 3, 4], 2: [1, 3, 7], 3: [1, 2, 5, 6],
              4: [1], 5: [3], 6: [3], 7: [2]}
G.edges = {(1, 2): [], (1, 3): [], (1, 4): [], (2, 3): [],
           (2, 7): [], (3, 5): [], (3, 6): []}
G.nodes = {}


class TestFirst_Search(unittest.TestCase):

    def test_BFS(self):
        test = {1: None, 2: 1, 3: 1, 4: 1, 5: 3, 6: 3, 7: 2}
        self.assertEqual(first_search.BFS(G, 1), test)
        self.assertRaises(first_search.GraphInsertError,
                          first_search.BFS, G, 9)

    def test_BFS_Tree(self):
        test = {1: [2, 3, 4], 2: [7], 3: [5, 6], 4: [], 5: [], 6: [], 7: []}
        self.assertEqual(first_search.BFS_Tree(G, 1).vertices, test)
        self.assertRaises(first_search.GraphInsertError,
                          first_search.BFS_Tree, G, 9)

    def test_DFS(self):
        test = {1: (None, 1, 14), 2: (1, 2, 11), 3: (2, 3, 8), 4: (1, 12, 13),
                5: (3, 4, 5), 6: (3, 6, 7), 7: (2, 9, 10)}
        self.assertEqual(first_search.DFS(G), test)
        self.assertRaises(first_search.GraphInsertError,
                          first_search.DFS, EmptyG)

    def test_DFS_Tree(self):
        test = {1: [2, 4], 2: [3, 7], 3: [5, 6], 4: [], 5: [], 6: [], 7: []}
        self.assertEqual(first_search.DFS_Tree(G).vertices, test)
        self.assertRaises(first_search.GraphInsertError,
                          first_search.DFS_Tree, EmptyG)


if __name__ == '__main__':
    unittest.main()
