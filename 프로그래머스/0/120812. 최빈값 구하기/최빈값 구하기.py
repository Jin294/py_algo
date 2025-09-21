# 인덱스 카운트 방법
# array의 원소가 0과 양수, 길이가 100 미만인 상황
def solution(array):
    # 1. 모든 원소가 0이고 길이 1000인 리스트 생성
    count_list = [0] * 1000
    # 2. 원소를 인덱스 삼아서 개수 카운팅
    for num in array:
        count_list[num] += 1
        
    answer = -1
    max_count = max(count_list)
    # 3. 카운트리스트를 순회해 최빈값을 반환
    for idx in range(len(count_list)):
        if answer != -1 and max_count == count_list[idx]:
            answer = -1
            break
        elif max_count == count_list[idx]:
            answer = idx
        
    return answer