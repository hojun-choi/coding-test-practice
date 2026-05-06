# Stack / Queue / Linked List

## Short Explanation

스택은 최근 값을 먼저 처리할 때, 큐는 먼저 들어온 값을 먼저 처리할 때 유용하다. 연결 리스트는 포인터 조작이 핵심이며 더미 노드, slow/fast 포인터가 자주 나온다.

## When To Use

- 괄호 매칭, 역순 계산, monotonic stack 문제
- BFS용 대기열 관리
- 중간 노드, 사이클, 병합, 뒤집기 같은 연결 리스트 조작

## Basic Python Template

```python
stack = []
for x in items:
    while stack and stack[-1] < x:
        stack.pop()
    stack.append(x)
```

## Common Mistakes

- 빈 스택/큐 예외 처리를 놓침
- 연결 리스트에서 다음 노드를 저장하기 전에 포인터를 바꿈
- 더미 노드를 쓰면 쉬운 문제를 복잡하게 구현함
- monotonic stack의 유지 조건을 명확히 쓰지 않음
