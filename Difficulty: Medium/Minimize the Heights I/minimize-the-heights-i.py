#User function Template for python3



class Solution:
    def getMinDiff(self, k , arr):
        n = len(arr)
        arr.sort()
        ans = arr[n-1] - arr[0]

        for i in range(n-1):
            small1 = min(arr[0]  + k , arr[i+1] - k) 
            large1 = max(arr[n-1] - k, arr[i] + k)   
            ans = min(ans, abs(large1 - small1))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends