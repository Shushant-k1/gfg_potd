
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        l = 0
        h = n - 1
        ans = 0
        while l < h :
            cur_max = min(arr[l] , arr[h] ) * (h - l)
            ans = max(ans , cur_max)
            if arr[l] < arr[h] :
                l += 1
            else :
                h -= 1
            
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