import re
import sys
import os
import glob


#Function to loop directory
def searchDirectory(dirname,phrase):
	filenames = os.listdir(dirname);
	searchword = phrase

	for file in filenames:
		#print(os.path.isfile.join("C:\\Users\\PC\\Document", file))
		try:
		    if file.endswith(".txt"):
		        fileurlinfo = os.path.join(dirname, file)
		        print('Checking in file: ',fileurlinfo)
		        with open(dirname+file, 'rt') as in_file:
		        	for line in in_file: 
		        		for m in re.finditer(searchword.lower(), line.lower()):
		        			print(searchword, "found at position : ", m.start())
		        			if m.start() - 20 < 0:
				        		startprint = 0
				        	else:
				        		startprint = m.start() - 20

				        	print('found in line: ...',line[startprint:m.end()+20])
				        	print('---------------------')

			elif:
				if file.endswith(".doc") or file.endswith(".docx"):
		except:
			print ('Error while reading processing file:',file)
	return;

#Function to loop file
def searchFile( filename ,phrase):
	filename = filename
	searchword = phrase

	#print('in search ulfe')
	with open(filename, 'rt') as in_file:
		for line in in_file: 
			for m in re.finditer(searchword.lower(), line.lower()):
				print(searchword, "found at position : ", m.start())
				if m.start() - 20 < 0:
					startprint = 0
				else:
					startprint = m.start() - 20

				print('found in line: ...',line[startprint:m.end()+20])
				print('---------------------------')
	        	
	return;

phrase = input("Enter the phrase to search:")
fileordir = input("Enter the location:")

if os.path.isdir(fileordir):
	ans = input('Do you want to searc complete directory for the word? Type yes to continue.. ')
	if ans == 'yes' or ans == 'y':
		print("searching...")
		searchDirectory(fileordir,phrase)
else:
	searchFile(fileordir,phrase)
	sys.exit(0)





#sys.exit(0)
#filenames = os.listdir('C:\\Users\\PC\\Documents')
#filenames = os.listdir(fileordir);
#searchword = 'Deepak'


#for root, dirs, files in os.walk("C:\\Users\\PC\\Documents"):
#   for file in files:
#       if file.endswith(".txt"):
#            print(os.path.join(root, file))
#print(os.listdir('c:/'))
#print(glob.glob('c:/*'))

sys.exit(0)

lines = []

with open('test1.txt', 'rt') as in_file:
    for line in in_file:   
        #lines.append(line)   
        #print("lines : :: "+ line)  

        for m in re.finditer('you', line):
        	print("'you' found at position", m.start(), m.end())
        	if m.start() - 20 < 0:
        		startprint = 0
        	else:
        		startprint = m.start() - 20

        	print(line[startprint:m.end()+20])

    #for element in lines:  
        #print('elements::'+element)     
