# https://school.programmers.co.kr/learn/courses/30/lessons/120812

# 1차 풀이 -> 3개 중 2개 성공 ㅠ

# from collections import Counter

# def solution(array):

#     cnt = Counter(array)

#     cnt_most = cnt.most_common()

#     if cnt_most[0][1] == cnt_most[1][1]:
#         return -1
    
#     else:
#         return cnt_most[0][0]

# 2차 풀이

from collections import Counter

def solution(array):
    cnt = Counter(array)
    
    cnt_most = cnt.most_common()

    if len(cnt_most) > 1 and cnt_most[0][1] == cnt_most[1][1]:
        answer = -1

    else:
        answer = cnt_most[0][0]

    return answer