# Two Pointers / Sliding Window / Prefix Sum

## Short Explanation

두 포인터는 양끝 또는 같은 방향에서 포인터를 움직이며 조건을 만족시키는 방식이고, 슬라이딩 윈도우는 연속 구간의 상태를 유지한다. Prefix sum은 구간 합을 빠르게 계산하기 위한 누적합 패턴이다.

## When To Use

- 정렬된 배열에서 쌍을 찾을 때
- 연속 부분 배열/부분 문자열 조건을 검사할 때
- 구간 합이나 평균을 반복 계산할 때
- `subarray sum = k`처럼 누적합 차이를 활용할 때

## Basic Python Template

```python
def sliding_window(nums, k):
    window_sum = 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1
```

## Common Mistakes

- 윈도우를 줄여야 하는 조건을 반대로 씀
- left/right 이동 후 상태 갱신 순서를 섞음
- prefix sum 초기값 `0` 처리를 놓침
- 음수가 포함될 때 일반 슬라이딩 윈도우가 안 되는 점을 놓침
