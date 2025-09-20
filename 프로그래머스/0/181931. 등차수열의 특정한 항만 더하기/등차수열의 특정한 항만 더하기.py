def solution(a, d, included):
    # true일때의 인덱스 저장
    check_list = []
    for idx in range(len(included)):
        if included[idx]:
            check_list.append(idx)
    # 한꺼번에 계산
    count = len(check_list)
    return a * count + d * (sum(check_list))