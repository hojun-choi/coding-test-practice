# Templates

실전에서 자주 꺼내 쓰는 최소 템플릿만 모아둔 페이지입니다.

## Fast Frequency Count

```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

## Two Pointers

```python
left, right = 0, len(nums) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

## Sliding Window

```python
left = 0
for right in range(len(nums)):
    # add nums[right]
    while need_shrink:
        # remove nums[left]
        left += 1
```

## BFS

```python
from collections import deque

q = deque([start])
visited = {start}
while q:
    node = q.popleft()
```

## DFS Recursive

```python
def dfs(node):
    if node is None:
        return
    for nxt in graph[node]:
        dfs(nxt)
```

## Binary Search

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
```

## Heap

```python
import heapq

heap = []
heapq.heappush(heap, value)
value = heapq.heappop(heap)
```

## 1D DP

```python
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = ...
```

## Matrix Directions

```python
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
```
