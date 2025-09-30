def solution(my_string, index_list):
	list_str = []
	for idx in index_list:
		list_str.append(my_string[idx])
	return "".join(list_str)