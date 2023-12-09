import pygame
from gameBoard import GameBoard
from gameLines import Line
from gameWindow import Window
from characterO import O
from characterX import X
class Game():
	"""docstring for Game"""
	def __init__(self, width=600, height=500):
		self.window = Window(width, height)
		self.is_running = True
		self.clock = pygame.time.Clock()
		self.set_screen_dimensions(self.window.get_width(), self.window.get_height())
		self.set_screen_background_color(self.window.get_bg_color())

		self.grid_lines = Line((35, 36, 35), 4, 0.2)


		self.game_board = GameBoard()
		self.current_player = "X"
		self.placed_characters = list()


	def start(self):
		pygame.init()

		while self.is_running:
			self.set_screen_background_color(self.window.get_bg_color())
			self.draw_board()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_running = False

				if event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						# TODO: Update clicked square here. 
						index, *grid_data = self.get_index_from_click(event.pos[0], event.pos[1])

						if 0 <= index < 9:
							if self.game_board.update_board(self.current_player, index):
								print(self.game_board.board)
								if self.current_player == "X":
									top_left = (grid_data[0], grid_data[2])
									top_right = ( grid_data[1], grid_data[2])
									bottom_left = (grid_data[0], grid_data[3])
									bottom_right = ( grid_data[1], grid_data[3])
									self.placed_characters.append(("X", X(top_left, top_right, bottom_left, bottom_right)))

								if self.current_player == "O":
									# find center 
									# find radius
									center_x = ( grid_data[1] + grid_data[0] ) / 2
									center_y = ( grid_data[3] + grid_data[2] ) / 2

									diff_x = grid_data[1] - grid_data[0]
									diff_y = grid_data[3] - grid_data[2]

									radius = .7 * min(diff_x, diff_y)/2
									center = (center_x, center_y)

									self.placed_characters.append(("O", O(center, radius)))



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

		percent_of_height = self.window.get_height() * self.grid_lines.margin
		percent_of_width = self.window.get_width() * self.grid_lines.margin
		height_divider = ( self.window.get_height() - percent_of_height ) / 3
		width_divider = ( self.window.get_width() - percent_of_width ) / 3
		horizontal_line_end = self.window.get_width() - percent_of_width / 2
		vertical_line_end = self.window.get_height() - percent_of_height/2


		pygame.draw.line(
			self.screen, 
			self.grid_lines.color, 
			(percent_of_width/2,(height_divider+percent_of_height/2)), 
			(horizontal_line_end, height_divider+percent_of_height/2),
			self.grid_lines.width
		)

		pygame.draw.line(
			self.screen, 
			self.grid_lines.color, 
			(percent_of_width/2,(height_divider*2+percent_of_height/2)), 
			(horizontal_line_end, height_divider*2+percent_of_height/2),
			self.grid_lines.width
		)


		pygame.draw.line(
			self.screen, 
			self.grid_lines.color, 
			((width_divider*2)+percent_of_width/2,percent_of_height/2), 
			(width_divider*2+percent_of_width/2, vertical_line_end),
			self.grid_lines.width
		)

		pygame.draw.line(
			self.screen, 
			self.grid_lines.color, 
			((width_divider)+percent_of_width/2,percent_of_height/2), 
			(width_divider+percent_of_width/2, vertical_line_end),
			self.grid_lines.width
		)

		for chara, data in self.placed_characters:
			if chara == "O":
				pygame.draw.circle(self.screen, data.color, data.center, data.radius, data.width)
			else:
				pygame.draw.line(self.screen, data.color, data.coord_t_left, data.coord_b_right, data.width)
				pygame.draw.line(self.screen, data.color, data.coord_t_right, data.coord_b_left, data.width)

	def get_index_from_click(self, width, height):
		print(f'Mouse left clicked at {height, width}')

		col, left, right = self.get_col_clicked(width)
		row, top, bottom = self.get_row_clicked(height)
		

		print(row, col)

		if row == -1 or col == -1:
			return -1, -1 
		
		print("Index: ", row * 3 + col)
		return row * 3 + col, left, right, top, bottom
		

	def get_col_clicked(self, col):
		
		percent_of_width = self.window.get_width() * self.grid_lines.margin 
		width_divider = ( self.window.get_width() - percent_of_width ) / 3
		x2 = (width_divider)+percent_of_width/2
		x3 = (width_divider*2)+percent_of_width/2
		x1 = x2 - (x3-x2)
		x4 = x3 + (x3-x2)

		if x1 < col < x2:
			return 0, x1, x2
		elif x2 < col < x3:
			return 1, x2, x3
		elif x3 < col < x4:
			return 2, x3, x4

		return -1, -1, -1

	def get_row_clicked(self, row):
		percent_of_height = self.window.get_height() * self.grid_lines.margin
		height_divider = ( self.window.get_height() - percent_of_height ) / 3
		
		y2 = height_divider+percent_of_height/2
		y3 = height_divider*2+percent_of_height/2
		y1 = y2 - (y3-y2)
		y4 = y3 + (y3-y2)

		if y1 < row < y2:
			return 0, y1, y2
		elif y2 < row < y3:
			return 1, y2, y3
		elif y3 < row < y4:
			return 2, y3, y4

		return -1, -1, -1







	
	
