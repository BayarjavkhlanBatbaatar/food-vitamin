import pandas
import sqlite3

fpath = 'sheet.tsv'
inputFile = pandas.read_csv(fpath, sep='\t')

def addToTableVitamin(vitaminString, foodString, WUNString, WTMString):
	alreadyInDb = 0
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitamin")
	data = data.fetchall()
	# print(data)
	for vit in data:
		if vit[0] == vitaminString:
			alreadyInDb = 1

	if alreadyInDb == 0:
		cur = conn.cursor()
		cur.execute("INSERT INTO vitamin VALUES (?, ?, ?, ?)",(vitaminString, foodString, WUNString, WTMString ))
		conn.commit()
		conn.close()
def addToTableVitQinFood(foodName, vitamin, quantity):
	alreadyInDb = 0
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitaminQuantInFood")
	data = data.fetchall()
	# print(data)
	for vit in data:
		if vit[0] == foodName and vit[1] == vitamin:
			alreadyInDb = 1

	if alreadyInDb == 0:
		cur = conn.cursor()
		cur.execute("INSERT INTO vitaminQuantInFood VALUES (?, ?, ?)",(foodName, vitamin, quantity))
		conn.commit()
		conn.close()
# Testing pandas
# print(inputFile)

# Testing database
# conn = sqlite3.connect("sql/database.sqlite3")
# data = conn.execute("SELECT * FROM vitamins")
# data = data.fetchall()
# print(data)

# State value 0~starting new vitamin 1~working on new vitamin
state = 0
vitaminString = ""
foodString = ""
WUNString = ""
WTMString = ""

for index, row in inputFile.iterrows():
	if(str(row["vitamin"]) != "nan"):
		if(state == 1):
			addToTableVitamin(vitaminString, foodString, WUNString, WTMString)
			state = 0
			vitaminString = ""
			foodString = ""
			WUNString = ""
			WTMString = ""
		if(vitaminString == ""):
			vitaminString = str(row["vitamin"]).lower()
		else:
			vitaminString = vitaminString + "," + str(row["vitamin"]).lower()
	elif(str(row["food"]) == "WUN"):
		WUNString = str(row["info"])
	elif(str(row["food"]) == "WTM"):
		WTMString = str(row["info"])
	else:
		if(str(row["food"]) == "WTM "):
			print(vitaminString)
		addToTableVitQinFood(row["food"], vitaminString, row["info"])
		if(foodString == ""):
			foodString = str(row["food"]).lower()
		else:
			foodString = foodString + "," + str(row["food"]).lower()
		state = 1
addToTableVitamin(vitaminString, foodString, WUNString, WTMString)
conn = sqlite3.connect("sql/database.sqlite3")
data = conn.execute("SELECT * FROM vitaminQuantInFood")
data = data.fetchall()
# print(data)
