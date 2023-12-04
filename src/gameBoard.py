from gameBoard import GameBoard
class GameBoard(object):
	"""
	Object representation of the game board. 
	"""
	def __init__(self):
		self.board = [0,0,0,0,0,0,0,0,0]
		self.win_options_indexes = [
									(0,1,2),(3,4,5),(6,7,8),
									(0,3,6),(1,4,7),(2,5,8),
									(0,4,8),(2,4,6)
								   ]


	def check_for_win(self, letter) -> bool:
		"""
		Check if win condition is met. 

		Checks the indexes of the board to see if the a condition
		is met that will end the game for either the letter X or O.

		Parameters
	    ----------
	    letter : char
	        Can be either X or O. 
		"""
		for i,j,k in self.win_options_indexes:
			if letter == board[i] == board[j] == board[k]:
				return True

		return False



	def update_board(self, letter, index) -> bool:
		"""
		Update board state.

		Checks if it is okay to put an let in a perticular index
		of the board. If it is possilbe place the letter there else
		return a failure response.

		Parameters
	    ----------
	    letter : char
	        The letter to add to the board. This is either X or O
	    index : int
	        The index to add the letter to. 

	    Returns
	    -------
	    bool
	    	False: Adding the character to the board was unsuccessful
	    	True: Adding the character to the board was successful 
		"""
		if index < 0 or index > 8:
			return False

		elif board[index] != 0:
			return False

		else:
			board[index] = letter

		return True
