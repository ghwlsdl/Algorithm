﻿# 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를,

# a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

# 비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,

# 그 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자이다.

# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.

a, b = map(int,input().split())
print(a<b)