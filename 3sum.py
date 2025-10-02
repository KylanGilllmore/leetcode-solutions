class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(logn)
        store = set()
        ns_len = len(nums)
        for i in range(ns_len): # O(n) checks
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            target = nums[i]
            l_ptr = i + 1
            r_ptr = ns_len - 1
            while l_ptr < r_ptr:
                sumv = nums[l_ptr] + nums[r_ptr]
                if sumv == -target:
                    store.add((nums[l_ptr],nums[r_ptr], target))
                    l_ptr += 1
                    r_ptr -= 1
                    while l_ptr < r_ptr and nums[l_ptr] == nums[l_ptr - 1]:
                        l_ptr += 1
                    while l_ptr < r_ptr and nums[r_ptr] == nums[r_ptr + 1]:
                        r_ptr -=1

                elif sumv < -target:
                    l_ptr += 1
                else:
                    r_ptr -= 1
                
        store_u = [list(val) for val in store]
        return store_u
