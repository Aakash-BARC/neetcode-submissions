class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        srt_nums = sorted(nums)
        count = 1
        res = 1

        for i in range(1, len(nums)):
            if srt_nums[i] == srt_nums[i-1]:
                continue
            
            if srt_nums[i] == srt_nums[i-1] + 1:
                count += 1
            
            else:
                count = 1
                
            res = max(res, count)
            
        return res