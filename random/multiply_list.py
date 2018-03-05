

input_list = []



def multiply(a_list):
	result = 1
	
	for element in a_list:
		result *= element
		
		
	return result

def main(one_list):
	output_list = []
	size = len(one_list)
	
	for index in range(size):
		output_list.append(multiply(one_list[:index]+one_list[index+1:]))
		
		
	return output_list
		
		
print(main(input_list))
		
		
		
	
	
