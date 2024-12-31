 #User function Template for python3

class Solution:
    
    def longestConsecutive(self,arr):
        #code here
        arr = list(set(arr))
        arr.sort()
        ans = 1
        maxi = 1
        for i in range(len(arr)- 1) :
            if (arr[i] + 1 ) == arr[i + 1] :
                ans += 1
                maxi = max(ans , maxi)
            else : ans = 1
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends