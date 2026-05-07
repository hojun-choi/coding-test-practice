"""
Problem: Longest Common Prefix
Difficulty: Easy
Category: Array / String / Hash
Link: https://leetcode.com/problems/longest-common-prefix/

Study Plan:
- Week: 1
- Day: 2
- Role: Practice
- Task:
  - Check string comparison and early stop logic.

Idea:
- 최소길이 찾고 그 길이만큼 비교하면서 다르면 바로 리턴하는 방식으로 풀이.

Code:
  '''
  class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        len_min=len(strs[0])
        for st in strs:
            if len(st) < len_min:
                len_min = len(st)
        if len_min==0:
            return ""
        for n in range(len_min):
            word = strs[0][n]
            for st in strs:
                if st[n] != word:
                    if n == 0:
                        return ""
                    return st[0:n]

        return st[0:len_min]

  '''

Time Complexity:
- O(n*m) where n is the number of strings and m is the length of the shortest string.

Space Complexity:
- O(1) if we don't consider the output string, otherwise O(m) for the output string.

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
