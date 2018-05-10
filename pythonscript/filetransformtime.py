import csv
import googlemaps
from datetime import datetime
import time 
from interruptingcow import timeout

	

def google(text):
	print("Calling Api")
	gmaps = googlemaps.Client(key='AIzaSyCNDORIMI9U_zuZqS60iAL7EP18bql4q_I')
	geocode_result = gmaps.geocode(text)
	print("Api has been called")
	return geocode_result
	


def valid(row):
	if (row.find('http:')!=-1):
		return False 
	elif (not row):
		return False 
	elif(row=='N/A'):
		return False 
	elif(row=='0'):
		return False 
	else :
		return True
def transformfiletime(file):
	i=0
	n=0
	listr=[]
	output=[]
	with open(file, encoding="utf8", errors='ignore') as fd:
		reader = csv.DictReader(fd)
		for row in reader:
			if(valid(row['address']) and (valid(row['city']) and valid(row['state']))):
				listr.append(row['address'] +","+row['city']+","+row['state']+", USA")
			elif(valid(row['address'])):
				listr.append(row['address']+", USA")
			else:
				listr.append('N/A')
				

	for i in range(0,len(listr)):
		print("This is the row you are on: "+str(i))
		if(valid(listr[i])):
			try:
				with timeout(20, RuntimeError):
					print("Appending to output")
					output.append(google(listr[i])[0]["geometry"]["location"])
					print("Appended to output")
			except RuntimeError: 
				print("Run time error occured")
				output.append("Invalid Address run time error")
				print("Appended to output")
			except: 
				print("Invalid adress")
				output.append("Invalid Address Error")
				print("Appended to output")
				
					
		else:
			print("Api was not called for this row")
			output.append("Invalid Address") 
				
	return output
	





