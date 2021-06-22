def Calculate_cgpa( ):
	while True:	
		try:
			sub=int(input('Enter How Many Subjects you have in semester: '))
			i=0
			sum=0
			print("\nenter following grades you had got in semester exams O,S,A,B,C,D,F : ")
			grades = ["O","S","A","B","C","D","E","F"]
			print(" ")
			while i<sub:	
				var1=input(' enter the grade of your subject : ').upper()
				while var1 not in grades:
					var1= input("enter your valid Subject grades O,S,A,B,C,D,E,F : ").upper()
				if(var1=='O'):
					var1=10
				elif(var1=='S'):
					var1=9
				elif(var1=='A'):
					var1=8
				elif(var1=='B'):
					var1=7
				elif(var1=='C'):
					var1=6
				elif(var1=='D'):
					var1=5
				elif(var1=='F'):
					var1=0
				else:
					print('please enter valid grade above mentioned ')
				sum=sum+var1
				i+=1
			
			print(" "+str(sum))
			
			labs=int(input(' Enter no of labs in semester : '))
			j=0
			sum2=0
			while j<labs:
				lab = input("Please enter your grades in your lab: ").upper()
				while len(lab) == 0:
					lab = input("enter your valid Subject grades A,B,C,D,E,F : ").upper()
				if(lab=='O'):
					lab=10
				elif(lab=='S'):
					lab=9
				elif(lab=='A'):
					lab=8
				elif(lab=='B'):
					lab=7
				elif(lab=='C'):
					lab=6
				elif(lab=='D'):
					lab=5
				elif(lab=='F'):
					lab=0
				else:
					print('Please enter valid grade above mentioned A,B,C,D,E,F: ')
				sum2=sum2+lab
				j+=1
			print(" "+str(sum2))
			credits =int(input("enter how many credits for each subject : "))
			lab_credits = int(input("enter how many credits for each lab : "))
			sum *=credits
			sum2 *=lab_credits
			Total_result = sum+sum2
			sub =(sub*10)*credits
			labs =(labs*10)*lab_credits
			grandtotal = sub+labs
			final =(Total_result/grandtotal)*100
			print(final)	
		except Exception:
			print("\nPlease Enter Any Number Bro -_- ..")
		n = input("\nDo you want to Try Again (yes/no) : ").lower()
		print()
		if n != 'yes':
			break
	print("\n******_______Thank you for using my Code -_- ! ______*******")
	
	
Calculate_cgpa()