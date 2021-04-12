# 수 정렬하기
n = int(input())
array = list()
for _ in range(n):
    array.append(int(input()))
for i in range(n):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
for i in array:
    print(i)

n = 5
array = [5, 4, 2, 3, 1]

for i in range(n):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
for i in array:
    print(i)


i = 0 
# array = [5, 4, 2, 3, 1]
range(0, 5)
    min_index = i:0
    range(0+1, 5)
        j=1
        if array[min_index:0]:5 > array[j:1]:4
            min_index = j:1
        j=2
        if array[min_index:1]:4 > array[j:2]:2
        j=3
        if array[min_index:1]:4 > array[j:3]:3
            min_index = j:3
        j=4
        if array[min_index:3]:3 > array[j:4]:1
            min_index = j:4
    array[i:0], array[min_index:4] = array[min_index:4:1], array[i:0:5] # 스와프 ['1', 4, 2, 3, '5']

i = 1
# array = ['1', 4, 2, 3, '5']
range(1, 5)
    min_index = i:1
    range(1+1, 5)
        j=2
        if array[min_index:1]:4 > array[j:2]:2
            min_index = j:2
        j=3
        if array[min_index:2]:2 > array[j:3]:3
        j=4
        if array[min_index:2]:2 > array[j:4]:5
    
    array[i:1], array[min_index:2] = array[min_index:2]:2, array[i:1]:4 # 스와프 [1, '2', '4', 3, 5]

i = 2
# array = [1, '2', '4', 3, 5]
range(2, 5)
    min_index = i:2
    range(2+1, 5)
        j=3
        if array[min_index:2]:4 > array[j:3]:3
            min_index = j:3
        j=4
        if array[min_index:3]:3 > array[j:4]:5
    
    array[i:2], array[min_index:3] = array[min_index:3]:3, array[i:2]:4 # 스와프 [1, 2, '3', '4', 5]

# 소트 인사이드
array = [9,8,8,2,9,7]
for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')
# 나이순 정렬
n = int(input())
array = []
for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

n = 3
array = [(21, "Junkyu"), (21, "Dohyun"), (20, "Sunyoung")]

array = sorted(array, key=lambda x: x[0])
for i in array:
  print(i[0], i[1])

# 좌표 정렬하기
n = int(input())
array = []

for _ in range(n):
    x, y = map(int, input().split(' '))
    array.append((x, y))
array = sorted(array)
for i in array:
    print(i[0], i[1])

# 수 정렬하기3
import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)