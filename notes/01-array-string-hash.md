# Array / String / Hash

## Short Explanation

배열과 문자열은 순차 탐색이 기본이고, 해시는 `빠른 조회/카운팅/중복 체크`에 강하다. 많은 Easy 문제는 결국 "무엇을 key로 저장할까"를 묻는다.

## When To Use

- 중복 여부를 빠르게 확인해야 할 때
- 값의 빈도 수를 세야 할 때
- 두 값의 관계를 빠르게 역추적해야 할 때
- 정렬 없이 문자열/배열 패턴을 비교해야 할 때

## Basic Python Template

```python
def count_items(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq
```

## Common Mistakes

- key 설계를 애매하게 해서 비교가 복잡해짐
- `list`로 membership check를 해서 `O(n^2)`가 됨
- 문자열 문제를 불필요하게 복사해서 공간 사용이 커짐
- 정렬이 필요한지 해시만으로 되는지 구분하지 못함
