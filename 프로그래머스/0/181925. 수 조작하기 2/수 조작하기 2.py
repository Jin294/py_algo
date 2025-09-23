def get_char(num):
	if num == 1:
		return 'w'
	elif num == -1:
		return 's'
	elif num == 10:
		return 'd'
	elif num == -10:
		return 'a'

def solution(numLog):
	# 문자열을 담을 리스트
	str_list = []
	# 인덱스 1부터 numLog 순회
	for idx in range(1, len(numLog)):
		diff = numLog[idx] - numLog[idx - 1]
		char = get_char(diff)
		# 차잇값으로부터 문자를 반환받아 문자열에 넣는다
		str_list.append(char)
		
	# 리스트의 요소들 합성
	answer = "".join(str_list)
	return answer