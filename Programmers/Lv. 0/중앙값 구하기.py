# https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    answer = 0
    
    array.sort()
    idx = 0
    
    if len(array) % 2 == 0:
        idx = len(array) // 2
        answer = (array[idx-1] + array[idx])/2
    
    else:
        idx = len(array) // 2
        answer = array[idx]
    
    return answer