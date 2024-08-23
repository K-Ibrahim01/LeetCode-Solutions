class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count]=nums[i]
                count = count+1
        return count

solution = Solution()
nums=[3,2,2,3]
val = 3
print(solution.removeElement(nums,val))       