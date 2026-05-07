"""
Problem: Contains Duplicate
Difficulty: Easy
Category: Array / String / Hash
Link: https://leetcode.com/problems/contains-duplicate/

Study Plan:
- Week: 1
- Day: 2
- Role: Practice
- Task:
  - Solve with set-based duplicate check.

Idea:
- 직접 하나씩 보면서 중복 발견 즉시 종료

Code:
  '''
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True    
            num_set.add(n)
        return False

  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(num_set) != len(nums):
            return True
        return False
  '''

Time Complexity:
- O(n) where n is the length of the input list, due to the set operations.

Space Complexity:
- O(n) in the worst case if all elements are unique, as we store them in a set.

Status:
- Solved

Mistake:
- None yet.

Retry:
  Idea:
  -

  Code:
    '''
    '''

  Time Complexity:
  -

  Space Complexity:
  -
"""
