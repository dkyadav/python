numbers = range(1,10)

def incr(n):
	#lambda valat : valat + 2
	return n+1
	

#numlist = (1,2,3,4,5,6)
m_numbers = map(incr, numbers)

print(list(numbers))
#print(list(numlist))
print(list(m_numbers))

