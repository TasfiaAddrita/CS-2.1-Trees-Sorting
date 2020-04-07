#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # O(n) = n^2-n
    # O(n) = (n^2-n)/2

    # Repeat until all items are in sorted order
    # Swap adjacent items that are out of order

    end_pointer = len(items) - 1
    for scan in range(len(items)):
        swap = False
        for index in range(end_pointer):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swap = True
        end_pointer -= 1
        if swap == False:
            break
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""    
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
                # swap = True
            index += 1
        items[start_pointer], items[min_index] = items[min_index], items[start_pointer]
        start_pointer += 1
        index = start_pointer
        min_index = start_pointer
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    pass

# lst = [5, 4, 3, 2, 1]
# lst = [1, 2, 3, 5, 4]
# print(bubble_sort(lst))
# print(selection_sort(lst))
