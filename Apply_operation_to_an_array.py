class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i+1] = 0
                i += 1
            else:
                i += 1
                
        j = 0
        k = j + 1
        while j < len(nums) and k < len(nums):
            if nums[j] == 0:
                if nums[k] != 0:
                    nums[j], nums[k] = nums[k], nums[j]
                    j += 1
                    k += 1
                else:
                    k += 1
            else:
                j += 1
                k += 1
        return nums

