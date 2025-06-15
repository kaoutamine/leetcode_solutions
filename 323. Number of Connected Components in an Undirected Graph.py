class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        

        def find_parent(node):
            while par[node] != node:
                par[node] = par[par[node]] #compression step for next runs
                node = par[node]

            return node 

        def union(n1, n2):
            p1 = find_parent(n1)
            p2 = find_parent(n2) 

            if p1 == p2:
                return 0
            elif rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return -1
        disjoints = n
        for n1,n2 in edges:
            disjoints += union(n1, n2)
        
        return disjoints
            


        