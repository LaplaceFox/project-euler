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

		assert(len(self.board) == 81)

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

	# method for entering a number that automatically removes possibles

	# method that calculates possibles for a given cell