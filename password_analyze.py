#Written by Bincheng lWang


import string
more_than_fifteen = 0
less_than_six = 0
less_than_eight = 0

one_com = 0
two_com = 0
three_com = 0

count = 0

with open("password.txt") as f:
	for line in f:
		num = 0
		lower_case = 0
		upper_case = 0
		third_party = 0
		print(len(line[:-1]))
		if(len(line[:-1])<=6):
			less_than_six+=1
		if(len(line[:-1])<=8):
			less_than_eight+=1
		if(len(line[:-1])>=15):
			more_than_fifteen+=1
		for char in line[:-1]:
			if((char in string.punctuation) or char==' '):
				third_party = 1
			if(char.isalpha):
				if(char.isupper()):
					upper_case = 1
				elif (char.islower()):
					lower_case = 1
			if(char.isdigit()):
				num=1
		together = lower_case+ num+upper_case+third_party
		if(together == 1):
			one_com+=1
		elif(together ==2):
			two_com +=1
		else:
			three_com+=1	
		count+=1
		if(count > 1000000):
			break

print ("There are %s less or equal than length 6 passwords in 1000000 files " % (less_than_six)) 		
print ("There are %s less or equal than length 8 passwords in 1000000 files " % (less_than_eight))
print ("There are %s no mixture passwords in 1000000 files " % (one_com))
print ("There are %s having two combinations of passwords in 1000000 files " % (two_com))
print ("There are %s passwords containing more than three combinations in 1000000 files " % (three_com))
 		
 		
 		
 		
 		
