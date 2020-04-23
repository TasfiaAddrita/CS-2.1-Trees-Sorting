#!python

from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """
    Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: ??? Why and under what conditions?
        Best:
        Average: O(3n + range) = O(n)
        Worst:
    Memory usage: ??? Why and under what conditions?
    """
    if len(numbers) < 1:
        return numbers
    
    # Find range of given numbers (minimum and maximum integer values)
    min_, max_ = min(numbers), max(numbers)

    # Create list of counts with a slot for each number in input range
    counts = [0] * (max_ - min_ + 1)

    # Loop over given numbers and increment each number's count
    for num in numbers:
        counts[num - min_] += 1
    
    # Improve this to mutate input instead of creating new output list
    start = 0
    for index, count in enumerate(counts):
        number = min_ + index
        for offset in range(count):
            numbers[start + offset] = number
        start += count


def bucket_sort(numbers, num_buckets=10):
# def bucket_sort(numbers, num_buckets=None):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Find range of given numbers (minimum and maximum values)
    # min_, max_ = min(numbers), max(numbers)
    range_ = max(numbers) - min(numbers)
    print(range_)
    print(len(numbers))

    # if num_buckets is None:
    #     num_buckets = ??? # consider what's the max number of elements a bucket can have
    
    print(num_buckets)

    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]

    # Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        percent = num / range_
        i = range_ // num_buckets
        # i = num // num_buckets # FIX THIS
        buckets[i].append(num)
    
    # Sort each bucket using any sorting algorithm (recursive or another)
    start = 0
    for bucket in buckets:
        insertion_sort(bucket)
        end = start + len(bucket)
        numbers[start:end] = bucket
        start = end
    
    # Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == "__main__":
        
    lst = [9, 8, 7, 5, 8, 3, 1, 6, 3, 8, 0, 2, 1, 5, 7, 3, 2]
    lst = [48, 46, 31, 6, 9, 28, 3, 10, 48, 19, 39, 50, 13, 9, 29, 50, 30, 12, 30, 22]
    lst = list(range(0, 101))

    print(lst)
    print()
    # print(counting_sort(lst))
    print(bucket_sort(lst))
    print(lst) # [0, 1, 1, 2, 2, 3, 3, 3, 5, 5, 6, 7, 7, 8, 8, 8, 9]

