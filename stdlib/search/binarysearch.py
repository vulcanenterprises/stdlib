"""
binarysearch.py
=========================================================
The binarysearch.py module for python stdlib
"""
from typing import List


class BinarySearch:

    @classmethod
    def index_of(cls, a: (List[int], List[str]), key: int) -> int:
        lo = 0
        hi = len(a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if key < a[mid]:
                hi = mid - 1
            elif key > a[mid]:
                lo = mid + 1
            else:
                return mid

        return -1

