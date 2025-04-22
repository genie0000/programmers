def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] == letter:
            answer += ''
        else:
            answer += my_string[i]
    return answer