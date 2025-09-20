def solution(code):
    answer = []
    #시작할 때 mode는 0
    mode = 0
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            elif (code[idx] != "1") and (idx % 2 == 0):
                answer.append(code[idx])
        elif mode == 1:
            if code[idx] == "1":
                mode = 0
            elif (code[idx] != "1") and (idx % 2 == 1):
                answer.append(code[idx])        
    
    return ''.join(answer) if len(answer) > 0 else "EMPTY"