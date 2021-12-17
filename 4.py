class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new = nums1 + nums2
        new.sort()
        print(new)

        if len(new) % 2 == 1:
            return new[len(new)//2]

        else:
            return sum([new[len(new)//2],new[len(new)//2-1]])/2
