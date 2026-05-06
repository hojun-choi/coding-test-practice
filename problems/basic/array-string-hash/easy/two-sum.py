"""
Problem: Two Sum
Difficulty: Easy
Category: Array / String / Hash
Link: https://leetcode.com/problems/two-sum/

Study Plan:
- Week: 1
- Day: 1
- Role: Concept Example
- Task:
  - Practice complement lookup with a hash map.
  - Retry on Week 1 Day 4 without hints.

Idea:
- 리스트 차례대로 확인

Code:
  '''
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          listN = len(nums)
          for n in range(0, listN):
              firstN = nums[n]
              targetSecondN = target - firstN
              for n2 in range(n + 1, listN):
                  if targetSecondN == nums[n2]:
                      return [n, n2]
  '''

Time Complexity:
- O(n^2) where n is the length of the input list.

Space Complexity:
- O(1) as we are not using any additional data structures.

Status:
- Solved

Mistake:
- None yet.

Retry:
  Idea:
  - 지나온거 다 기억 후 필요 할 때 바로 꺼내서 확인하기

  Code:
    '''
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}

            for i, num in enumerate(nums):
                need = target - num

                if need in seen:
                    return [seen[need], i]

                seen[num] = i
    '''

  Time Complexity:
  - O(n) where n is the length of the input list.

  Space Complexity:
  - O(n) as we are using a hash map to store the elements we have seen so far.
"""
