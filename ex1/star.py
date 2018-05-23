nos = int(input("Enter number of star:"))
maxn = nos
numeroftower = (int(nos/2)) + 1
stepall = numeroftower
numberofstar = 1
stepnum = 0

while numeroftower > 0:
	toprint = ''
	#print(numeroftower,'total star:',numberofstar)
	maxn = nos
	while maxn > 0:
		if maxn>stepall+stepnum or maxn<stepall-stepnum:
			toprint = toprint + ' '
		else:
			toprint = toprint + '*'
		maxn-=1
	
	numberofstar=numberofstar+2
	numeroftower=numeroftower-1
	stepnum = stepnum+1
	print(toprint)