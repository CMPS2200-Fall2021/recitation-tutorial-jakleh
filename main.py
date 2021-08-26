def sum_of_squares(a):
	sum = 0
	for i in a:
		sum += i**2
	return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

print(test_one())	#Prints "None"

#Test w/ negative nums...
def test_two():
	assert sum_of_squares([-1, -2, -3]) == 14

print(test_two())	#Prints "None"
