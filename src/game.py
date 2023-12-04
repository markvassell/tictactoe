import pygame

class Game():
	"""docstring for Game"""
	def __init__(self, width=500, height=500):
		self.window_width = width
		self.window_height = height
		self.is_running = True
		self.clock = pygame.time.Clock()
		self.set_screen_dimensions(self.window_width, self.window_height)
		self.bg_rgb_color = (50, 168, 133)
		self.set_screen_background_color(self.bg_rgb_color)
		self.board_line_color = (35, 36, 35)


	def start(self):
		pygame.init()

		while self.is_running:
			self.set_screen_background_color(self.bg_rgb_color)
			self.draw_board()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_running = False


			pygame.display.flip()
			self.clock.tick(60)

			

		pygame.quit()


	def set_screen_dimensions(self, width:int, height: int):
		# TODO: Should check edge cases here. 
		self.screen = pygame.display.set_mode((width, height))


	def set_screen_background_color(self, color: tuple):
		self.screen.fill(color)

	def draw_board(self): 
		height_divider = (self.window_height-50)/3
		width_divider = (self.window_width-50)/3
		horizontal_line_end = self.window_width-25
		vertical_line_end = self.window_height-25

		line_width = 4

		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			(25,(height_divider+25)), 
			(horizontal_line_end, height_divider+25),
			line_width
		)

		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			(25,(height_divider*2+25)), 
			(horizontal_line_end, height_divider*2+25),
			line_width
		)


		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			((width_divider*2)+25,25), 
			(width_divider*2+25, vertical_line_end),
			line_width
		)

		pygame.draw.line(
			self.screen, 
			self.board_line_color, 
			((width_divider)+25,25), 
			(width_divider+25, vertical_line_end),
			line_width
		)









	
	
