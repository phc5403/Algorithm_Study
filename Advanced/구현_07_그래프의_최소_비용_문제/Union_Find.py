def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_set(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

## Main ##
parent = [-1, 1, 1, 2, 4, 4, 5]
union_set(3, 6)
print(parent)

'''
# Kruskal Algorithm에서 Cycle을 판단하는 용도로 사용된다. #
>> Disjoint Set (서로소 집합)을 표현하는 자료구조.
>> 서로 다른 두 집합을 병합하는 Union(), 원소 X가 어떤 집합에 속해있는지 찾는 Find().
>> find()를 "단순 재귀 & return x" 하지않고 "부모 갱신 & return parent[x]"를 하는 이유는,
전자는 최악의 경우 노드 개수 V, 해당 연산의 횟수 M 만큼의 O(V * M)가 소요되지만
후자는 Path Compression(경로 압축)함으로써 최악의 경우 O(V + M(1 + (log2-M/V / V)))로 효율적으로 탐색이 가능하기 때문이다.
'''
