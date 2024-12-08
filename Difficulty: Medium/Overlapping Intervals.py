class Solution:
	def mergeOverlap(self, path):
		#Code here
        lst = []
        path = sorted(path)
    
        ins = [path[0][0], path[0][1]]
        for i in range(1, len(path)):
            if ins[0] <= path[i][0] <= ins[1] :
                ins[1] = max(path[i][1] , ins[1])
            elif path[i][0] > ins[1]:
                lst.append(ins)
                ins = [path[i][0], path[i][1]]
        
        if not lst or lst[-1] != ins:
            lst.append(ins)
        
        return lst
