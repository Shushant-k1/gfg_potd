#User function Template for python3


class Solution:
    def is_possible(self, stalls , k , cur) :
        n = len(stalls)
        cnt = 0
        prev = -float('inf')
        for i in stalls :
            if i - prev >= cur :
                prev = i
                cnt += 1
                if cnt == k :
                    return True
        return False
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        l = 1
        r = stalls[-1] - stalls[0]
        while l < r :
            mid = (l + r) // 2
            if self.is_possible(stalls , k , mid) :
                l = mid + 1
            else :
                r = mid
        return l - 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends