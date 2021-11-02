print("Enter number. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
	print("Enter number: ")
mean=sum / (count-1)
if count == 0:
	print("Input some numbers")
else:
	print(f"Quantity: {count} Sum: {sum} Mean: {mean} ")