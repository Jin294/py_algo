def solution(num_list):
    sum_list = sum(num_list)
    sum_list = sum_list ** 2
    answer = 1
    for idx in range(len(num_list)):
        answer *= num_list[idx]
    
    return 1 if answer < sum_list else 0