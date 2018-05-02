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
def transformfiletime(file):
	i=0
	n=0
	listr=[]
	output=[]
	with open(file, encoding="utf8", errors='ignore') as fd:
		reader = csv.DictReader(fd)
		for row in reader:
			if(valid(row['address'])):
				listr.append(row['address'])
				
			else:
				listr.append('N/A')
				

		for i in range(0,len(listr)):
			if(n==100):
				n=n-100
				time.sleep(10) 
				print("This is the row you are on: "+str(i))

				if(valid(listr[i])):
					try: 
						print("Appending to output")
						output.append(google(listr[i])[0]["geometry"]["location"])
						print("Appended to output")
					except:
						print("Api Call fail")
						output.append("Invalid Address Failed API Call") 
					finally:
						print("Api Call fail")
						output.append("Invalid Address Failed API Call") 

				else:
					print("Api was not called for this row")
					output.append("Invalid Address") 
			else:
				n=n+1
				print("This is the row you are on: "+str(i))
				if(valid(listr[i])):
					try: 
						print("Appending to output")
						output.append(google(listr[i])[0]["geometry"]["location"])
						print("Appended to output")
					except:
						print("Api Call fail")
						output.append("Invalid Address Failed API Call") 


				else:
					print("Api was not called for this row")
					output.append("Invalid Address") 

			
				

	return output
	





