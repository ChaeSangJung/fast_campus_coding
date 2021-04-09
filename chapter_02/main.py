# SHA-256
import hashlib
input_data = 'Baekjoon'
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)

# 수 찾기
array = [4, 1, 5, 2, 3]
x = [1, 3, 7, 9, 5]

for i in x:
  if i not in array:
    print('0')
  else:
    print('1')

파이썬에는 포함(Containment) 연산자를 ( in, not in ) 제공하며, 객체 in (not in) 시퀀스의 형태로 사용 가능하다.

1. 문자열(strings)
########### in ###########

if 'p' in 'python':
    print(True)

else:
    print(False)
-------------------------
True


########### not in ###########

if 'k' not in 'python':
    print(True)
else:
    print(False)
-------------------------
True

2. 리스트(list)
############## in ##############

if 'a' in ['a','b','c']:
    print(True)
else:
    print(False)
--------------------------------
True

############## not in ##############
if 'd' not in ['a','b','c']:
    print(True)
else:
    print(False)
--------------------------------
 True

3. 튜플(tuple)
############# in #############
if 'a' in ('a','b','c'):
	print(True)
else:
	print(False)
-------------------------
True

############# not in #############
if 'd' not in ('a','b','c'):
	print(True)
else:
	print(False)
-------------------------
True

4. 딕셔너리(Dictionary)
########### in ###########

if 'a' in {'a':1,'b':2}:
	print(True)
else:
	print(False)
---------------------------
True


########### not in ###########

if 'c' not in {'a':1,'b':2}:
	print(True)
else:
	print(False)
---------------------------
False

# 친구 네트워크
# 강의 들을 것

# 수 정렬하기
n = 5
array = [5, 2, 3, 4, 1]

for i in range(n):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i + 1, n):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

for i in array:
  print(i)

i=0
range(0, 5)
  min_index = 0
  range(0+1,5): j=1
    if array[min_index:0(5)] > array[j:1(2)]
      min_index = j(1)
  range(0+1,5): j=2
    if array[min_index:1(2)] > array[j:2(3)]
        min_index = j(1)
  range(0+1,5): j=3
    if array[min_index:1(2)] > array[j:3(4)]
        min_index = j(1)
  range(0+1,5): j=4
    if array[min_index:1(2)] > array[j:4(1)]
        min_index = j(4)
  # swap
  array[0], array[4] = array[4:1], array[0:5]
  0 1 2 3 4
  1 2 3 4 5
  .
  .
  .


# 소트 인사이드
# 강의 들을 것!

# 나이순 정렬
https://assaeunji.github.io/python/2020-05-05-bj10814/
# 강의 들을 것!