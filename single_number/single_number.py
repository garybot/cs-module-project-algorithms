'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     every = set(arr)
#     for n in every:
#     	arr.remove(n)
#     for n in every:
#     	if n not in arr:
#     		return n

# def single_number(arr):
#     temp = []
#     for n in arr:
#     	if n not in temp:
#     		temp.append(n)
#     	else:
#     		temp.remove(n)
#     return temp[0]

# def single_number(arr):
#     # Your code 
#     once =     
#     for n in arr:
    	
# def single_number(arr):
#     every = set(arr)
#     # for n in every:
#     # 	arr.remove(n)
#     # for n in every:
#     # 	if n not in arr:
#     # 		return n
#     return arr - list(every) 


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")	