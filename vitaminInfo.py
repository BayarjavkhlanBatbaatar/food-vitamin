import sys
import sqlite3
from gtts import gTTS
import os

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
	elif request == "ei":
		showExtendedInfo()
	elif request == "vi":
		showVitaminInfo()
	elif request == "vf":
		showVitaminInFood()

def handleArgv():
	global requestArg
	if len(sys.argv) == 1:
		return "h"
	elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
		return "h"
	elif sys.argv[1] == "-ei" or sys.argv[1] == "--extendedInfo":
		return "ei"
	elif sys.argv[1] == "-lf" or sys.argv[1] == "--listFood":
		return "lf"
	elif sys.argv[1] == "-lv" or sys.argv[1] == "--listVitamin":
		return "lv"
	elif sys.argv[1] == "-vi" or sys.argv[1] == "--vitaminInfo":
		requestArg = sys.argv[2].lower()
		return "vi"
	elif sys.argv[1] == "-v" or sys.argv[1] == "--vitamin":
		requestArg = sys.argv[2].lower()
		return "v"
	elif sys.argv[1] == "-f" or sys.argv[1] == "--food":
		requestArg = sys.argv[2].lower()
		return "f"
	elif sys.argv[1] == "-vf" or sys.argv[1] =="--vitaminAmountInFood":
		requestArg = sys.argv[2].lower() + " " + sys.argv[3].lower()
		return "vf"
	else:
		return "error"	

def showVitaminInFood():
	inputList = requestArg.split()
	foodname = inputList[1]
	foodname = foodname.replace("-", " ")
	vitamin = inputList[0]
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitaminQuantInFood")
	data = data.fetchall()
	for food in data:
		if foodname == food[0]:
			vits = food[1].split(',')
			for vit in vits:
				if vit == vitamin:
					print("Vitamin " + vitamin.upper() + " in " + foodname.upper() + ": " + food[2])
					print("--------------------------------")
					return
	print("As recorded in Database " + vitamin.upper() + " is not included in " + foodname.upper())
	print("--------------------------------")
def showVitaminInfo():
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitamin")
	data = data.fetchall()
	for vitamin in data:
		vitamin_sep = vitamin[0].split(',')
		for vit in vitamin_sep:
			if vit == requestArg:
				print("--------------------------------")
				print(vitamin[2])
				print("--------------------------------")
				tts = gTTS(text = vitamin[2], lang='en')
				tts.save('vitInfo.mp3')
				os.system("mpg321 vitInfo.mp3")
				return
def handleShowFood():
	vitList = []
	conn = sqlite3.connect("sql/database.sqlite3")
	data = conn.execute("SELECT * FROM vitaminQuantInFood")
	data = data.fetchall()
	for food in data:
		dummy = food[0].split()
		for foo in dummy:
			if foo == requestArg:
				vitList.append(food[0].upper() + ": " + food[1] + "\n\t [[ QUANT: " + food[2] + " ]]")
	print("\nSearched for " + requestArg.upper() + ": ")
	vitList.sort()
	print("\n".join(vitList))
	print("--------------------------------")
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
				print("What you need is: " + vitamin[3])
				print("What is too much is: " + vitamin[4])
				print("--------------------------------")
				return
	print("Vitamin " + requestArg.upper() + " is not included in Database, try another one :D")

	print("--------------------------------")
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

	print("--------------------------------")
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
	print("--------------------------------")
def handleHelp():
	print('''
	use one of following flags: 
	h or help flag will show you instruction you can use this program.

	lf or listFood flag will show you all food you can search for.
	lv or listVitamin flag will show you all vitamins you can search for.

	v [arg] or vitamin [arg] flag will show you list of food which includes the vitamin you searched.
	f [arg] or food [arg] will show you list of vitamins in the specific food.
	vi [arg] or vitaminInfo will show you info about effect of the vitamin on your body.

	vf [arg][arg] or vitaminAmountInFood will show you how much of the vitamin is in the food.
		!!!!! if food name consists of multiple words, connect those words with dash '-'

	ei or extendedInfo flag will you show you long boring info. 
		You can it from https://greatist.com/health/ultimate-guide-vitamins-and-minerals.
		It is easier to read from the source.


	Example: 
	1) vitaminInfo.sh h  OR vitaminInfo.sh help
	2) vitaminInfo.sh lf
	3) vitaminInfo.sh v b12
	4) vitaminInfo.sh f kale
	''')

def handleError():
	print('''
	You are using it wrong dude. 
	Type following and get help.

	vitaminInfo.sh help
	''')

def showExtendedInfo():
	print(''' 
Vitamins: Organic substances required for normal cell function, growth, and development. There are 13 essential vitamins. (More on that below)

Fat-Soluble Vitamins: Fat-soluble vitamins are those that bind to fat in the stomach and are then stored in the body for later use. We are less likely to become deficient in these vitamins (A, D, E, and K), but more likely to build up to toxic levels, usually due to extreme overconsumption or overzealous supplement use. (Or maybe just an unhealthy obsession with kale chips…)

Water-Soluble Vitamins: The rest of the vitamins are water-soluble, meaning they can be absorbed directly by cells. When in excess, these vitamins are flushed out of our system with each bathroom break. The water-soluble vitamins — biotin, vitamin C, niacin, folic acid, pantothenic acid, and the four B complex vitamins — need to be restored more frequently, but the body can tolerate higher doses.

Minerals: Minerals are inorganic substances (meaning they contain no carbon), and all hold on place on the good ol’ periodic table (flashback to 6th grade chemistry class!). They’re also necessary for normal body function and development. There are two groups of minerals: macrominerals (which the body needs in large doses) and trace minerals (only a pinch required).

RDA: Recommended Dietary Allowances, or RDAs, represent the average daily dietary intake of each vitamin and mineral a person needs to stay healthy and steer clear of deficiencies. The values, which are all backed by scientific data, are broken down by age and gender.

AI: For those vitamins for which an RDA has not yet been set (usually due to lack of scientific data), an AI, or adequate intake level, is used in place.

UL: The tolerable upper intake level (UL) is the maximum amount of daily vitamin or mineral dosage that is likely to be safe for the average person. Stay under the UL radar (especially when using supplements) to keep toxicities at bay.

The Measurements: Vitamins or minerals that are needed in larger doses are expressed in units of milligrams (mg). Trace minerals and vitamins are expressed in micrograms (mcg). There are 1,000 mcg in one milligram (no fancy math here). All of Greatist’s recommendations for daily intake (“What You Need”) and limits (What’s Too Much”) follow the RDA, AI, and UL guidelines.


	''')

if __name__ == "__main__":
    main()

