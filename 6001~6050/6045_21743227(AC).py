# 정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = map(int, input().split())

sum_n = a+b+c
avg = format(sum_n/3, ".2f")

print(sum_n, avg)
