# 숫자 -> 문자열 : str(숫자)
# 문자열 -> 숫자 : int(문자열)
def solution(a, b):
    str1 = str(a)
    str2 = str(b)
    return max(int(str1 + str2), 2 * a * b)