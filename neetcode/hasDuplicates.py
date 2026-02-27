class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for n in range(len(nums)-1):
            if nums[n] == nums[n+1]:
                return True
        return False


# Sort the list so duplicates are adjacent, then compare neighbors. 
# Time: O(n log n) due to sorting.
# Space: O(1) because we don’t use any extra data structures.


#Solution #2 Using Hashsets
        Hashsets = set()
        
        for n in nums:
            if n in Hashsets:
                return True
            else:
                Hashsets.add(n)
                
        return False
    
#What are Hashmaps Hashsets Hashtables?
#



