from functools import *

def multiply(a_list):
	result = 1
	
	for element in a_list:
		result *= element
		
		
	return result

def main(one_list):
    output_list = []
    size = len(one_list)
    for index in range(size):
        temp_list = one_list[:index]+one_list[index+1:]
        output_list.append(reduce(lambda x,y: x*y, temp_list))

    return output_list


