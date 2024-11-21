class Solution:
    def maximumProfit(self, prices):
        # code here
        ans = 0
        n = len(prices)
        cur = prices[0]
        for i in range(1 , n) :
            if prices[i] > cur :
                ans = max(ans , prices[i] - cur)
            else :
                cur = prices[i]
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