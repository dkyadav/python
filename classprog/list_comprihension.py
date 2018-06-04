numbers = list(range(1,100))
print(numbers)

print("*****")

numbers = [num for num in range(1,100) if num%2 == 0]
print(numbers)

print("*****")

numbers = range(1,100)
for n in numbers:
	print(n.endswith(','))

