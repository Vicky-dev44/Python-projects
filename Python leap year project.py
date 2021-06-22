def leapyear():
	
	year = None	
	while not year:
		year = input("enter your year : ")
	
	year = int(year)
	
	if(year%4==0):
		if(year%100==0):
			if(year%400==0):
				print("{0} is a Leap year congrats".format(year))
			else:
				print("{0} is not a leap year sorry bro".format(year))
		else:
			(str(year)+" is Not a leap year bro")
	else:
		print(str(year)+" Not a leap year")
		
leapyear()