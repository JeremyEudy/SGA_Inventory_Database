#Author: Jeremy Eudy
#For: COP 3729 Spring 2018
#Usage: clear; python FrontEnd.py
from pymongo import *
import sys
import gridfs
import pprint
import psycopg2

try:
	postgreClient = psycopg2.connect(dbname="rdms", user="jeudy2552")
except:
	print("Unable to connect to PostgreSQL")
	sys.exit()
try:
	mongoClient = MongoClient()
except:
	print("Unable to connect to MongoDB")
	sys.exit()

db = mongoClient.SGA_Inventory
collection = gridfs.GridFS(db)

print("Welcome to the SGA Inventory and Clubs Database")
print("\n1 - View Club Database\n2 - View Budget Database\n3 - View Inventory Database\n")

def getInput():
	while (True):
		try:
			userInput = int(input("Please input a choice (0 to exit): "))
		except ValueError:
			print("Please enter a valid integer")
		else:
			return userInput

userInput = getInput()

while (True):
	if (userInput ==0):
		sys.exit()

	elif (userInput == 1):
		cur = postgreClient.cursor()
		print("\n1 - Search for club\n2 - View all clubs\n")
		userInput = getInput()

		if (userInput == 1):
			query = str(input("Input club name: ")).upper()
			cur.execute("SELECT * FROM clubs WHERE club_name = %s", (query,))
			row = cur.fetchone()
			print("Club: " + str(row[1]) + "\t\tPresident: " + str(row[2]) + "\t\tVice President: " + str(row[3]) + "\t\tTreasurer: " + str(row[4]) + "\t\tSecretary: " + str(row[5]))
			
		elif (userInput == 2):
			cur.execute("SELECT * FROM clubs")
			while (True):
				row = cur.fetchone()
				if (row == None):
					break
				print("Club: " + str(row[1]) +"\t\tPresident: " + str(row[2]) + "\t\tVice President: " + str(row[3]) + "\t\tTreasurer: " + str(row[4]) + "\t\tSecretary: " + str(row[5]))
		
		elif (userInput == 0):
			sys.exit()

		cur.close()
	
	elif (userInput == 2):
		cur = postgreClient.cursor()
		print("\n1 - Search for club\n2 - View all budgets\n")
		userInput = getInput()

		if (userInput == 1):
			query = str(input("Input club name: ")).upper()
			cur.execute("SELECT * FROM ledger WHERE club_name = %s", (query,))
			row = cur.fetchone()
			print("Club: " + str(row[1]) + "\t\tTotal Budget: " + str(row[2]) + "\t\tBudget Used: " + str(row[3]))

		elif (userInput == 2):
			cur.execute("SELECT * FROM ledger")
			while (True):
				row = cur.fetchone()
				if (row == None):
					break
				print("Club: " + str(row[1]) + "\t\tTotal Budget: " + str(row[2]) + "\t\tBudget Used: " + str(row[3]))
			cur.fetchall()
		
		elif (userInput == 0):
			sys.exit()
		
		cur.close()
	
	elif (userInput == 3):
		print("\n1 - Query by club name\n2 - Query by location\n3 - Query by condition\n")
		userInput = getInput()
		
		if (userInput == 0):
			sys.exit()
	
		elif (userInput == 1):
			counter = 0
			queryArray = []
			query = str(input("Input club name: "))
			query = query.upper()
			if (query == "CAB"):
				query = "CAMPUS ACTIVITIES BOARD \r\n"
			elif (query == "NSBE"):
				query = "NSBE (National Society of Black Engineers\r\n"
			else:
				query = query + '\r\n'
	
			for item in db.fs.files.find({"Owner" : query}):
				print(counter)
				pprint.pprint(item)
				print("-------------------------------------------------------------------------------------")
				counter+=1
				queryArray.append(item)
	
			print("\n1 - Query by club name\n2 - Query by location\n3 - Query by condition\n")
			userInput = getInput()

		elif (userInput == 2):
			counter = 0
			queryArray = []
			query = str(input("Input location: "))
			query = query.upper()
	
			for item in db.fs.files.find({"Location" : query}):
				print(counter)
				pprint.pprint(item)
				print("-------------------------------------------------------------------------------------")
				counter+=1
			queryArray.append(item)
	
			print("\n1 - Query by club name\n2 - Query by location\n3 - Query by condition\n")
			userInput = getInput()
		
		elif (userInput == 3):
			counter = 0
			queryArray = []
			query = str(input("Input condition: "))
			query = query.upper()
	
			for item in db.fs.files.find({"Condition" : query}):
				print(counter)
				pprint.pprint(item)
				print("-------------------------------------------------------------------------------------")
				counter+=1
				queryArray.append(item)
	
			print("\n1 - Query by club name\n2 - Query by location\n3 - Query by condition\n")
			userInput = getInput()
