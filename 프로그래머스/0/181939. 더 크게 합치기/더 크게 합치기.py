# 숫자 -> 문자열 : str(숫자)
# 문자열 -> 숫자 : int(문자열)
def solution(a, b):
    str1 = str(a)
    str2 = str(b)
    num1 = int(str1 + str2)
    num2 = int(str2 + str1)
    return num1 if num1 >= num2 else num2