from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
               key[ord(c) - ord("a")] += 1

            h[tuple(key)].append(s)        

        return list(h.values())
        

"""
Input:  ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act","cat"],["stop","pots","tops"]]

Approach 1 (Brute Force):
- Sort each string -> group matching ones together
- Time: O(m x nlogn) where m = number of strings, n = avg string length

Approach 2 (Optimal - Hashmap):
- Use character frequency as the key instead of sorting
- Key: tuple of 26 counts (a-z), e.g. "act" -> (1,0,1,0,...,1,0,0)
- Value: list of strings that share that frequency pattern
- Note: must use tuple (not list) since keys must be hashable

Workflow:
    1. create a hashmap h = defaultdict(list)
    2. for each string, count frequency of each character (array of 26)
    3. use frequency tuple as key, append string to h[key]

Time: O(m x n) | Space: O(m x n)
"""