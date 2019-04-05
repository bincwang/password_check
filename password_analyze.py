#Written by Bincheng Wang


import string
#more_than_fifteen = 0
#less_than_six = 0
#less_than_eight = 0
one = 0
two = 0
three = 0
four= 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
thirteen = 0
fourteen = 0
more_than_fifteen = 0



one_com = 0
two_com = 0
three_com = 0
four_com = 0


count = 0

with open("password.txt") as f:
	for line in f:
                new_line = line.split(":")[1]
		num = 0
		lower_case = 0
		upper_case = 0
		third_party = 0
		"""if(len(new_line[:-1])<=6):
			less_than_six+=1
		if(len(new_line[:-1])<=8):
			less_than_eight+=1
		if(len(new_line[:-1])>=15):
			more_than_fifteen+=1"""
		if(len(new_line[:-1])==1):
                        one+=1
                if(len(new_line[:-1])==2):
                        two+=1
                if(len(new_line[:-1])==3):
                        three+=1
                if(len(new_line[:-1])==4):
                        four+=1
                if(len(new_line[:-1])==5):
                        five+=1
                if(len(new_line[:-1])==6):
                        six+=1
                if(len(new_line[:-1])==7):
                        seven+=1
                if(len(new_line[:-1])==8):
                        eight+=1
                if(len(new_line[:-1])==9):
                        nine+=1
                if(len(new_line[:-1])==10):
                        ten+=1
                if(len(new_line[:-1])==11):
                        eleven+=1
                if(len(new_line[:-1])==12):
                        twelve+=1
                if(len(new_line[:-1])==13):
                        thirteen+=1
                if(len(new_line[:-1])==14):
                        fourteen+=1
                if(len(new_line[:-1])>=15):
			more_than_fifteen+=1
			
		for char in new_line[:-1]:
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
		if(together ==2):
			two_com +=1
		if(together ==3):
			three_com+=1
		if(together ==4):
                        four_com+=1
		count+=1
		if(count > 100000):
			break

"""print ("There are %s less or equal than length 6 passwords in 1000000 files " % (less_than_six)) 		
print ("There are %s less or equal than length 8 passwords in 1000000 files " % (less_than_eight))"""
                   
print ("There are %s length 1 passwords in 1000000 files " % (one))
print ("There are %s length 2 passwords in 1000000 files " % (two))
print ("There are %s  length 3 passwords in 1000000 files " % (three))
print ("There are %s length 4 passwords in 1000000 files " % (four))
print ("There are %s length 5 passwords in 1000000 files " % (five))
print ("There are %s length 6 passwords in 1000000 files " % (six))
print ("There are %s  length 7 passwords in 1000000 files " % (seven))
print ("There are %s length 8 passwords in 1000000 files " % (eight))
print ("There are %s  length 9 passwords in 1000000 files " % (nine))
print ("There are %s length 10 passwords in 1000000 files " % (ten))
print ("There are %s length 11 passwords in 1000000 files " % (eleven))
print ("There are %s length 12 passwords in 1000000 files " % (twelve))
print ("There are %s length 13 passwords in 1000000 files " % (thirteen))
print ("There are %s length 14 passwords in 1000000 files " % (fourteen))
print ("There are %s more or equal than length 15 passwords in 1000000 files " % (more_than_fifteen))                
print ("There are %s no mixture passwords in 1000000 files " % (one_com))
print ("There are %s having two combinations of passwords in 1000000 files " % (two_com))
print ("There are %s passwords containing more than three combinations in 1000000 files " % (three_com))
print ("There are %s passwords containing more than four combinations in 1000000 files " % (four_com))
 		
 		
