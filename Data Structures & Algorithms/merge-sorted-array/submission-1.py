class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1 = nums1[:m]

        i = 0
        while arr1 or nums2:
            print(i, arr1, nums2, nums1)
            v1 = arr1[0] if len(arr1) > 0 else None
            v2 = nums2[0] if len(nums2) > 0 else None

            if v1 != None and v2 != None:
                if v1 <= v2:
                    nums1[i] = v1
                    arr1 = arr1[1:]
                else:
                    nums1[i] = v2
                    nums2 = nums2[1:]
            else:
                if v1 and not v2:
                    nums1[i] = v1
                    arr1 = arr1[1:]
                else:
                    nums1[i] = v2
                    nums2 = nums2[1:]
            
            i += 1