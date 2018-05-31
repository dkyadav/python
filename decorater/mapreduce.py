import functools

def sum_all(on,nn):
	print(on, nn)
	return on+nn

numbers = range(1,10)
sum_num = functools.reduce(sum_all,numbers);
print(sum_num)


print("From Lamda now")
sum_numbers = functools.reduce(lambda on,nn:on+nn, numbers )
print(sum_numbers)