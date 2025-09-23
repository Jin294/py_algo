def solution(num_list):
    first_val = num_list[len(num_list) - 1]
    second_val = num_list[len(num_list) - 2]
    
    if first_val > second_val:
        num_list.append(first_val - second_val)
    else:
        num_list.append(first_val * 2)
    return num_list