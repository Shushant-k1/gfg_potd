class Solution:
    def maximumProfit(self, prices):
        ans = 0
        minn = prices[0]
        for i in range(1,  len(prices)):
            ans = max(ans, prices[i] - minn)
            minn = min(minn, prices[i])
        
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends