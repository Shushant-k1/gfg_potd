# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    def rotate(self, head, k):
        tail = head
        n = 1
        while tail and tail.next :
            n += 1
            tail = tail.next
        
        k %= n
        
        if k == 0 :
            return head
        
        
        dum = head
        prev = None
        while k > 0  :
            prev = dum
            dum = dum.next
            k -= 1
        
        tail.next = head
        prev.next = None

        return dum
            
        






#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        print("~")
        t -= 1

# } Driver Code Ends