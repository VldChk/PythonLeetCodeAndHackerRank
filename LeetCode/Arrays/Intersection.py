class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        d1 = dict()
        d2 = dict()
        res = list()
        for i in nums1:
            d1[i] = d1.setdefault(i,0) + 1
        for j in nums2:
            d2[j] = d2.setdefault(j,0) + 1
        if len(d1) >= len(d2):
            for k in d1:
                if k in d2:
                    res.extend([k]*min(d1[k], d2[k]))
        else:
            for k in d2:
                if k in d1:
                    res.extend([k]*min(d1[k], d2[k]))
        return res


def intersect_sorted(nums1: list, nums2: list) -> list:
    i = 0
    j = 0
    res = list()
    while j < len(nums1) and i < len(nums2):
        if nums1[j] == nums2[i]:
            res.append(nums1[j])
            i += 1
            j += 1
        elif nums1[j] < nums2[i]:
            j += 1
        else:
            i += 1
    return res


print(intersect_sorted([1,1,2,2], [2,2]))

print(intersect_sorted([1,1,1,2,2,2,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7], [1,1,1,1,1,1,1,1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,7,7,7]))