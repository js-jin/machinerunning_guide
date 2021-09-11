# 6033
# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

n = ord(input())
print(chr(n+1))

# 6034
# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

a,b = input().split(' ')
print(int(a)-int(b))

# 6035
# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

f1, f2 = input().split()
m = float(f1)*float(f2)
print(m)

# 6036
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

w, n = input().split()
print(w*int(n))

# 6037
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.

n = input()
s = input()
print(int(n)*s)
