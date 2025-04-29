def solution(my_string):
    answer = 'aeiou'
    for a in answer:
        my_string = my_string.replace(a,"")
    return my_string