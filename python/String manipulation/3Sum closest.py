class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        current_best = -999999999
        nums.sort()
        ns_len = len(nums)
        for i in range(ns_len):
            check_val = nums[i]
            l_ptr = i +1
            r_ptr = ns_len - 1
            while l_ptr < r_ptr:
                save = check_val + nums[l_ptr] + nums[r_ptr]
                if target == save:
                    return target   
                if abs(target - current_best) >= abs(target - save):
                    current_best = save
                if save > target:
                    r_ptr -= 1
                else:
                    l_ptr +=1
                
                # while nums[l_ptr] == nums[l_ptr - 1]:
                #     l_ptr += 1
                # while nums[r_ptr] == nums[r_ptr + 1]:
                #     r_ptr -= 1
        return current_best
               
        