class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Last index of nums1 
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                # don't forget to decrement m
                m -= 1
            else:
                # ??
                nums1[last] < nums2[n - 1]:
                

            


