# Binary Search / Sorting / Intervals

## Short Explanation

이분 탐색은 정렬된 공간에서 답을 절반씩 줄여 찾는 패턴이고, 정렬은 비교 기준을 고정해 문제를 단순화한다. Interval 문제는 보통 정렬 후 겹침 여부를 순차적으로 처리한다.

## When To Use

- 정렬된 배열에서 값이나 경계를 찾을 때
- `최소/최대 가능한 값`을 답으로 탐색할 때
- 겹치는 구간을 병합하거나 제거해야 할 때

## Basic Python Template

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Common Mistakes

- `left <= right`와 `left < right` 케이스를 혼동함
- mid 갱신 후 left/right 이동을 잘못해 무한 루프가 남
- interval 정렬 기준을 시작점/끝점 중 잘못 잡음
- binary search on answer에서 판별 함수 조건을 불명확하게 둠
