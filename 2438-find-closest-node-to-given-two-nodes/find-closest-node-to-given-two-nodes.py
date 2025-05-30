class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        reachable_1 = {node1: 0}
        reachable_2 = {node2: 0}

        def BFS(node, reachable, weight=0):
            while True:
                next_node = edges[node]
                if reachable.get(next_node) is not None:
                    break
                if next_node != -1:
                    weight += 1
                    reachable[next_node] = weight
                    node = next_node
                else:
                    break
            
            return reachable
        
        reachable_1 = BFS(node1, reachable_1)
        reachable_2 = BFS(node2, reachable_2)

        s1 = set(reachable_1.keys()).intersection(set(reachable_2.keys()))
        s2 = set(reachable_2.keys())

        s1 = s1.intersection(s2)

        # which max(reachable_1[node], reachable_2[node]) is minimum.

        if s1 == set():
            return -1
        
        output = 0
        min_distance = 100000000
        for node in s1:
            max_distance = max(reachable_1[node], reachable_2[node])
            if min_distance == max_distance:
                output = min(output, node)
            elif min_distance > max_distance:
                min_distance = max_distance
                output = node   
        return output        
