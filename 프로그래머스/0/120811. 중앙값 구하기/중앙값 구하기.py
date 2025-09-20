def solution(array):
    sorted_list = sorted(array)
    mid = divmod(len(sorted_list), 2)[0]
    return sorted_list[mid]