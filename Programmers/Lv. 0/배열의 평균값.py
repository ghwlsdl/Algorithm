# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    answer = 0
    sum = 0
    total_num = 0

    for i in numbers:
        sum += i
        total_num += 1

    answer = sum / total_num

    return answer