#User function Template for python3
class Solution:

	# Function to find maximum
    def maxProduct(self,arr,):
        # code here
        mx , mi = 1 , 1
        ans = float("-inf")
        for i in arr :
            x = mx * i
            y = mi * i
            mx = max(y , x , i )
            mi = min(x , y , i)
            ans = max(ans , mx)
            if mx == 0 and mi == 0:
                mi = ma = 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends