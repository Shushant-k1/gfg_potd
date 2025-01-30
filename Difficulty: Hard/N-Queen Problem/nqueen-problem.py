#User function Template for python3
class Solution:
    def isSafe(self,board,i,j):
        n=len(board)
        if any(board[i]):
            return False
        for dx,dy in [(1,-1),(-1,-1)]:
            x,y=i+dx,j+dy
            while 0<=x<n and 0<=y<n:
                if board[x][y]:
                    return False
                x+=dx
                y+=dy
        return True
    
    def queen(self,board,c,curr,ans):
        n=len(board)
        if c==n:
            ans.append(curr.copy())
            return
        for i in range(n):
            if self.isSafe(board,i,c):
                board[i][c]=1
                curr.append(i+1)
                self.queen(board,c+1,curr,ans)
                board[i][c]=0
                curr.pop()
    
    def nQueen(self, n):
        board=[[0]*n for _ in range(n)]
        ans=[]
        self.queen(board,0,[],ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends