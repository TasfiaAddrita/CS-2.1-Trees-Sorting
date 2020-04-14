#!python

# from sorting import random_ints
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort
from timeit import default_timer as timer


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]

def time_it(func):
    # Made wth love by Ben <3 - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start)) + '  s')
        return result

    return wrapper

def merge(items1, items2):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
        
        Running time: O(n * log(n))
        
        Memory usage: O(n * log(n))
    """
    # Repeat until one list is empty
    # Find minimum item in both lists and append it to new list
    # Append remaining items in non-empty list to new list
    
    merge_arr = []

    i, j = 0, 0

    while i < len(items1) and j < len(items2):
        # readability and don't have to make a copy when used
        val_1 = items1[i]
        val_2 = items2[j]

        if items1[i] <= items2[j]:
            merge_arr.append(val_1)
            i += 1
        else:
            merge_arr.append(val_2)
            j += 1

    # --- in case we can't use the .extend function --- 
    # if lst1_index == len(items1):
    #     for num in items2[lst2_index:]:
    #         merge_arr.append(num)
    # elif lst2_index == len(items2):
    #     for num in items1[lst1_index:]:
    #         merge_arr.append(num)

    merge_arr.extend(items1[i:]) # extend is basically this 'merge_arr += items[i:]'
    merge_arr.extend(items2[j:])

    return merge_arr

def split_sort_merge(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    
        Running time: ??? Why and under what conditions?
        
        Memory usage: ??? Why and under what conditions?
    """
    # Split items list into approximately equal halves
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order
    
    lst1, lst2 = bubble_sort(items[0 : len(items)//2]), selection_sort(items[len(items)//2 : len(items)])
    
    # return in-place array
    items[:] = merge(lst1, lst2)

    # return a new array
    # return merge(lst1, lst)

# @time_it
def merge_sort(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
        
        Running time: ??? Why and under what conditions?
        
        Memory usage: ??? Why and under what conditions?
    """
    # Check if list is so small it's already sorted (base case)
    # Split items list into approximately equal halves
    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order

    # --- returns a new array of sorted elements --- 
    # if len(items) <= 1:
    #     return items
    # mid = len(items)//2
    # left_half = merge_sort(items[0:mid])
    # right_half = merge_sort(items[mid:len(items)])
    # return merge(left_half, right_half)

    # returns in-place array for sorted elements
    # --- thanks Ben and Shash --- 
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]
        merge_sort(left)
        merge_sort(right)
        merged = merge(left, right)
        items[:] = merged # overwriting items array

# def merge_vs_iterative(lst):
#     merge_time = timeit.timeit('merge_sort(lst)', 'from __main__ import merge_sort, lst')
#     insertion_time = timeit.timeit('insertion_sort(lst)')
#     size = 'small list' if len(lst) <= 1000 else 'large list'

#     return size, 'merge' if merge_time > insertion_time else 'insertion'


def partition(items, low, high):
    """
    Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
        
        Running time: ??? Why and under what conditions?
        
        Memory usage: ??? Why and under what conditions?
    """
    # Choose a pivot any way and document your method in docstring above
    divider = low 
    pivot = high # last item as pivot
    # Loop through all items in range [low..high]
    for index in range(low, high):
        # Move items less than pivot into front of range [low...p-1]
        # Move items greater than pivot into back of range [p+1...high]
        if items[index] < items[pivot]:
            # swap with divider
            items[index], items[divider] = items[divider], items[index]
            divider += 1
    # Move pivot item into final position [p] and return index p
    items[pivot], items[divider] = items[divider], items[pivot]
    return divider


def quick_sort(items, low=None, high=None):
    """
    Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
        Best case running time: ??? Why and under what conditions?
        
        Worst case running time: ??? Why and under what conditions?
        
        Memory usage: ??? Why and under what conditions?
    """
    # Check if high and low range bounds have default values (not given)
    if low is None or high is None:
        low = 0
        high = len(items) - 1
    # Check if list or range is so small it's already sorted (base case)
    if (high - low) > 0:
        # Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1, high)

if __name__ == "__main__":
    # a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # b = random_ints(50, 1, 30)
    # c = random_ints(1000, 1, 100)
    # d = random_ints(1000000, 1, 1000)
    # e = random_ints(15, 1, 50)
    # f = [4, 5, 7, 3, 1, 9, 6, 5]

    # start = timer()
    # merge_sort(d)
    # end = timer()
    # print('merge', round((end - start) * 1000, 5))

    # start = timer()
    # insertion_sort(d)
    # end = timer()
    # print('insertion', round((end - start) * 1000, 5))

    # print(f, 'original')
    # print(partition(f, 0, len(f)))
    # print(f, 'partioned')

    lst = [41, 35, 9, 40, 18, 21, 29, 20, 35, 12, 46, 12, 3, 28, 40] # dups 12, 35, 40
    print(lst)
    quick_sort(lst)
    print(lst)
