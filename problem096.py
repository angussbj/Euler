import math
import sys #debugging only

class Sudoku:
	def __init__(self, stringrows):
		self.dataVariable = []
		for row in xrange(0, 9):
			self.dataVariable.append([])
			for entry in stringrows[row]:
				self.dataVariable[row].append(int(entry))

	def newPuzzle(self, stringrows):
		self.dataVariable = []
		for row in xrange(0, 9):
			self.dataVariable.append([])
			for entry in stringrows[row]:
				self.dataVariable[row].append(int(entry))

	def toStringRows(self):
		stringrows = []
		for row in xrange(0,9):
			rowstring = ""
			for entry in self.dataVariable[row]:
				rowstring += str(entry)
			stringrows.append(rowstring)
		return stringrows


	def data(self):
		return self.dataVariable

	def row(self, rownumber):
		return self.dataVariable[rownumber]

	def column(self, colnumber):
		col = []
		for i in xrange(0, 9):
			col.append(self.dataVariable[i][colnumber])
		return col

	def square(self, x, y):
		square = []
		x = 3*(x/3)
		y = 3*(y/3)
		for i in xrange(x, x+3):
			for j in xrange(y, y+3):
				square.append(self.dataVariable[i][j])
		return square

	def complete(self):
		for i in range(9):
			for j in range(9):
				if self.dataVariable[i][j] == 0:
					return False
		return True

	def newEntry(self, x, y, number):
		self.dataVariable[x][y] = number

	def output(self):
		print
		for row in range(0,3):
			print self.dataVariable[row][0], self.dataVariable[row][1], self.dataVariable[row][2], "|", self.dataVariable[row][3], self.dataVariable[row][4], self.dataVariable[row][5], "|", self.dataVariable[row][6], self.dataVariable[row][7], self.dataVariable[row][8]
		print "------+-------+------"
		for row in range(3,6):
			print self.dataVariable[row][0], self.dataVariable[row][1], self.dataVariable[row][2], "|", self.dataVariable[row][3], self.dataVariable[row][4], self.dataVariable[row][5], "|", self.dataVariable[row][6], self.dataVariable[row][7], self.dataVariable[row][8]
		print "------+-------+------"
		for row in range(6,9):
			print self.dataVariable[row][0], self.dataVariable[row][1], self.dataVariable[row][2], "|", self.dataVariable[row][3], self.dataVariable[row][4], self.dataVariable[row][5], "|", self.dataVariable[row][6], self.dataVariable[row][7], self.dataVariable[row][8]
		print

	def theNumber(self):
		return int(str(self.dataVariable[0][0]) + str(self.dataVariable[0][1]) + str(self.dataVariable[0][2]))



def displayPossibilities(possibilities):	#for debugging only
	for row in range(0,9):
		rowstring = ""
		for column in range(0,9):
			entrystring = ""
			for possibility in possibilities[row][column]:
				entrystring += str(possibility)
			rowstring += entrystring.zfill(9) + " "
		print rowstring
	print

def rawPossibilities():
	rawPossibilities = []
	for i in range(0,9):
		rawPossibilities.append([])
		for j in range(0,9):
			rawPossibilities[i].append(range(1,10))
	return rawPossibilities

def duplicate3dList(A):
	out = []
	for i in range(len(A)):
		out.append([])
		for j in range(len(A[i])):
			out[i].append([])
			for k in range(len(A[i][j])):
				out[i][j].append(A[i][j][k])
	return out

def isPossibility(puzzle, row, col, value):
	if puzzle.data()[row][col] != 0:
		return False
	elif puzzle.row(row).count(value) != 0:
		return False
	elif puzzle.column(col).count(value) != 0:
		return False
	elif puzzle.square(row, col).count(value) != 0:
		return False
	return True

def logicSolve2(puzzle):
	changes = False
	for row in range(9):
		therow = puzzle.row(row)
		for value in range(1,10):
			if therow.count(value) == 0:
				possiblePlaces = []
				for position in range(9):
					if isPossibility(puzzle, row, position, value):
						possiblePlaces.append(position)
				if len(possiblePlaces) == 1:
					puzzle.newEntry(row, possiblePlaces[0], value)
					changes = True
					#print "rowchange: ", row, possiblePlaces[0], value
				elif len(possiblePlaces) == 0:
					#print "logic 2 conflict at", row, possiblePlaces[0], value
					return [puzzle, True, False]
	for col in range(9):
		thecol = puzzle.column(col)
		for value in range(1,10):
			if thecol.count(value) == 0:
				possiblePlaces = []
				for position in range(9):
					if isPossibility(puzzle, position, col, value):
						possiblePlaces.append(position)
				if len(possiblePlaces) == 1:
					puzzle.newEntry(possiblePlaces[0], col, value)
					changes = True
					#print "colchange: ", possiblePlaces[0], col, value
				elif len(possiblePlaces) == 0:
					#print "logic 2 conflict at", possiblePlaces[0], col, value
					return [puzzle, True, False]
	for square in range(9):
		thesquare = puzzle.square((square/3)*3, (square%3)*3)
		for value in range(1,10):
			if thesquare.count(value) == 0:
				possiblePlaces = []
				for position in range(9):
					if isPossibility(puzzle, (square/3)*3 + position/3, (square%3)*3 + position%3, value):
						possiblePlaces.append(position)
				if len(possiblePlaces) == 1:
					puzzle.newEntry((square/3)*3 + possiblePlaces[0]/3, (square%3)*3 + possiblePlaces[0]%3, value)
					changes = True
					#print "squchange: ", (square/3)*3 + possiblePlaces[0]/3, (square%3)*3 + possiblePlaces[0]%3, value
				elif len(possiblePlaces) == 0:
					#print "logic 2 conflict at", (square/3)*3 + possiblePlaces[0]/3, (square%3)*3 + possiblePlaces[0]%3, value
					return [puzzle, True, False]
	return [puzzle, changes, True]

def logicSolve1(puzzle, possibilities):
	changes = False
	for i in range(9):
		for j in range(9):
			if puzzle.data()[i][j] == 0:
				if len(possibilities[i][j]) > 1:
					for number in puzzle.row(i) + puzzle.column(j) + puzzle.square(i,j):
						if number != 0:
							if possibilities[i][j].count(number) != 0:
								possibilities[i][j].remove(number)
				if len(possibilities[i][j]) == 1:
					puzzle.newEntry(i,j,possibilities[i][j][0])
					changes = True
				elif len(possibilities[i][j]) == 0:
					#print "logic 1 conflict at ", i, j
					return [puzzle, possibilities, True, False]
	return [puzzle, possibilities, changes, True]

def solve(puzzle, possibilities, depth):
	while not puzzle.complete():
		#puzzle.output()
		[puzzle, possibilities, changes1, noConflicts] = logicSolve1(puzzle, possibilities)
		[puzzle, changes2, noConflicts2] = logicSolve2(puzzle)
		if not noConflicts or not noConflicts2:
			print "AA"
			return [puzzle, False]
		#print "changes: ", changes1, changes2
		if not changes1 and not changes2:
			print "BB"
			for i in range(9):
				row = puzzle.row(i)
				if row.count(0) != 0:
					j = row.index(0)
					break
			for value in possibilities[i][j]:
				print " " * depth, "guess ", i, j, value, "/", possibilities[i][j]
				duplicatePossibilities = duplicate3dList(possibilities)
				duplicatePossibilities[i][j] = [value]
				duplicatePuzzle = Sudoku(puzzle.toStringRows())
				duplicatePuzzle.newEntry(i, j, value)
				[duplicatePuzzle, noConflicts] = solve(duplicatePuzzle, duplicatePossibilities, depth + 1)
				if noConflicts:
					puzzle = duplicatePuzzle
					return [puzzle, True]
			return [puzzle, False]
	#print "solve method returned without conflicts"
	print "CC"
	print puzzle.complete()
	return [puzzle, True]


rawpuzzles = [["070001930","140500020","000000800","000002100","700000083","006400000","000000300","020007054","459100000"]]
#rawpuzzles = [["003020600","900305001","001806400","008102900","700000008","006708200","002609500","800203009","005010300"],["200080300","060070084","030500209","000105408","000000000","402706000","301007040","720040060","004010003"],["000000907","000420180","000705026","100904000","050000040","000507009","920108000","034059000","507000000"],["030050040","008010500","460000012","070502080","000603000","040109030","250000098","001020600","080060020"],["020810740","700003100","090002805","009040087","400208003","160030200","302700060","005600008","076051090"],["100920000","524010000","000000070","050008102","000000000","402700090","060000000","000030945","000071006"],["043080250","600000000","000001094","900004070","000608000","010200003","820500000","000000005","034090710"],["480006902","002008001","900370060","840010200","003704100","001060049","020085007","700900600","609200018"],["000900002","050123400","030000160","908000000","070000090","000000205","091000050","007439020","400007000"],["001900003","900700160","030005007","050000009","004302600","200000070","600100030","042007006","500006800"],["000125400","008400000","420800000","030000095","060902010","510000060","000003049","000007200","001298000"],["062340750","100005600","570000040","000094800","400000006","005830000","030000091","006400007","059083260"],["300000000","005009000","200504000","020000700","160000058","704310600","000890100","000067080","000005437"],["630000000","000500008","005674000","000020000","003401020","000000345","000007004","080300902","947100080"],["000020040","008035000","000070602","031046970","200000000","000501203","049000730","000000010","800004000"],["361025900","080960010","400000057","008000471","000603000","259000800","740000005","020018060","005470329"],["050807020","600010090","702540006","070020301","504000908","103080070","900076205","060090003","080103040"],["080005000","000003457","000070809","060400903","007010500","408007020","901020000","842300000","000100080"],["003502900","000040000","106000305","900251008","070408030","800763001","308000104","000020000","005104800"],["000000000","009805100","051907420","290401065","000000000","140508093","026709580","005103600","000000000"],["020030090","000907000","900208005","004806500","607000208","003102900","800605007","000309000","030020050"],["005000006","070009020","000500107","804150000","000803000","000092805","907006000","030400010","200000600"],["040000050","001943600","009000300","600050002","103000506","800020007","005000200","002436700","030000040"],["004000000","000030002","390700080","400009001","209801307","600200008","010008053","900040000","000000800"],["360020089","000361000","000000000","803000602","400603007","607000108","000000000","000418000","970030014"],["500400060","009000800","640020000","000001008","208000501","700500000","000090084","003000600","060003002"],["007256400","400000005","010030060","000508000","008060200","000107000","030070090","200000004","006312700"],["000000000","079050180","800000007","007306800","450708096","003502700","700000005","016030420","000000000"],["030000080","009000500","007509200","700105008","020090030","900402001","004207100","002000800","070000090"],["200170603","050000100","000006079","000040700","000801000","009050000","310400000","005000060","906037002"],["000000080","800701040","040020030","374000900","000030000","005000321","010060050","050802006","080000000"],["000000085","000210009","960080100","500800016","000000000","890006007","009070052","300054000","480000000"],["608070502","050608070","002000300","500090006","040302050","800050003","005000200","010704090","409060701"],["050010040","107000602","000905000","208030501","040070020","901080406","000401000","304000709","020060010"],["053000790","009753400","100000002","090080010","000907000","080030070","500000003","007641200","061000940"],["006080300","049070250","000405000","600317004","007000800","100826009","000702000","075040190","003090600"],["005080700","700204005","320000084","060105040","008000500","070803010","450000091","600508007","003010600"],["000900800","128006400","070800060","800430007","500000009","600079008","090004010","003600284","001007000"],["000080000","270000054","095000810","009806400","020403060","006905100","017000620","460000038","000090000"],["000602000","400050001","085010620","038206710","000000000","019407350","026040530","900020007","000809000"],["000900002","050123400","030000160","908000000","070000090","000000205","091000050","007439020","400007000"],["380000000","000400785","009020300","060090000","800302009","000040070","001070500","495006000","000000092"],["000158000","002060800","030000040","027030510","000000000","046080790","050000080","004070100","000325000"],["010500200","900001000","002008030","500030007","008000500","600080004","040100700","000700006","003004050"],["080000040","000469000","400000007","005904600","070608030","008502100","900000005","000781000","060000010"],["904200007","010000000","000706500","000800090","020904060","040002000","001607000","000000030","300005702"],["000700800","006000031","040002000","024070000","010030080","000060290","000800070","860000500","002006000"],["001007090","590080001","030000080","000005800","050060020","004100000","080000030","100020079","020700400"],["000003017","015009008","060000000","100007000","009000200","000500004","000000020","500600340","340200000"],["300200000","000107000","706030500","070009080","900020004","010800050","009040301","000702000","000008006"]]
numbers = []


depth = 0
c = 0
puzzle = Sudoku(rawpuzzles[0])
for rawpuzzle in rawpuzzles:
	print "new puzzle", c
	puzzle.newPuzzle(rawpuzzle)
	puzzle.output()
	possibilities = rawPossibilities()
	for i in range(9):
		for j in range(9):
			if puzzle.data()[i][j] != 0:
				possibilities[i][j] = [puzzle.data()[i][j]]
	[puzzle, noConflicts] = solve(puzzle, possibilities, depth)
	numbers.append(puzzle.theNumber())
	print "answer"
	puzzle.output()
	c += 1

#output
print sum(numbers)









