#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        ans = 0
        dict = { } 
        for ele in arr :
            if target - ele in dict :
                ans += dict[target-ele]
            if ele in dict :
                dict[ele] += 1
            else :
                dict[ele] = 1
        return ans
                

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends