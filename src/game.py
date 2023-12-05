import pygame
from gameBoard import GameBoard

class Game():
	"""docstring for Game"""
	def __init__(self, width=600, height=500):
		self.window_width = width
		self.window_height = height
		self.is_running = True
		self.clock = pygame.time.Clock()
		self.set_screen_dimensions(self.window_width, self.window_height)
		self.bg_rgb_color = (50, 168, 133)
		self.set_screen_background_color(self.bg_rgb_color)
		self.board_line_color = (35, 36, 35)
		self.line_margin = .2
		self.line_width = 4

		self.game_board = GameBoard()
		self.current_player = "X"


	def start(self):
		pygame.init()

		while self.is_running:
			self.set_screen_background_color(self.bg_rgb_color)
			self.draw_board()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_running = False

				if event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						# TODO: Update clicked square here. 
						index = self.get_index_from_click(event.pos[0], event.pos[1])

						if 0 <= index < 9:
							self.game_board.update_board(self.current_player, index)
							print(self.game_board.board)
							if self.game_board.check_for_win(self.current_player):
								print("Win")
							
							self.current_player = "X" if self.current_player == "O" else "O"


						



			pygame.display.flip()
			self.clock.tick(60)

			

		pygame.quit()


	def set_screen_dimensions(self, width:int, height: int):
		# TODO: Should check edge cases here. 
		self.screen = pygame.display.set_mode((width, height))


	def set_screen_background_color(self, color: tuple):
		self.screen.fill(color)

	def draw_board(self):
		# 10% gap. 5% off top and bottom

		percent_of_height = self.window_height*self.line_margin
		percent_of_width = self.window_width*self.line_margin
		height_divider = (self.window_height-percent_of_height)/3
		width_divider = (self.window_width-percent_of_width)/3
		horizontal_line_end = self.window_width-percent_of_width/2
		vertical_line_end = self.window_height-percent_of_height/2


		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			(percent_of_width/2,(height_divider+percent_of_height/2)), 
			(horizontal_line_end, height_divider+percent_of_height/2),
			self.line_width
		)

		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			(percent_of_width/2,(height_divider*2+percent_of_height/2)), 
			(horizontal_line_end, height_divider*2+percent_of_height/2),
			self.line_width
		)


		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			((width_divider*2)+percent_of_width/2,percent_of_height/2), 
			(width_divider*2+percent_of_width/2, vertical_line_end),
			self.line_width
		)

		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			((width_divider)+percent_of_width/2,percent_of_height/2), 
			(width_divider+percent_of_width/2, vertical_line_end),
			self.line_width
		)

	def get_index_from_click(self, width, height):
		print(f'Mouse left clicked at {height, width}')

		col = self.get_col_clicked(width)
		row = self.get_row_clicked(height)
		

		print(row, col)

		if row == -1 or col == -1:
			print(-1)
			return -1
		
		print("Index: ", row * 3 + col)
		return row * 3 + col
		

	def get_col_clicked(self, col):
		
		percent_of_width = self.window_width*self.line_margin
		width_divider = (self.window_width-percent_of_width)/3
		x2 = (width_divider)+percent_of_width/2
		x3 = (width_divider*2)+percent_of_width/2
		x1 = x2 - (x3-x2)
		x4 = x3 + (x3-x2)

		if x1 < col < x2:
			return 0
		elif x2 < col < x3:
			return 1
		elif x3 < col < x4:
			return 2

		return -1

	def get_row_clicked(self, row):
		percent_of_height = self.window_height*self.line_margin
		height_divider = (self.window_height-percent_of_height)/3
		
		y2 = height_divider+percent_of_height/2
		y3 = height_divider*2+percent_of_height/2
		y1 = y2 - (y3-y2)
		y4 = y3 + (y3-y2)

		if y1 < row < y2:
			return 0
		elif y2 < row < y3:
			return 1
		elif y3 < row < y4:
			return 2

		return -1






	
	
