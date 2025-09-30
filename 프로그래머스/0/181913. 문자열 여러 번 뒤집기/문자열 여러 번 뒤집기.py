def solution(my_string, queries):
	list_char = list(my_string)
	answer = []
	for s, e in queries:
		while s<e:
			tmp = list_char[s]
			list_char[s] = list_char[e]
			list_char[e] = tmp
			s +=1
			e -=1
	return "".join(list_char)