'''@Author: Amer Sulieman
   @Version: 10/07/2018
   @Info: A decryption file'''

import sys
from pathlib import Path

#check arguments given for the script to work
if len(sys.argv)< 2:
	sys.exit("Error!!!!\nProvide <fileName> to decrypt!!");

def decryption(file):
	#File path to accomdate any running system
	filePath = Path("./"+file);
	#The file data will be copied to this variable encrypted
	Decrypt1=""; 
	Decrypt2="";
	#Open the file
	with open(filePath) as myFile:
		#read the file data
		readFile = myFile.read()

		#every letter in the read data
		for character in readFile:
			#decrypt1 gets shifted back 2^2 places
			Decrypt1+=chr(ord(character)>>2)

			#Loop every letter in decrypt1
		for letter in Decrypt1:
			#If the letter is small 'a' to small 'z' shift it by 13 in alpha order
			if ord(letter)>=97 and ord(letter)<=122:
				#Replace the letter and concatnate to ENC variable 
				Decrypt2+=chr(((ord(letter)-97+13)%26)+97);
			#If the letter is capital 'A' to capital 'Z' shoft it by 13 in alpha order
			elif ord(letter)>=65 and ord(letter)<=90 :
				#Replace the letter and concatnate to ENC variable 
				Decrypt2+=chr(((ord(letter)-65+13)%26)+65);	
			#If it is a line feed then add the line feed so i can keep the format		
			elif ord(letter)==10:
				Decrypt2+="\n"
			#Any other character shift its asic by 2 spots 
			else:	
				Decrypt2+=chr(ord(letter)>>2);	

	#Write the decrypted data back to the file			
	with open(filePath,"w") as myFile:
		myFile.write(Decrypt2);
		print(file +" Decrypted!!");

decryption(sys.argv[1]);	