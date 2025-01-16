# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        cur_sum = 0
        d = {}
        
        ans = 0
        for i , j in enumerate(arr) :
            cur_sum += j
            
            if cur_sum  == k :
                ans = max(ans , i + 1)
            if cur_sum - k in d :
                ans = max(ans ,i - d[cur_sum - k])
            
            if cur_sum not in d :
                d[cur_sum ] = i

        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends