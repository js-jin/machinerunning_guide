# 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기

a,b = input().split(' ')
c = int(a)**int(b) 
print(c)

# 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기
a,b = input().split(' ')
a = float(a)
b = float(b)
c = a**b
print(c)

# 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기

a,b = input().split(' ')
c = int(a)//int(b)
print(c)

# 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기

a,b = input().split(' ')
c = int(a)%int(b)
print(c)

# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기

# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

a=float(input())
print( format(a, ".2f") )
