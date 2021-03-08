def leap(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			print(str(year) + " is not a leap year!\n")
		else:
			print(str(year) + " is a leap year!\n")
	else:
		print(str(year) + " is not a leap year!\n")
