# BFS / DFS / Graph / Tree

## Short Explanation

DFS는 한 경로를 끝까지 탐색하고, BFS는 가까운 레벨부터 탐색한다. 트리는 보통 부모-자식 구조가 명확하지만 그래프는 방문 처리 없이는 순환에 빠질 수 있다.

## When To Use

- 연결 요소 개수 세기
- 최단 단계/최소 이동 횟수 구하기
- 트리 순회와 구조 비교
- 방향 그래프의 사이클 검사

## Basic Python Template

```python
from collections import deque

def bfs(start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt in visited:
                continue
            visited.add(nxt)
            q.append(nxt)
```

## Common Mistakes

- 방문 체크 시점을 늦게 잡아 중복 삽입이 발생함
- 행/열 범위 검사 순서를 잘못 둠
- 재귀 DFS에서 종료 조건을 놓침
- 트리 문제인데 그래프처럼 과하게 처리하거나 반대로 방문 처리를 생략함
