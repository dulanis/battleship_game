from random import randint


board = {
"battleground": [],
"rows": 7,
"columns": 7
}


for i in range(board["rows"]):
	board["battleground"].append("O  " * board["columns"])
# Create gameboard


def printBoard():
	for i in range(board["rows"]):
		print board["battleground"][i]
		print


def getPlayerRow():
	playerRow = raw_input("Guess a ship row: ")
	while not playerRow.isdigit() or (int(playerRow) < 1 or int(playerRow) > board["rows"]):
		playerRow = raw_input("Invalid guess. Enter a number between 1 and {}: ".format(str(board["rows"])))
	else:
		playerRow = int(playerRow)
	return playerRow


def getPlayerCol():
	playerCol = raw_input("Guess a ship column: ")
	while not playerCol.isdigit() or (int(playerCol) < 1 or int(playerCol) > board["columns"]):
		playerCol = raw_input("Invalid guess. Enter a number between 1 and {}: ".format(str(board["columns"])))
	else:
		playerCol = int(playerCol)
	return playerCol


class Boats(object):
	coordinates = []
	hits = 0
	def __init__(self, length):
		self.length = length
		self.coordinates = self.createBoat()
		self.sunk = False
	def createBoat(self):
		shipRow = 0
		shipCol = 0
		shipRows = [i for i in range(1, self.length + 1)]
		shipCols = [i for i in range(1, self.length + 1)]
		coin = randint(1, 2)
		if coin == 1:
			shipRow = randint(1, board["rows"])
			incrementer = randint(0, board["columns"] - self.length)
			shipCols = [x + incrementer for x in shipCols]
			print "The ship row is %s" % shipRow
			print "The ship columns are %s" % shipCols
			shipCoordinates = [shipRow, shipCols]
			return shipCoordinates
		elif coin == 2:
			shipCol = randint(1, board["columns"])
			incrementer = randint(0, board["rows"] - self.length)
			shipRows = [x + incrementer for x in shipRows]
			print "The ship column is %s" % shipCol
			print "The ship rows are %s" % shipRows
			shipCoordinates = [shipRows, shipCol]
			return shipCoordinates
	def hitBoat(self):
		self.hits += 1
		if self.hits == self.length:
			self.sunk = True


def checkForHits(playerRow, playerCol, boat):
	rowHit = False
	colHit = False
	if isinstance(boat.coordinates[0], int) and isinstance(boat.coordinates[1], list):
		if playerRow == boat.coordinates[0]:
			rowHit = True
		for x in boat.coordinates[1]:
			if playerCol == x:
				colHit = True
	elif isinstance(boat.coordinates[0], list) and isinstance(boat.coordinates[1], int):
		if playerCol == boat.coordinates[1]:
			colHit = True
		for x in boat.coordinates[0]:
			if playerRow == x:
				rowHit = True
	#print "rowHit status: %s" % rowHit
	#print "colHit status: %s" % colHit
	if rowHit and colHit:
		print "You got a hit!"
		board["battleground"][playerRow - 1] = board["battleground"][playerRow - 1].split("  ")
		board["battleground"][playerRow - 1].pop()
		s = ""
		for circle in board["battleground"][playerRow - 1]:
			s += circle
		s = s[:playerCol - 1] + "!" + s[playerCol:]
		t = ""
		for i in range(len(s)):
			t += s[i] + "  "
		board["battleground"][playerRow - 1] = t
		printBoard()
		print
		boat.hitBoat()
	else:
		print "Bro you suck"
		board["battleground"][playerRow - 1] = board["battleground"][playerRow - 1].split("  ")
		board["battleground"][playerRow - 1].pop()
		s = ""
		for circle in board["battleground"][playerRow - 1]:
			s += circle
		s = s[:playerCol - 1] + "X" + s[playerCol:]
		t = ""
		for i in range(len(s)):
			t += s[i] + "  "
		board["battleground"][playerRow - 1] = t
		printBoard()
		print


def playGame():
	print "Let's play battleship!"
	printBoard()
	print
	print "The board is {} by {}. Hits are denoted by a '!' while misses are denoted by a 'X'.".format(board["rows"], board["columns"])
	print
	boat = Boats(5)
	gameStatus = True
	while gameStatus:
		playerRow = getPlayerRow()
		playerCol = getPlayerCol()
		checkForHits(playerRow, playerCol, boat)
		if boat.sunk:
			gameStatus = False
	else:
		print "Congratulations, you won!"


playGame()
