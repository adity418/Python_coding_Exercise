class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoArr(arr1, arr2):
    temp = ListNode()  # Dummy node
    curr = temp

    # Convert arrays to linked lists
    list1 = ListNode(arr1[0])
    current1 = list1
    for i in range(1, len(arr1)):
        current1.next = ListNode(arr1[i])
        current1 = current1.next

    list2 = ListNode(arr2[0])
    current2 = list2
    for i in range(1, len(arr2)):
        current2.next = ListNode(arr2[i])
        current2 = current2.next

    # Merge the two linked lists
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    # Append the remaining elements of list1 or list2, if any
    curr.next = list1 if list1 else list2

    # Convert the merged linked list to an array
    merged_arr = []
    curr = temp.next
    while curr:
        merged_arr.append(curr.val)
        curr = curr.next

    return merged_arr

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

print(mergeTwoArr(arr1, arr2))
                        