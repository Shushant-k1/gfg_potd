class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        # code here 
        top, down = 0, r - 1
        left, right = 0, c - 1
        dir = 0
        result = []
        while top <= down and left <= right :
            if dir == 0:
                for r in range(left,right+1) :
                    result.append(matrix[top][r])
                top += 1
            elif dir == 1 :
                for d in range(top,down+1) :
                    result.append(matrix[d][right])
                right -= 1
            elif dir == 2 :
                for l in range(right,left-1,-1) :
                    result.append(matrix[down][l])
                down -= 1
            else :
                for u in range(down,top-1,-1) :
                    result.append(matrix[u][left])
                left += 1
            dir = (dir + 1)%4
        return result
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends