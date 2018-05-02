
import csv
import googlemaps
from datetime import datetime
import time 

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
def transformfile(file,listin,realout,counter,hundred):
	i=counter
	n=hundred
	realoutput=realout
	if(n>1):
		print("Appending to realoutput")
		realoutput.append(listin)
		print("Appended to realoutput")
	listr=[]
	output=[]
	with open(file, encoding="utf8", errors='ignore') as fd:
		reader = csv.DictReader(fd)
		for row in reader:
			if(valid(row['address'])):
				listr.append(row['address'])
				
			else:
				listr.append('N/A')
				

		for i in range((n-1)*100,len(listr)):
			if(i<100*n):
				print("This is the row you are on: "+str(i))
				if(valid(listr[i])):
					print("Appending to output")
					output.append(google(listr[i])[0]["geometry"]["location"])
					print("Appended to output")
				else:
					print("Api was not called for this row")
					output.append("Invalid Address") 
			else:
				print("recursing function")
				n=n+1
				return transformfile(file,output,realoutput,i,n)
				

	if(n==1):
		return output
	else:
		return realoutput
	





