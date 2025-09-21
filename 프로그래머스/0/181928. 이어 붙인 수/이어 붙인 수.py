def solution(num_list):
    odd = []
    even = []
    for idx in range(len(num_list)):
        if num_list[idx] % 2 == 0:
            even.append(str(num_list[idx]))
        else:
            odd.append(str(num_list[idx]))
    odd_sum = int("".join(odd))
    even_sum = int("".join(even))
    
    return odd_sum + even_sum