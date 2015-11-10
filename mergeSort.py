import math

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        midpoint = int(math.floor(len(array)/2))
        first_half = merge_sort(array[0:midpoint])
        second_half = merge_sort(array[midpoint:])
        # NOTE: stoppint point: these now need to have two counters in the loop because popping/shifting isnt efficient in the same way that it is in JS
        while (len(first_half) > 0 && len(second_half) > 0):
            if len(first_half) > 0 && first_half[0] <= second_half[0]:

print merge_sort([1,2,3,4,5])
print merge_sort([5,4,3,2,1])
print merge_sort([1,3,2,4,5])
print merge_sort([5,3,1,2,4])
print merge_sort([9,1,4,3,2,7,6,10])
