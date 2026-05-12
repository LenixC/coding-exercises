class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        max_is = 0
        i_cnt = 0
        while i < len(nums):
            if nums[i] == 1:
                i_cnt += 1
            else:
                max_is = max(max_is, i_cnt)
                i_cnt = 0
            i += 1
        
        return max(max_is, i_cnt)
