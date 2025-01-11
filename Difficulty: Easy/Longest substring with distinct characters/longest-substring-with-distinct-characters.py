#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        ans = 0
        
        d = { }
        i = 0
        j = 0
        while i < len(s) :
            if s[i] in d :
                d[s[i]] += 1
                while d[s[i]] != 1 :
                    d[s[j]] -= 1
                    if d[s[j]] == 0 :
                        del d[s[j]]
                    
                    j += 1
                
            else :
                d[s[i]] = 1
                
            ans = max(ans , len(d))
            i+= 1
        
        return ans
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends