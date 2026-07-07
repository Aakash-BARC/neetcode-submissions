class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                l = len(nums)
                op = [0] * l
                res = 1
                ind = -1
                count = 0

                for i in range(l):
                    if nums[i] == 0:
                        ind = i
                        count += 1
                    else:
                        res *= nums[i]

                if count == 0:
                    for k in range(l):
                        op[k] = res//nums[k]

                if count == 1:
                    op[ind] = res
                        
                        
                return op