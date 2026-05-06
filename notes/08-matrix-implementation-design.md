# Matrix / Implementation / Design

## Short Explanation

행렬 문제는 방향 벡터와 경계 조건이 중요하고, 구현 문제는 조건 분기와 상태 관리가 핵심이다. 설계 문제는 어떤 연산을 `O(1)` 또는 `O(log n)`에 맞출지부터 결정해야 한다.

## When To Use

- 2차원 배열을 순회하거나 변형할 때
- 시뮬레이션 과정을 그대로 코드로 옮길 때
- 캐시, 히스토리, 사용자 정의 자료구조를 설계할 때

## Basic Python Template

```python
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for dr, dc in directions:
    nr = row + dr
    nc = col + dc
```

## Common Mistakes

- row/col 인덱스를 섞음
- 방문 처리와 원본 값 변경 시점을 잘못 둠
- 구현 순서를 머릿속으로만 유지하다가 분기 누락이 생김
- 설계 문제에서 요구 연산 복잡도를 먼저 확인하지 않음
