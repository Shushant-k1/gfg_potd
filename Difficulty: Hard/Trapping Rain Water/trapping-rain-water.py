
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        #Code here
        left = [0] * n
        left[0] = arr[0]
        right = [0] * n
        right[-1] = arr[-1]
        for i in range(1 , n) :
            left[i] = max(arr[i] , left[i-1])
        for j in range(n-2 , -1 , -1) :
            right[j] = max(right[j + 1] , arr[j])
        ans = 0
        for i in range(n) :
            ans = ans + (min(left[i], right[i]) - arr[i])
        
        return ans

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends