#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_int):
    if not list_of_int:
        return None

    def peak_helper(low, high):
        mid = (low + high) // 2

        if ((mid == 0 or list_of_int[mid] >= list_of_int[mid - 1]) and
                (mid == len(list_of_int) - 1 or
                 list_of_int[mid] >= list_of_int[mid + 1])):
            return list_of_int[mid]
        elif mid > 0 and list_of_int[mid] < list_of_int[mid - 1]:
            return peak_helper(low, mid - 1)
        else:
            return peak_helper(mid + 1, high)

    return peak_helper(0, len(list_of_int) - 1)
