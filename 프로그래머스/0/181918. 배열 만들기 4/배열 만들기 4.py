def solution(arr):
    stk = []
    
    i = 0
    while i < len(arr):
        stk_size = len(stk)
        if stk_size > 0 and stk[stk_size - 1] >= arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
            i += 1
    return stk