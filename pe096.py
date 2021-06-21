from copy import deepcopy as copy

testboard = '''
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300'''


alldigits = range(1,10)

class Board:

	def __init__(self, boardstr):
		# Remove newlines, then convert each char to:
		# 0 -> list of all possibles
		# _ -> list containing char converted to int

		self.board = [[int(char)] if char != "0" else list(alldigits) for char in "".join(boardstr.split("\n"))]

	def __str__(self):
		res = ""
		for i in range(9):
			res += str(self.board[9*i:9*(i+1)]) + "\n\n"
		return res

	# Get list of row contents, r is 0-indexed
	def getrow(self, r):
		return self.board[9*r:9*(r+1)]

	# Get list of col contents, c is 0-indexed
	def getcol(self, c):
		return self.board[c::9]

	# Get list of box contents, b is 0-indexed
	def getbox(self, b):
		startcol = b%3 * 3
		startrow = b//3 * 3
		idx = startrow*9 + startcol # Index of top left cell of box
		return self.board[idx:idx+3] + self.board[idx+9:idx+12] + self.board[idx+18:idx+21] 

	def checkvalid(self):
		return [] not in self.board
	
	# Get values of solved cells in a given list
	def getsolved(self, cells):
		return [cell[0] for cell in cells if len(cell) == 1]

	# Get correct list of possibles for specified cell
	def getpossibles(self, r, c):
		b = r//3 * 3 + c//3
		solved = self.getsolved(self.getrow(r) + self.getcol(c) + self.getbox(b))
		return sorted(list(set(alldigits) - set(solved)))

	# Set possibles for all cells
	def initpossibles(self):
		for idx in range(len(self.board)):
			if len(self.board[idx]) > 1:
				self.board[idx] = self.getpossibles(idx//9, idx%9)

	def checksolved(self):
		return len([cell for cell in self.board if len(cell) != 1]) == 0

	# Enter a digit, removing conflicting possibles
	def setdigit(self, r, c, digit):
		idx = 9*r + c

		# Make sure the digit is one of the possibles and that cell is not already solved
		assert(len(self.board[idx]) > 1 and digit in self.board[idx])

		rowidx = list(range(9*r,9*(r+1)))
		colidx = list(range(c,81,9))

		bxidx = r//3*3 *9 + c//3*3
		boxidx = list(range(bxidx,bxidx+3)) + list(range(bxidx+9,bxidx+12)) + list(range(bxidx+18,bxidx+21))

		#Remove from all affected cells
		for i in rowidx + colidx + boxidx:
			if i != idx and digit in self.board[i]:
				self.board[i].remove(digit)

		self.board[idx] = [digit]

def trySolve(b):

	if b.checksolved():
		# Done! Return solved board
		return b

	if not b.checkvalid():
		# Invalid! Backtrack
		return None

	possiblenums = [len(cell) if len(cell) > 1 else 999 for cell in b.board]

	idx = possiblenums.index(min(possiblenums))

	for digit in b.board[idx]:
		b_new = copy(b)

		b_new.setdigit(idx//9, idx%9, digit)

		res = trySolve(b_new)

		if res != None:
			return res

	#Exhausted all options
	return None