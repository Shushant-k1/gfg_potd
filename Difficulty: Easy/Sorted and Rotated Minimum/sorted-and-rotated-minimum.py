#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        l = 0
        h = len(arr) - 1
        ans = float("inf")
        while l <= h  :
            mid = ( l + h ) // 2
            ans = min(ans , arr[mid])
            if arr[l] <= arr[mid] :
                ans = min(ans , arr[l])
                l = mid + 1
            else :
                ans = min(ans , arr[mid + 1])
                h = mid - 1
        return ans


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends