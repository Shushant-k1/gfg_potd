
class Solution:
    def search(self,arr,key):
        # Complete this function
        n = len(arr)
        l = 0
        h = n - 1
        while l <= h :
            mid = (l + h) // 2
            if arr[mid] == key :
                return mid
            elif arr[mid] >=  arr[l]  :
                if arr[l] <= key < arr[mid] :
                    h = mid - 1
                else :
                    l = mid + 1
            else :
                if arr[mid] < key <= arr[h] :
                    l = mid + 1
                else :
                    h = mid - 1
        return -1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends