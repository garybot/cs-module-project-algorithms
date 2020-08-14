'''
Input: a List of integers
Returns: a List of integers
'''

# not quite! 
# def moving_zeroes(arr):
# 	for i in range(len(arr)):
# 		if arr[i] == 0:
# 			arr.append(arr.pop(i))
			
# 	return arr

def moving_zeroes(arr):
	zeroes = []
	others = []
	for i in range(len(arr)):
		if arr[i] == 0:
			zeroes.append(0)
		else:
			others.append(arr[i])
			
	return others + zeroes

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")