# 정수배열 arr와, 2차원 정수배열 queries
# queries의 원소는 길이 3의 배열이다
def solution(arr, queries):
    answer = []
    for query in queries:
        # 시작, 끝 인덱스 변수화
        s_idx = query[0]
        e_idx = query[1]
        k = query[2]
        max_val = 1000000
        for idx in range(s_idx, e_idx + 1, 1):
            # k 보다 클때만
            if arr[idx] > k:
                max_val = min(max_val, arr[idx])
        # 답이 존재하지 않으면 -1
        if max_val == 1000000:
            max_val = -1
        answer.append(max_val)
    return answer