# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None

class Solution:
    # Function to clone a linked list with next and random pointer.
    def cloneLinkedList(self, head):
        if not head:
            return None

        # Step 1: Create new nodes and insert them next to original nodes
        current = head
        while current:
            new_node = Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied linked lists
        original = head
        copy = head.next
        new_head = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return new_head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None


def print_linked_list(root):
    link = {}
    temp = root
    index = 0
    while temp:
        link[temp] = index
        temp = temp.next
        index += 1

    temp = root
    result = []
    while temp:
        random_index = "NULL" if not temp.random else link.get(temp.random) + 1
        result.append(f"[{temp.data}, {random_index}]")
        temp = temp.next

    print(f"[{', '.join(result)}]")


def build_linked_list(v, org_address):
    address = [None] * len(v)
    head = Node(v[0][0])
    address[0] = head
    org_address[head] = 0
    temp = head

    for i in range(1, len(v)):
        new_node = Node(v[i][0])
        org_address[new_node] = i
        address[i] = new_node
        temp.next = new_node
        temp = temp.next

    temp = head
    for i in range(len(v)):
        random_index = v[i][1]
        if random_index != -1:
            temp.random = address[random_index - 1]
        temp = temp.next

    return head


def validate_input(org_address, head, v):
    address = [None] * len(v)
    temp = head
    for i in range(len(v)):
        if temp not in org_address or org_address[temp] != i:
            return False
        address[i] = temp
        temp = temp.next

    if temp is not None:
        return False

    temp = head
    for i in range(len(v)):
        value = v[i][0]
        random_index = v[i][1]

        if random_index == -1:
            if temp.random is not None:
                return False
        else:
            temp_node = address[random_index - 1]
            if temp.random != temp_node:
                return False
        temp = temp.next
    return True


def validation(res, org_address):
    temp = res
    while temp:
        if temp in org_address:
            return False
        if temp.random in org_address:
            return False
        temp = temp.next
    return True


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        v = []
        for _ in range(n):
            a, b = input().split()
            a = int(a)
            b = -1 if b in ["NULL", "N", "null", "n", "Null"] else int(b)
            v.append((a, b))

        org_address = {}
        head = build_linked_list(v, org_address)

        solution = Solution()
        res = solution.cloneLinkedList(head)

        # Validate if input is modified
        if validate_input(org_address, head, v):
            if validation(res, org_address):
                print_linked_list(res)
            else:
                print("Pointing to the original list")
        else:
            print("Input list modified")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends