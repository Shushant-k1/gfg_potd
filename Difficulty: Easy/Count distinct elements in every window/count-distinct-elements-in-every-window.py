
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        
        d = { }
        
        for i in range(k) :
            if arr[i] in d :
                d[arr[i]] += 1
            else :
                d[arr[i]] = 1
        
        ans = [len(d)]
        
        for i in range(k , len(arr)) :
            d[arr[i - k ]] -= 1
            if arr[i] in d :
                d[arr[i]] += 1
            else :
                d[arr[i]] = 1
                
            if d[arr[i - k]] == 0 :
                del d[arr[i-k]]
            
            ans.append(len(d))
        
        return ans


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends