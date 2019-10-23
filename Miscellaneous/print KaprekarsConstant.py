def KaprekarsConstant(num):
	steps = 0
	while(num != 6174):
		num1 = "".join(sort(str(num)))
		num2 = "".join(sort(str(num, reverse = true)))
		print(num1, num2)







print(KaprekarsConstant(input()))

