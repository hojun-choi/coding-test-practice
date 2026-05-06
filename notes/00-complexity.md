# Complexity

## Short Explanation

시간 복잡도는 입력 크기가 커질 때 연산량이 어떻게 증가하는지, 공간 복잡도는 추가 메모리가 얼마나 필요한지를 본다. 코딩 테스트에서는 정답 여부뿐 아니라 제한 시간 안에 통과 가능한지 판단하는 기준이다.

## When To Use

- 풀이를 떠올렸을 때 여러 접근을 비교할 때
- 이중 반복문, 정렬, 해시, 힙, 재귀를 사용할 때
- Brute Force를 줄여야 하는지 판단할 때

## Basic Python Template

```python
# n: input size

def solve(nums):
    # O(n)
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

## Common Mistakes

- 평균 시간 복잡도와 최악 시간 복잡도를 구분하지 않음
- 정렬 `O(n log n)`을 너무 가볍게 사용함
- 슬라이싱, `sum()`, 문자열 이어붙이기의 숨은 비용을 놓침
- 재귀 깊이와 추가 스택 메모리를 공간 복잡도에서 빼먹음
