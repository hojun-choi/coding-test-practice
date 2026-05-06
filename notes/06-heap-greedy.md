# Heap / Greedy

## Short Explanation

힙은 최솟값/최댓값을 반복해서 꺼낼 때 적합하고, greedy는 매 순간 최선 선택이 전체 최적해로 이어질 때 사용한다. 핵심은 자료구조 선택과 선택의 정당화다.

## When To Use

- 가장 큰 값/작은 값을 여러 번 꺼내야 할 때
- 우선순위가 계속 바뀌는 작업을 관리할 때
- "지금 이 선택이 가장 낫다"를 증명할 수 있을 때

## Basic Python Template

```python
import heapq

heap = []
for x in nums:
    heapq.heappush(heap, x)

smallest = heapq.heappop(heap)
```

## Common Mistakes

- Python `heapq`가 최소 힙이라는 점을 잊음
- 정렬 한 번이면 되는 문제에 힙을 과하게 사용함
- greedy 선택의 이유 없이 구현만 맞추려 함
- 전체 합/가능 여부 같은 선행 조건 검사를 빼먹음
