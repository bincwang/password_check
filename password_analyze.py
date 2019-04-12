#Written by Bincheng Wang


import string
#more_than_fifteen = 0
#less_than_six = 0
#less_than_eight = 0



array = [0]*30

maximum = 0

one_com = 0
two_com = 0
three_com = 0
four_com = 0
only_num = 0
only_low_key_letter = 0
only_symbol = 0
only_high_key_letter = 0
count = 0
number_and_lowercase = 0
lower_case_and_uppercase = 0
with open("password.txt") as f:
	for line in f:
                try:
			new_line = line.split(":")[1].replace(" ","")
		except:
			continue
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
		current = new_line[:-1]
		if(len(current)<=30):
			array[len(current)-1] +=1

			
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
			if(lower_case==1):
				only_low_key_letter+=1
			if(upper_case==1):
				only_high_key_letter+=1
			if(third_party==1):
				only_symbol+=1
			if(num==1):
				only_num+=1
			one_com+=1
		if(together ==2):
			if(lower_case==1 and num==1):
				number_and_lowercase+=1
			if(lower_case==1 and upper_case==1):
				lower_case_and_uppercase+=1
			two_com +=1
		if(together ==3):
			if(lower_case==1 and num==1):
				number_and_lowercase+=1
			if(lower_case==1 and upper_case==1):
				lower_case_and_uppercase+=1
			three_com+=1
		if(together ==4):
			if(lower_case==1 and num==1):
				number_and_lowercase+=1
			if(lower_case==1 and upper_case==1):
				lower_case_and_uppercase+=1
                        four_com+=1
		count+=1
		if(count > 1000000):
			break
haha = 0
for i in array:
	haha+=1
	print ("There are %s length %s passwords in 1000000 lines " % (i,haha))
print ("There are %s no mixture passwords in 1000000 files " % (one_com))
print ("There are %s only number passwords in 1000000 files " % (only_num))
print ("There are %s only lower case letter passwords in 1000000 files " % (only_low_key_letter))
print ("There are %s only upper case letter passwords in 1000000 files " % (only_high_key_letter))
print ("There are %s only symbol passwords in 1000000 files " % (only_symbol))
print ("There are %s passwords having at least a number and a lower case letter in 1000000 files " % (number_and_lowercase))
print ("There are %s passwords having at least a lowercase and a upper_case letter in 1000000 files " % (lower_case_and_uppercase))

print ("There are %s having two combinations of passwords in 1000000 files " % (two_com))
print ("There are %s passwords containing more than three combinations in 1000000 files " % (three_com))
print ("There are %s passwords containing more than four combinations in 1000000 files " % (four_com))
print ("Maximum length: %s" % (maximum))
