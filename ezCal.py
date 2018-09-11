import sys
import os

os.chdir("C:\\Users\\aguay\\Desktop\\life\\college\\projects\\ezCal");

if len(sys.argv) > 1:
	
	if sys.argv[1] == "set":	#if the first argument is set
		with open("dailyCal.txt","w") as f: #initializing log to 0
			f.write("0 0")
			print("daily log has been reset")
			
			
	elif sys.argv[1] == "check": #checks to see number of calories so far
		with open("dailycal.txt","r") as f:
			check = f.readline().split(" ") #make an array with calories and protein
			print("Total calories so far: " + check[0])
			print("Total protein calories so far: " + check[1])
			
	
	elif sys.argv[1] == "help": #help menu for list of commands
		print("\n\tA LIST OF COMMANDS USED IN THE PROGRAM. THESE COMMANDS WILL BE USED AS ARGUMENTS IN THE PY PROGRAM\n\n\tset: This command will set the daily log to 0 calories\n\tcheck: This command will show the current calorie amount\n\t[Integer]: An integer provided as an argument will add calories to the daily log")
	
	else:										#if command not present, take arguments as new input
		newCal = int(sys.argv[1])
		newProt = int(sys.argv[2])
		
		if os.stat("dailyCal.txt").st_size != 0: #if file is not empty
			with open("dailyCal.txt", "r") as f: #in read mode
				inputArray = (f.readline()).split(" ");			#take the previous calories and add new calories to the log
				cals = int(inputArray[0])
				prot = int(inputArray[1])
				
			with open("dailyCal.txt","w") as f: #in write mode
				totalCal = newCal + cals
				totalProt = newProt + prot
				f.write(str(totalCal) + " " + str(totalProt))
				print("Total number of calories for the day is: " + str(totalCal) + " calories")
				print("Total number of protein calories for the day is: " + str(totalProt) + " calories")
			
				
				
		
		'''with open("dailyCal.txt", "w+") as f: #in write mode
			f.write(cals)
		print("You have entered: " + cals + " calories")'''
		#trying this again