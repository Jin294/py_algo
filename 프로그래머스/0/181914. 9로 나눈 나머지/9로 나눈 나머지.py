def solution(number):
    num_list = []
    for x in number:
        num_list.append(int(x))
    return sum(num_list) % 9