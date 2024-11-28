
class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        i = 0
        sign = 1
        
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            sign = -1 if s[i] == "-" else 1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
        
        ans *= sign
        
        int_min, int_max = -2**31, 2**31 - 1
        if ans < int_min:
            return int_min
        if ans > int_max:
            return int_max
        
        return ans

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends