'''@Author: Amer Sulieman
   @Version: 10/07/2018
   @Info: An Encryption file'''

import sys
from pathlib import Path

#check arguments given for the script to work
if len(sys.argv)< 2:
	sys.exit("Error!!!!\nProvide <fileName> to encrypt!!");

def encryption(file):
	#File path to accomdate any running system
	filePath = Path("./"+file);
	#The file data will be copied to this variable encrypted
	Enc1=""; 
	Enc2="";
	#Open the file
	with open(filePath) as myFile:
		#read the file data
		readFile = myFile.read()

		#every letter in the read data
		for letter in readFile:
			#If the letter is small 'a' to small 'z' shift it by 13 in alpha order
			if ord(letter)>=97 and ord(letter)<=122:
				#Replace the letter and concatnate to ENC variable 
				Enc1+=chr(((ord(letter)-97+13)%26)+97);
			#If the letter is capital 'A' to capital 'Z' shoft it by 13 in alpha order
			elif ord(letter)>=65 and ord(letter)<=90 :
				#Replace the letter and concatnate to ENC variable 
				Enc1+=chr(((ord(letter)-65+13)%26)+65);	
			#If it is a line feed then add the line feed so I keep same format		
			elif ord(letter)==10:
				Enc1+="\n";
			#Any other character shift its asic by 2 spots 
			else:	
				Enc1+=chr(ord(letter)<<2);

		#Second Encryption shifts ascii's to the left by 2^2	
		for character in Enc1:
			Enc2+=chr(ord(character)<<2)

	#Write the encrypted data to the file	
	with open(filePath,"w") as myFile:
		myFile.write(Enc2);
		print(file+" Encrypted!!");

encryption(sys.argv[1]);		