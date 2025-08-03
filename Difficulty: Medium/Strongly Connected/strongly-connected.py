class Solution:

    def kosaraju(self, adj):
        #code here
        st = []
        vis = set()
        for i in range(len(adj)) :
            if i not in vis :
                self.finish_time(adj , i , vis ,st)
        st =st[::-1]
        
        adj_rev = [[]for i in range(len(adj))]
        
        for i in range(len(adj)) :
            for u in adj[i]:
                adj_rev[u].append(i)
        
        del vis
        cnt = 0
        vis = set()
        for i in st :
            if i not in vis :
                self.dfs(vis , i , adj_rev)
                cnt += 1
        
        return cnt
            
        
    
    def finish_time(self , adj , node , vis , st) :
        vis.add(node)
        for neigh in adj[node] :
            if neigh not in vis :
                self.finish_time(adj , neigh , vis , st)
        st.append(node)
                
        
        
    
    def dfs(self , vis , node , adj) :
        
        vis.add(node)
        for neigh in adj[node] :
            if neigh not in vis :
                self.dfs(vis , neigh , adj)
                