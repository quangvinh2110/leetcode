class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i+1: [] for i in range(len(edges))}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(
                graph: dict, 
                parent: int, 
                start: int, 
                visited: set, 
                path: list
            ):
            # print(start)
            visited.add(start)
            path.append(start)
            for adjacent_node in graph[start]:
                if adjacent_node not in visited:
                    new_path = dfs(graph, start, adjacent_node, visited, path.copy())
                    if new_path:
                        return new_path
                elif parent and adjacent_node!=parent:
                    # print(parent)
                    # print(start)
                    return path[path.index(adjacent_node):] + [adjacent_node]
            return None
        
        path_contains_cycle = dfs(
            graph,
            None,
            1,
            set(),
            []
        )
        removable_edges = []
        for i in range(len(path_contains_cycle)-1):
            node1 = path_contains_cycle[i]
            node2 = path_contains_cycle[i+1]
            removable_edges.append([node1, node2] if node1<node2 else [node2, node1])

        for edge in edges[::-1]:
            if edge in removable_edges:
                return edge