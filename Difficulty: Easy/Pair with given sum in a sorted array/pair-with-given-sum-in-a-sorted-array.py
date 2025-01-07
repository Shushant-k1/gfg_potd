#User function Template for python3


class Solution:
    def countPairs (self, arr, tar) : 
        #Complete the function
        ans = 0
        
        d  = { }
        
        for i in arr :
            if tar - i in d :
                ans += d[tar - i]
            
            if i in d :
                d[i] += 1
            else :
                d[i] = 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends