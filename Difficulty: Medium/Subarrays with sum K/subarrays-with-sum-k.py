#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        d = { }
        cur_s = 0
        ans = 0
        for i in arr :
            cur_s += i
            if cur_s == k :
                ans += 1
            rem = cur_s - k
            if rem in d :
                ans += d[rem]
            
            if cur_s in d :
                d[cur_s] += 1
            else :
                d[cur_s] = 1
        
        return ans
            
            
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends