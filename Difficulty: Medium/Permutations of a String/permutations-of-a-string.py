#User function Template for python3


class Solution:
    def findPermutation(self, S):

        factos = [1, 1, 2, 6, 24, 120, 720 , 720 * 7 , 720 * 7 * 8 , 720 * 7 * 8 * 9]
        l = len(S)
        wordset = set()
        words = []
        sortedchars = [ch for ch in S]
        sortedchars.sort()
        
        for w in range(1, factos[l] + 1):
            chars = [ch for ch in sortedchars]
            word = ""
            for i in range(1, l + 1):
                word += chars.pop(((w - 1) // factos[l - i]) % len(chars))
            if word not in wordset:
                wordset.add(word)
                words.append(word)
        
        return words
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends