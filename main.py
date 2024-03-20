"""
    Performs a binary search to find a target value within a sorted list.

    Explanation:
    - Binary search is an efficient algorithm for finding an item from a sorted list of items.
    - It works by repeatedly dividing in half the portion of the list that could contain the item,
      until you've narrowed down the possible locations to just one.

    How it works:
    - We start with two markers, 'start' and 'end', which represent the range we are searching within.
    - 'mid' is calculated as the middle index of this range.
    - If the 'mid' element is equal to the target, we return the mid index.
    - If the 'mid' element is greater than the target, we move the 'end' marker to just before 'mid',
      as the target must be in the lower half of the range.
    - If the 'mid' element is less than the target, we move the 'start' marker to just after 'mid',
      as the target must be in the upper half of the range.
    - The process repeats until the target is found or the 'start' marker passes the 'end' marker.

    Parameters:
    - list: A sorted list of elements in which to search.
    - target: The value that the function attempts to find.

    Returns:
    - The index of the target element in the list if found.
    - '-1' if the target is not found in the list.

    Steps Counter:
    - 'steps' variable is used to count how many iterations or steps have been taken.
"""


print("")
print("Binary Search Algorithm - Time Complexity: O(log n)")
print("")

def binary_search(list, target):
    """
    Performs a binary search on a sorted list to find a specific target value.

    The function uses a while loop to repeatedly halve the search range until the target is found.
    It keeps track of the number of steps taken to find the target. If the target is not found in the list,
    the function returns -1.

    @param list The sorted list in which to search for the target.
    @param target The value to search for in the list.
    @returns The index of the target value in the list, or -1 if the target is not found.
    """
    steps = 0
    start = 0
    mid  = 0
    end = len(list) 

    while(start<=end):
        print("Step", steps, ":" ,str(list[start:end+1]))

        steps+=1
        mid=(start+end)//2

        if target == list[mid]:
            return mid
        if target < list[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

print("Test Case 1: ")
test_list=[10, 20, 30, 40, 50, 60, 70, 80, 90]
test_target=10
binary_search(test_list, test_target)
print("Target found: " + str(test_target))

print("\nTest Case 2: ")
test_list2=[10, 20, 30, 40, 50, 60, 70, 80, 90]
test_target2=20
binary_search(test_list2, test_target2)
print("Target found: " + str(test_target2))

print("\nTest Case 3: ")
test_list3=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
test_target3=50
binary_search(test_list3, test_target3)
print("Target found: " + str(test_target3))