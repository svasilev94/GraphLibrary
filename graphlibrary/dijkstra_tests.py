import unittest
import dijkstra
import digraph
import graph


G = digraph.DiGraph()
G.vertices = {1: [2, 3, 4], 2: [7], 3: [2, 5, 6],
              4: [], 5: [], 6: [], 7: []}
G.edges = {(1, 2): {'weight': 500}, (1, 3): {'weight': 100},
           (1, 4): {'weight': 300}, (3, 2): {'weight': 200},
           (2, 7): {'weight': 300}, (3, 5): {'weight': 200},
           (3, 6): {'weight': 100}}
G.nodes = {}


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        test = ({1: 0, 2: 300, 3: 100, 4: 300, 5: 300, 6: 200, 7:600},
                {2: 3, 3: 1, 4: 1, 5: 3, 6: 3, 7: 2})
        self.assertEqual(dijkstra.dijkstra(G, 1), test)
        self.assertRaises(dijkstra.GraphInsertError, dijkstra.dijkstra, G, 9)

    def test_dijkstra_single_path_length(self):
        self.assertEqual(dijkstra.dijkstra_single_path_length(G, 1, 5),
                        (300, [5, 3, 1]))
        self.assertRaises(dijkstra.GraphInsertError,
                          dijkstra.dijkstra_single_path_length, G, 9, 5)
        self.assertRaises(dijkstra.GraphInsertError,
                          dijkstra.dijkstra_single_path_length, G, 1, 9)


if __name__ == '__main__':
    unittest.main()