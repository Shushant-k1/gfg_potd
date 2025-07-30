class Solution:
	def isCycle(self, n, edges):
		#Code here
		adj = [[] for i in range(n)]
		
		adj = self.adj_mat(edges , adj)
		
		vis = set()
		for i in range(n) :
		    if i not in vis :
		        if self.dfs(adj , vis , i , -1) :
		            return True
		 
		return False
		
	
	def dfs(self , adj , vis , cur , par) :
	    vis.add(cur)
	    for neigh in adj[cur] :
	        if neigh not in vis :
		        if self.dfs(adj , vis , neigh , cur) :
		            return True
		    else :
		        if par != neigh :
		            return True
	    return False
    
    def adj_mat(self , edges , adj) :
        
        for u , v in edges :
            adj[u].append(v)
            adj[v].append(u)
        
        return adj
        
        
            
        