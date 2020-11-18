"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def extract_graph(self, graph: dict, node: 'Node'):
        graph[node.val] = []
        for n_ in node.neighbors:
            graph[node.val].append(n_.val)
            if n_.val not in graph:
                self.extract_graph(graph, n_)

    def build_graph(self, graph: dict) -> 'Node':
        nodes = {k_: Node(k_) for k_ in graph}
        for k_ in graph:
            for neighbor_ in graph[k_]:
                nodes[k_].neighbors.append(nodes[neighbor_])
        return nodes

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        graph = {}
        self.extract_graph(graph, node)
        nodes = self.build_graph(graph)
        return nodes[1]
