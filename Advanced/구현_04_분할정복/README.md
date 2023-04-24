# Divide and Conquer(분할 정복)
● Divide → Conquer → Combine = Top-down approach   

● `X^n`을 구할 때, 기본적인 반복 = O(N) 분할 정복 = O(log2n)  

## ▶ Merge sort(병합 정렬) → O(n log n)
● 여러 개의 **정렬된** 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식  
● 자료를 **최소 단위의 문제까지 분할** 후, 차례대로 정렬하여 최종 결과 획득  
● 분할 정복 알고리즘 활용, Top-down approach  

### 동작 과정 1: Divide
`def merge_sort(lst)`  
`    if len(lst) <= 1: return lst`  
  
`# 1. Divide`  
`    mid = len(lst) // 2`  
`    left = lst[:mid]`  
`    right = lst[mid:]`  
  
`# List의 크기가 1이 될 때까지 재귀 호출`  
`    left = merge_sort(left)`  
`    right = merge_sort(right)`  
  
`# 2. Conquer`  
`    return merge(left, right)`  

### 동작 과정 2: Combine
`def merge(left, right)`  
`    result = []  # 두 개의 분할된 List를 병합`  
  
`    # 양쪽 List에 원소가 남아있는 경우`  
`    while len(left) > 0 and len(right) > 0`  
`    if left[0] <= right[0]:`  
`        result.append(left.pop(0))`  
`    else:`  
`        result.append(right.pop(0))`  
  
`    if len(left) > 0:  # left가 남아있는 경우`  
`        result.extend(left)`  
  
`    if len(right) > 0  # right가 남아있는 경우`  
`        result.extend(right)`  
  
`    return result`

1. List로 구현할 경우  
  → Divide ~ Combine 과정에서 **자료의 비교 & 이동 연산이 발생하여 비효율적**  
  
2. Linked List로 구현할 경우  
  → List 구현의 비효율적 단점을 극복하여 **효과적 구현 가능**  
  
  
## ▶ Quick sort(퀵 정렬) → O()
● Merge sort  
  → 두 부분으로 나눔.  
  → 각 부분 정렬이 끝난 후 **병합하는 후처리 작업 필요**  
  
● Quick sort  
  → 분할 시, **Pivot** 기준으로 작으면 왼편, 크면 오른편에 위치.  
  → 각 부분 정렬이 끝난 후, **병합하는 후처리 작업 없음**  
  
### 동작 과정
`def quickSort(lst, left, right):`  
`    if left < right:`  
`        # Pivot의 위치를 반환하는 함수`  
`        p = partition(lst, left, right)`  
  
`        quickSort(lst, left, p - 1)`  
`        quickSort(lst, p + 1, right)`  

#### Hoare-Partition(호어-파티션 알고리즘)의 아이디어
  → Pivot값 보다 **작으면 왼쪽, 크면 오른쪽** 집합에 위치시킴.  
  → Pivot을 두 집합의 가운데에 위치시킴.  
  → Pivot이 위치한 곳은 **정렬된 상태일 때 자기가 있어야 할 위치**에 놓임.  
  → Pivot 값은 다음 정렬 과정에서 제외됨.  

● Hoare-Partition 동작 과정 ★★  
`def partition(lst, L, R):`  
`    pivot = lst[L]  # Pivot`  
`    left = L + 1  # 첫번째 값은 pivot으로 사용하기 때문`  
`    right = R`  
  
`    while left <= right:`  
`        while(left <= right and lst[left] <= pivot): left += 1`  
`        while(left <= right and lst[right] >= pivot): right -= 1`  
  
`        # 현 시점: left= pivot보다 큰 값, right= pivot보다 작은 값을 가리킴`  
`        # Pivot값은 left ~ right 사이에 해당해야 하므로 left ↔ right Swap이 일어남`  
`        if left <= right:  # 위치 = right - pivot - left 상태이니, 혹시 두 값이 크기가 반대면 교환`  
`            lst[left], lst[right] = lst[right], lst[left]`  
  
`    # 1. Pivot을 기준으로 작은값은 왼쪽, 큰 값은 오른쪽에 이동된 상태`  
`    # 2. Pivot을 작은값들과 큰값들을 분할하는 위치(중간)에 두기 위해 `  
`    lst[L], lst[right] = lst[right], lst[L]`  
  
`    return right  # pivot의 위치를 반환`  

└→ 03:42 ~  

#### Lomuto-Partition(로무토-파티션 알고리즘)의 아이디어
● 로무토 파티션 동작 과정 ★  
`def partition(lst, L, R):`  
`    pivot = lst[R]`  
`    left = L - 1`  

`    # left= Pivot보다 작은 마지막 값`  
`    # right= Pivot보다 큰 마지막 값`  
`    for right in range(L, R):`  
`        if lst[right] <= pivot:`  
`            left += 1`  
`            lst[left], lst[right] = lst[right], lst[left]`  
  
`    lst[left + 1], lst[R] = lst[R], lst[left + 1]`  
  
`    return left + 1`    

└→ 08:15 ~


## ▶ Binary Search(이진 검색)
● 순차검색보다 효율적  

● 자료의 가운데에 있는 항목의 key 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법  
  → 목적 key를 찾을 때 까지 이진 검색을 순환적으로 반복 수행해 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행.  
  → **선행 조건: 자료 정렬 상태 필요**  
  
● 검색 과정  
1. 자료의 중앙에 있는 원소를 선택(기준)  
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교  
3. 목표 값과 중앙 원소 값의 관계  
  → IF 목표 값 < 중앙 원소 값: 자료의 왼쪽 절반에 대해서 새로 검색 수행  
  → ELSE: 자료의 오른쪽 절반에 대해서 새로 검색 수행  

4. 찾고자 하는 값이 나올때 까지 위 과정 반복  

● 특징 ★★  
→ 자료의 삽입 & 삭제 발생 시 List의 상태를 **항상 정렬 상태로 유지**하는 **추가 작업 필요**  

### 1. 반복을 통한 구현
`# lst= 검색할 List, key= 검색하고자 하는 값`    
`def binarySearch(lst, key):`  
`    start = 0`  
`    end = len(lst) - 1`  
  
`    while start <= end:`  
`        mid = start + (end - start) // 2`  

`        # 검색 성공`  
`        if key == lst[mid]:`  
`            return mid`  
  
`        elif key < lst[mid]:`  
`            end = mid - 1`  
  
`        else:  # key > lst[mid]`  
`            start = mid + 1`  
  
`    # 검색 실패`  
`    return -1`    

### 2. 재귀를 통한 구현
`# lst= 검색할 List, key= 검색하고자 하는 값`    
`def binarySearch(lst, low, high, key):`  
`    # 검색 실패`  
`    if low > high:`  
`        return -1`  
  
`    else:`  
`        mid = (low + high) // 2`  
  
`        # 검색 성공`  
`        if key == lst[mid]:`  
`            return mid`  
  
`        elif key < lst[mid]:`  
`            return binarySearch(lst, low, mid - 1, key)`  
`        else:  # key > lst[mid]`  
`            return binarySearch(lst, mid + 1, high, key)`    


