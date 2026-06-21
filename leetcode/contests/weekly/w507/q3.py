from typing import Optional, List

class Node:
    def __init__(self,position: int = 0, weight: int = 0, label: str = "", next: Optional["Node"] = None):
        self.position = position
        self.weight = weight
        self.label = label
        self.next = next
        # p0 to1 wg1 a    p1 to2 wg1 a    p0 to2 wg3 b

    def __repr__(self) -> str:
        return f"Node({self.position})"


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        Node_list: List[Node] = []
        for i in range(n):
            Node_list[i] = Node(edges[i][0],edges[i][2],labels[i])
        for i in range(n):
            for j in range(n):
                if edges[i][1] == Node_list[j].position:
                    Node_list[i] = Node(edges[i][0],edges[i][2],labels[i], Node_list[j])
        current_position = Node_list[0].position
        end_position = Node_list[-1].position
        dict_label: dict[str, int] = {}

        def node_traverser(self, current_position: int, dict_label: dict[str, int], weight: int = 0) -> Optional["int"]:
            tmp_dict = dict_label
            min_weight = 1000000
            if current_position == -1:
                return 1000000
            if current_position != end_position:
                for i in range(n):
                    if Node_list[i].position == current_position and dict_label[Node_list[i].label] <= k:
                        dict_label[Node_list[i].label] += 1
                        after_weight += node_traverser(current_position, dict_label, weight)
                        current_position = Node_list[i].next.position if Node_list[i].next else -1
                        weight += min_weight
            dict_label = tmp_dict
            return min_weight

        return node_traverser(current_position=)
