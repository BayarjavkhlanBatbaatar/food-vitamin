import sys
import sqlite3

requestArg = ""

def main():
	request = handleArgv()
	if request == "error":
		handleError()
	elif request == "h":
		handleHelp()
	elif request == "lf":
		handleListFood()
	elif request == "lv":
		handleListVitamins()
	elif request == "v":
		handleShowVitamin()
	elif request == "f":
		handleShowFood()

def handleArgv():
	if len(sys.argv) == 1:
		return "h"
	elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
		if len(sys.argv) != 2:
			return "error"
		return "h"
	elif sys.argv[1] == "-lf" or sys.argv[1] == "--listFood":
		if len(sys.argv) != 2:
			return "error"
		return "lf"
	elif sys.argv[1] == "-lv" or sys.argv[1] == "--listVitamin":
		if len(sys.argv) != 2:
			return "error"
		return "lv"
	elif sys.argv[1] == "-v" or sys.argv[1] == "--vitamin":
		if len(sys.argv) != 3:
			return "error"
		global requestArg
		requestArg = sys.argv[2].lower()
		return "v"
	elif sys.argv[1] == "-f" or sys.argv[1] == "--food":
		if len(sys.argv) != 3:
			return "error"
		requestArg = sys.argv[2].lower()
		return "f"
	else:
		return "error"	

def handleShowFood():
	vitList = []
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitaminQuantInFood")
	data = data.fetchall()
	for food in data:
		if food[0] == requestArg:
			vitList.append(food[1])
	print(requestArg.upper() + " has following Vitamins: ")
	vitList.sort()
	print("\n".join(vitList))

def handleShowVitamin():
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitamin")
	data = data.fetchall()

	for vitamin in data:
		vitamin_sep = vitamin[0].split(',')
		for vit in vitamin_sep:
			if vit == requestArg:
				if len(vitamin_sep) > 1:
					print("Vitamin " + vit.upper() + " is known as [" + (", ".join(vitamin_sep)) + "]")
				print("Vitamin " + vit.upper() + " is in [" + vitamin[1] + "]")
				print("What you need is: " + vitamin[2])
				print("What is too much is: " + vitamin[3])
				return
	print("Vitamin " + requestArg.upper + " is not included in Database, try another one :D")
	return

def handleListVitamins():
	vitList = []
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitamin")
	data = data.fetchall()
	for vitamin in data:
		vitamin_sep = vitamin[0].split(',')
		vitList.extend(vitamin_sep)
	vitList.sort()
	print("\n".join(vitList))
	# print(vitList)
def handleListFood():
	foodList = []
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitaminQuantInFood")
	data = data.fetchall()
	for food in data:
		if foodList.count(food[0]) == 0:
			foodList.append(food[0])
	print("\n".join(foodList))
def handleHelp():
	print('''
	use one of following flags: 
	--help or -h flag will show you instruction you can use this program

	--vitamin or -v [arg] flag will show you information about the vitamin you searched
	--food or -f [arg] will show you information about specific food

	--listFood or -lf flag will show you all food you can search for
	--listVitamin or -lv flag will show you all vitamins you can search for

	Example: 
	1) python vitaminInfo.py -h  OR python vitaminInfo.py --help
	2) python vitaminInfo.py -lf
	3) python vitaminInfo.py -v b12
	4) python vitaminInfo.py -f kale
	''')

def handleError():
	print('''
	You are using it wrong dude. 
	Type following and get help.

	python vitaminInfo.py -h
	''')

if __name__ == "__main__":
    main()

