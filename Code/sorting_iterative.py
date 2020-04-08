#!python

import time


def time_it(func):
    # Made wth love by Ben <3 - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start)) + ' s')
        return result

    return wrapper

def is_sorted(items):
    """
    Return a boolean indicating whether given items are in sorted order.

        Running time: 
            Average: O(n), need to loop through all elements to make sure
                     they're in order. 
            Worst: if all elements are sorted
            Best: if the first pair of numbers are not sorted
    
        Memory usage: O(1), does not require any extra memory to execute
    """
    # Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True

def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
        
        Running time: 
            Average:    O(n^2), need to perform n swaps to get each of (n-1) elements
                        in sorted position

            Worst:      O(n^2), the elements are reversed (reached max number of 
                        comparisons)
                        
            Best:       O(n), the elements are in sorted order but still needs to 
                        make one scan through the array to make sure it's
                        sorted and then exit early
        
        Memory usage:   O(1), does not have extra memory (besides the variables which 
                        rounds down to O(1))
    """

    # O(n) = n^2-n
    # O(n) = (n^2-n)/2

    # Repeat until all items are in sorted order
    # Swap adjacent items that are out of order

    end_pointer = len(items) - 1
    for scan in range(len(items)): # n iterations
        swap = False
        for index in range(end_pointer): # n - scan
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swap = True
        end_pointer -= 1
        if swap == False: # exit early
            break
    return items

def selection_sort(items):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    
        Running time: Best and worst: O(n^2)
        
        Memory usage: Sorts in place and does not require any extra memory
    """    
    # Repeat until all items are in sorted order
    # Find minimum item in unsorted items
    # Swap it with first unsorted item
    index = 0
    min_index = 0
    start_pointer = 0
    while not is_sorted(items):
        # swap = False
        while index < len(items):
            if items[index] < items[min_index]:
                min_index = index
            index += 1
        items[start_pointer], items[min_index] = items[min_index], items[start_pointer]
        start_pointer += 1
        index = start_pointer
        min_index = start_pointer
    return items

# @time_it
def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
        
        Running time: 
            Best:   O(n)
            Worse:  O(n^2)
        
        Memory usage: Sorts in place and does not require any extra memory
    """
    # Repeat until all items are in sorted order
    # Take first unsorted item
    # Insert it in sorted order in front of items
    
    for index in range(1, len(items)):
        # print(index)
        # if items[index] >= items[index - 1]:
        #     continue
        # else:
        move = index
        while items[move] < items[move - 1] and move > 0:
            items[move], items[move - 1] = items[move - 1], items[move]
            move -= 1
    return items

# lst = [5, 4, 3, 2, 1]
# lst = [1, 2, 3, 5, 4]
# print(bubble_sort(lst))
# print(selection_sort(lst))
# print(insertion_sort(lst))
