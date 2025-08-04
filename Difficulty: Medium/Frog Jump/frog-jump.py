#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        n = len(height)
        if n == 1 : return 0
        if n == 2 : return abs(height[0] - height[1])

        dp = [0  for i in range(n)]
        dp[1] = abs(height[0] - height[1])
        dp[2] = abs(height[0] - height[2])
        
        for i in range(3 , n ) :
            dp[i] = min(dp[i-1] + abs(height[i] - height[i -1]) , abs(height[i] - height[ i - 2]) + dp[i - 2])
            

        return dp[-1]