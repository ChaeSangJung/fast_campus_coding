# 음계
a = [1,2,3,5,6,7,4,8]
ascending = True # 오름차순
descending = True # 내림차순

for i in range(1, len(a)): #1부터 시작하는 게 포인트
  if a[i] > a[i-1]:
    descending = False
  elif a[i] < a[i-1]:
    ascending = False

if ascending:
  print('ascending')
elif descending:
  print('descending')
else:
  print('mixed')

# 블랙잭
n = 5
m = 21
data = [1,2,3,4,5,6,7,8,9,10,11,12,13]
result = 0
length = len(data)
count = 0
list=[]

for i in range(0, length):
  for j in range(i+1, length):
    for k in range(j+1, length):
      sum_value = data[i] + data[j] + data[k]
      if sum_value <= m and result <= sum_value:
        result = sum_value
      # 합이 21인 것은 몇개일까요?
      if sum_value == m:
        count += 1
      # 합을 21로 만드는 조합을 다 구해보아요.
      if sum_value == m:
        list.append((data[i],data[j],data[k]))

print('결과:',result, '경우의 수:',count, '경우',list)

# 스택수열
n = int(input())
count = 1
stack = []
result = []

for i in range(1, n + 1): # 데이터 개수만큼 반복  
  data = int(input())
  while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
    stack.append(count)
    count += 1
    result.append('+')
  if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
    stack.pop()
    result.append('-')
  else: # 불가능한 경우
    print('NO')
    exit(0)
print('\n'.join(result)) # 가능한 경우

# 프린터 큐
# 강의 들을 것!!
조건2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
0 1 2 3 4 5 => 1 2 3 4 5 0 => 2 3 4 5 0 1
1 2 9 1 1 1    1 9 1 1 1 1    9 1 1 1 1 1
5번째!!

# 키로커
left_stack = []
right_stack = []
# data = ["<","<","B","P","<","A",">",">","C","d","-"]
data = 'ABC<<D>E<<F>>--'
for i in data:
  if i == '-':
    if left_stack:
      left_stack.pop()
  elif i == '<':
    if left_stack:
      right_stack.append(left_stack.pop())
  elif i == '>':
    if right_stack:
      left_stack.append(right_stack.pop())
  else:
    left_stack.append(i)
left_stack.extend(reversed(right_stack))
print(''.join(left_stack))
# extend와 reversed에 대해 강의 다시 듣기
extend()
reversed()