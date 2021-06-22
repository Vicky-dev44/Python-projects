def Calculate_Course_Cgpa():	
	while True:
		try:
			sem = int(input("enter how many semesters you have in your course : "))
			i=1
			sum=0
			print("enter your semesters percentages year wise below : ")
			while i<sem+1:
				var1 = float(input(f"Enter your {i} semester Percentage :  "))
				sum +=var1
				i+=1
			sem=sem*100
			final_total=(sum / sem)*100
			print(final_total)
				
			cgpa = input("Do you want to convert your percentage to CGPA type(yes/no) : ").lower()
			if (cgpa=="yes"):
				cgp = final_total / 9.5
				print("Your total CGPA is {:.1f} ".format(cgp))
			else:
				print("Thank you so much for using my code!")
		
		except Exception:
			print("\nPlease Enter any Number broo -_- ")
		n = input("\nDo you wanna to try Again(yes/no) ").lower()
			
		if n !='yes':
			break
	print("\n*********_______Thank you for using my Code_______**********")
				
			

Calculate_Course_Cgpa()
	