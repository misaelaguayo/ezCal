import sys
import os
import datetime

os.chdir("C:\\Users\\aguay\\Desktop\\life\\college\\projects\\ezCal");

if len(sys.argv) > 1:
	
	if sys.argv[1] == "set":	#if the first argument is set initialize log to 0
		with open("dailyCal.txt","w") as f:
			f.write("0 0" + " " + datetime.datetime.now().strftime("%H:%M:%S"))
			print("daily log has been reset")
			
			
	elif sys.argv[1] == "check": #checks to see number of calories so far
		with open("dailycal.txt","r") as f:
			for line in f:
				pass
			last = line
			check = last.split(" ") #make an array with calories and protein
			print("Total calories so far: " + check[0])
			print("Total protein calories so far: " + check[1])
			
	
	elif sys.argv[1] == "help": #help menu for list of commands
		print("\n\tA LIST OF COMMANDS USED IN THE PROGRAM. THESE COMMANDS WILL BE USED AS ARGUMENTS IN THE PY PROGRAM\n\n\tset: This command will set the daily log to 0 calories\n\tcheck: This command will show the current calorie amount\n\t[Integer]: An integer provided as an argument will add calories to the daily log")
	
	elif sys.argv[1] == "history": #history of entries today
		with open("dailyCal.txt","r") as f:
			histArray = f.readlines()
			histTotalCal = histArray[-1].split(" ")[0] #totalCal was already a used variable name
			print()
			for i in range(len(histArray) -1): #iterate through entries and find the difference in calories for each
				secondEntry = int(histArray[i+1].split(" ")[0]) #calculating entries for calories
				firstEntry = int(histArray[i].split(" ")[0])
				
				calorieDiff = str(secondEntry - firstEntry)
				
				secondEntry = int(histArray[i+1].split(" ")[1]) #calculating entries for protein
				firstEntry = int(histArray[i].split(" ")[1])
				
				proteinDiff = str(secondEntry - firstEntry)
				
				entryTime = histArray[i+1].split(" ")[2]
				
				print("\tcalories: " + calorieDiff +  "\n\tprotein: " + proteinDiff + "\n\t\t\t" + entryTime)
			print("\tTotal: " + histTotalCal)
	
	else:										#if command not present, take arguments as new input
		newCal = int(sys.argv[1])
		newProt = int(sys.argv[2])
		
		if os.stat("dailyCal.txt").st_size != 0: #if file is not empty
			with open("dailyCal.txt", "r") as f:
				for line in f:					#read the last input
					pass
				last = line
				inputArray = last.split(" ")			#take the previous calories and add new calories to the log
				cals = int(inputArray[0])
				prot = int(inputArray[1])
				
			with open("dailyCal.txt","a+") as f: #in write mode
				totalCal = newCal + cals
				totalProt = newProt + prot
				f.write("\n" + str(totalCal) + " " + str(totalProt) + " " + datetime.datetime.now().strftime("%H:%M:%S"))
				print("Total number of calories for the day is: " + str(totalCal) + " calories")
				print("Total number of protein calories for the day is: " + str(totalProt) + " calories")
		