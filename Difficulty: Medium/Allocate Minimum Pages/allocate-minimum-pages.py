class Solution:
    def is_possible(self , arr , k , mid) :
        stu = 1
        cur = 0
        for pages in arr :
            if cur + pages > mid :
                stu += 1
                cur = pages
                if stu > k : return False
            else :
                cur += pages
        return True
            
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if len(arr) < k : return -1
        l , h = max(arr) , sum(arr)
        while l < h :
            mid = (l + h) // 2
            if self.is_possible(arr , k , mid) :
                h = mid
            else :
                l = mid + 1
        return l



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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends