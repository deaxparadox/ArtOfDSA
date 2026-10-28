class Solution1:
    """
    Using Random solution.
    """
    def removeElement(self, nums: list[int], val: int) -> int:
        idx = 0
        remove = False
        while idx < len(nums):
            remove = False
            if val == nums[idx]:
                pop = nums.pop(idx)
                remove = True

            if not remove:
                idx += 1

        return len(nums)
    

class Solution2:
    """
    Using two pointer technique.
    """
    
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k