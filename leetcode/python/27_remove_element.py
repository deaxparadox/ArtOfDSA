class Solution:
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