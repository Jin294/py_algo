# 문자열이 0과 5로 이루어져있는지 확인하는 함수
def check_str(str):
    for ch in str:
        if ch != '0' and ch != '5':
            return False
    return True

def solution(l, r):
    answer = []
    # l부터 r까지 순회
    for num in range(l, r+1):
        # 숫자를 문자열로 캐스팅
        num_str = str(num)
        if check_str(num_str):
            answer.append(num)
    
    # 길이가 0이라면 -1을 삽입
    if len(answer) == 0:
        answer.append(-1)
        
    return answer