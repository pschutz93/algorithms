number_to_reverse=int(raw_input("Enter number to reverse: "))
new_num=0
length=len(str(number_to_reverse))
i=1

while i<=length:
	new_num+=(number_to_reverse % 10)*10**(length-i)
	number_to_reverse/=10
	i+=1

print new_num
