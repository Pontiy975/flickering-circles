import arcade
import random
import time


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
SCREEN_TITLE = 'Flickering Circles'

CIRCLE_SIZE = 20
MIN = 22
MAX = 22


class Game(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		arcade.set_background_color(arcade.color.BLACK)

		self.circles = []

	def setup(self):
		width = random.randint(MIN + 1, MAX + 1)
		height = random.randint(MIN + 1, MAX + 1)

		for i in range(width):
			self.circles.append([])
			for j in range(height):
				self.circles[i].append(random.randint(0, 2))

	# def update(self, delta_time):
	# 	for line in self.circles:
	# 		for circle in line:
	# 			if circle == 2:
	# 				circle = 0
	# 			else:
	# 				circle += 1

	def on_draw(self):
		arcade.start_render()

		for i in range(len(self.circles)):
			for j in range(len(self.circles[i])):
				if self.circles[i][j] == 0:
					arcade.draw_circle_filled(CIRCLE_SIZE * (i+1), CIRCLE_SIZE * (j+1),
											  CIRCLE_SIZE / 2, arcade.color.GOLDEN_YELLOW)
				elif self.circles[i][j] == 1:
					arcade.draw_circle_filled(CIRCLE_SIZE * (i + 1), CIRCLE_SIZE * (j + 1),
											  CIRCLE_SIZE / 2, arcade.color.SELECTIVE_YELLOW)
				elif self.circles[i][j] == 2:
					arcade.draw_circle_filled(CIRCLE_SIZE * (i + 1), CIRCLE_SIZE * (j + 1),
											  CIRCLE_SIZE / 2, arcade.color.INDIAN_YELLOW)

				if self.circles[i][j] == 2:
					self.circles[i][j] = 0
				else:
					self.circles[i][j] += 1


if __name__ == '__main__':
	root = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	root.setup()

	arcade.run()
