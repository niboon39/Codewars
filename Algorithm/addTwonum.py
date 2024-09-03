# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # print(l1.val,l2.val)
            
            carry, out = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(out)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

# Helper function to create a linked list from a list of numbers
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test the solution with example inputs
l1 = create_linked_list([2, 4, 3])
print(print_linked_list(l1))
l2 = create_linked_list([5, 6, 4])
print(print_linked_list(l2))

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print("Output linked list:")
print_linked_list(result)
