# zip을 이용하면 두 개의 리스트 혹은 문자열을 묶을 수 있다
def solution(str1, str2):
    answer = []
    for idx1, idx2 in zip(str1, str2):
        answer.append(idx1)
        answer.append(idx2)
    return "".join(answer)