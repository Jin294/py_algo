def solution(number):
    num_str = str(number)
    num_list = []
    for x in num_str:
        target_num = int(x)
        num_list.append(target_num)
    return sum(num_list) % 9