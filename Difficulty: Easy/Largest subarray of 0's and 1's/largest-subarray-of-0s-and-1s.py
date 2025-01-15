class Solution:
    def maxLen(self, arr):
        d = {}
        ans = 0
        cur = 0
        
        for j in range(len(arr)):
            if arr[j] == 0 :
                cur -= 1
            else :
                cur += 1
            if cur == 0:
                ans = max(ans, j + 1)
            if cur in d:
                ans = max(ans, j - d[cur])
            else:
                d[cur] = j
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends