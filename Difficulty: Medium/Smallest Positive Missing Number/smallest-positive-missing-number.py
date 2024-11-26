#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        n = len(arr)
        for i in range(n) :
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = float('inf')
        for i in range(n) :
            if abs(arr[i]) == float('inf')  or arr[abs(arr[i]) - 1] < 0 :
                continue
            else :
                arr[abs(arr[i ]) - 1] *= -1

        for i in range(n)  :
            if arr[i] > 0 :
                return i + 1
        return n + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends