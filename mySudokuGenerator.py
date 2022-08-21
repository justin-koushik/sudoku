from random import shuffle,choice
from copy import deepcopy
class sudoku:
	def __init__(self,board=None):
		self.board=board
		self.util=[*range(1,10)]
		self.seen=[]
		if self.board is None:
			self.generate()
		else:
			self.Solve()
	def isValid(self,num,i,j):
		if num in self.board[i]:
			return 0
		if num in [self.board[x][j] for x in range(9)]:
			return 0
		y=3*(i//3)
		x=3*(j//3)
		for i in range(y,y+3):
			for j in range(x,x+3):
				if num==self.board[i][j]:
					return 0
		return 1
	def fill(self):
		for n in range(0,7,3):
			shuffle(self.util)
			temp=iter(self.util)
			for i in range(3):
				for j in range(3):
					self.board[n+i][n+j]=next(temp)
		self.sol=[]
		self.possibleSol=0
		self.Solve()
		self.board=deepcopy(self.sol)
	def getRandomSpot(self):
		spots=[]
		for i in range(9):
			for j in range(9):
				if not (i,j) in self.seen:
					if self.board[i][j]:
						spots.append((i,j))
		return choice(spots)
	def empty(self):
		c=0
		for i in self.board:
			for j in i:
				if j==0:
					c+=1
		return c
	def setanti(self,y=0,x=0):
		for i in range(y,9):
			for j in range(x,9-i):
				if self.board[i][j]:
					self.board[i][j]=0
					self.board[8-i][8-j]=0
					self.Solve()
					if self.possibleSol>1:
						self.board[i][j]=self.sol[i][j]
						self.board[8-i][8-j]=self.sol[8-i][8-j]
						self.setanti(i,j+1)
					if self.board[i][i]:
						self.possibleSol=0
						self.board[i][i]=0
						self.Solve()
						if self.possibleSol>1:
							self.board[i][i]=self.sol[i][i]		
	def setDiag(self,y=0,x=0):
		self.possibleSol=0
		for i in range(y,9):
			self.possibleSol=0
			for j in range(x+i+1,9):
				if self.board[i][j]:
					self.board[i][j]=0
					self.board[j][i]=0
					self.Solve()
					if self.possibleSol>1:
						self.board[i][j]=self.sol[i][j]
						self.board[j][i]=self.sol[j][i]
						self.setDiag(i,j+1)
					if self.board[i][i]:
						self.possibleSol=0
						self.board[i][i]=0
						self.Solve()
						if self.possibleSol>1:
							self.board[i][i]=self.sol[i][i]
	def setBoard(self,y=0,x=0):
		self.possibleSol=0
		for i in range(y,9):
			for j in range(x,9):
				if self.board[i][j]:
					self.board[i][j]=0
					self.Solve()
					if self.possibleSol>1:
						self.board[i][j]=self.sol[i][j]
						self.setBoard(i,j+1)
	def generate(self):
		self.board=[[0 for i in range(9)] for j in range(9)]
		self.fill()
		self.setDiag()
	def Solve(self):
		if self.possibleSol>1:
			return 
		for i in range(9):
			for j in range(9):
				if not self.board[i][j]:
					for num in self.util:
						if self.isValid(num,i,j):
							self.board[i][j]=num
							self.Solve()
							self.board[i][j]=0
					return
		if not self.sol:
			self.sol=deepcopy(self.board)
		self.possibleSol+=1
		return 
def isValid(board,num,i,j):
	if num in board[i]:
		return 0
	if num in [board[x][j] for x in range(9)]:
		return 0
	y=3*(i//3)
	x=3*(j//3)
	for i in range(y,y+3):
		for j in range(x,x+3):
			if num == board[i][j]:
				return 0
	return 1
def solve(board):
	for i in range(9):
		for j in range(9):
			if not board[i][j]:
				for k in range(1,10):
					if isValid(board,k,i,j):
						board[i][j]=k
						solve(board)
						board[i][j]=0
				return
	printBoard(board)
	return 
def printBoard(board):
	print("\n")
	for i in range(9):
		print("   ",end=" ")
		for j in range(9):
			if j>0 and j%3==0:
				print("|",end="   ")
			k=board[i][j]
			k=str(k) if k else "."
			if k.isdigit():
				k="\033[1m"+k+"\033[0m"
			print(k,end="   ")
		if (i+1)%3==0 and i+1<9:
			print("\n")
			print("   ",end=" ")
			for k in range(9):
				print("_",end="   ")
				if k<8 and (k+1)%3==0:
					print("+",end="   ")
		print("\n")
if __name__=="__main__":
	a=sudoku()
	diag=a.board
	printBoard(diag)
	solve(diag)

#piecom
	