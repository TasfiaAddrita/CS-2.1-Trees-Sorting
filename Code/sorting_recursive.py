#!python

from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Repeat until one list is empty
    # Find minimum item in both lists and append it to new list
    # Append remaining items in non-empty list to new list
    merge_arr = []
    lst1_index = 0
    lst2_index = 0
    while lst1_index < len(items1) and lst2_index < len(items2):
        if items1[lst1_index] < items2[lst2_index]:
            merge_arr.append(items1[lst1_index])
            lst1_index += 1
        elif items1[lst1_index] > items2[lst2_index]:
            merge_arr.append(items2[lst2_index])
            lst2_index += 1
        else:
            # merge_arr.append(items1[lst1_index])
            # merge_arr.append(items2[lst2_index])
            lst1_index += 1
            lst2_index += 1

    # if lst1_index == len(items1):
    #     for num in items2[lst2_index:]:
    #         merge_arr.append(num)
    # elif lst2_index == len(items2):
    #     for num in items1[lst1_index:]:
    #         merge_arr.append(num)

    merge_arr.extend(items1[lst1_index:])
    merge_arr.extend(items2[lst2_index:])

    print("merge", merge_arr)
    return merge_arr

# lst1 = [1, 3, 5, 7, 9]
# lst1 = [1, 3, 5, 7, 9, 11, 13, 15]
# lst2 = [2, 4, 6, 8, 10]
# lst2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#  (merge(lst1, lst2))

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order
    lst1, lst2 = bubble_sort(items[0 : len(items)//2]), selection_sort(items[len(items)//2 : len(items)])
    return merge(lst1, lst2)

# print(split_sort_merge([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# print(split_sort_merge([38, 29, 49, 10, 68, 39, 58, 20]))
# print(split_sort_merge([5, 3]))
# print(split_sort_merge([7, 4, 1, 13, 14, 5, 17, 9, 9, 8]))

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    # Split items list into approximately equal halves
    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order

    # if len(items) <= 1:
    #     return items
    # mid = len(items)//2
    # left_half = merge_sort(items[0:mid])
    # right_half = merge_sort(items[mid:len(items)])
    # return merge(left_half, right_half)
    print(items)
    if len(items) > 1:
        mid = len(items) // 2
        merge_sort(items[:mid])
        merge_sort(items[mid:])
        # merge(items[:mid], items[mid:])
        # print(items)
        merged = merge(items[:mid], items[mid:])
        items[:] = merged
        # return items

lst = [16, 16, 9, 7, 13, 15, 19, 9, 15, 12]
# print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# print(merge_sort([7, 5, 13, 18, 19, 14, 17, 2, 7, 14]))
# print(merge_sort([16, 16, 9, 7, 13, 15, 19, 9, 15, 12]))
# print(merge_sort(['B', 'A']))
print(merge_sort(lst))
print(lst)

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pass


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    pass


# def merge_sort(a): 
#     if len(a) > 1: 
#         mid = len(a) // 2
#         L = a[:mid] 
#         R = a[mid:] 
#         merge_sort(L) 
#         merge_sort(R) 
          
#         a.clear() 
#         while len(L) > 0 and len(R) < 0: 
#             if L[0] <= R[0]: 
#                 a.append(L[0]) 
#                 L.pop(0) 
#             else: 
#                 a.append(R[0]) 
#                 R.pop(0) 
  
#         for i in L: 
#             a.append(i) 
#         for i in R: 
#             a.append(i) 