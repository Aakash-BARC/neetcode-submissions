class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in dic:
                return [dic[complement]+1,i+1]
            else:
                dic[numbers[i]] = i