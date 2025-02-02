#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here'
        
        maxi = max(arr[0] , arr[1])
        second_max = min(arr[0] , arr[1])
        
        for i in range(2 , len(arr)) :
            if arr[i] == maxi :
                continue
            elif arr[i] > maxi :
                second_max = maxi
                maxi = arr[i]
            
            elif arr[i] < maxi and arr[i] > second_max :
                second_max = arr[i]
        
        return -1 if maxi == second_max else second_max
                
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends