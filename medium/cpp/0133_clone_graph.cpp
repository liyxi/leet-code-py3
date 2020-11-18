/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

#include <map>

class Solution {

public:
    void extract_graph(
        std::map<int, vector<int>> graph,
        Node* node
    ) {
        vector<int> target;
        graph[node->val] = target;
    }

public:
    Node* build_graph() {
        Node* new_node = new Node();
        return new_node;
    }

public:
    Node* cloneGraph(Node* node) {
        /* return NULL for empty graph */
        if (node == NULL) {
            return NULL;
        }

        /* copy graph if not empty */
        std::map<int, vector<int>> graph;
        Node* new_node = new Node();
        return new_node;
    }
};
