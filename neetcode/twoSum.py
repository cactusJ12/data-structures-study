from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return [i, h[y]]
            
        # Approach: build a hashmap of value -> index, then find complement
        # - first loop maps each number to its index
        # - if duplicates exist, the last occurrence overwrites the earlier one
        # - second loop checks if complement (target - nums[i]) exists in map
        #   and ensures we don't use the same index twice (h[y] != i handles this
        #   since duplicates are stored at their last index, not the current one)
        # Time: O(n) | Space: O(n)