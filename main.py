import pygame
from character_class import character
from random import choice
import time

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Simple Fight Generator")
win.fill((0, 0, 0))

font = pygame.font.SysFont('arial', 16)

def main():
	# characters are rect with different colors
	#name, hp, atk, armor, magic, color, x, y
	character1 = character("Zollak (red) ", 200, choice([*range(10, 30)]), choice([*range(0, 10)]), ["fireball", "lighning bolt"], (255,0,0), 0, 0)
	character2 = character("Kallin (green) ", 200, choice([*range(10, 30)]), choice([*range(0, 10)]), ["iceball", "Volcanic Strike"], (0,255,0), 0, 0)

	chars = [character1, character2]

	#set random location for each character
	for i in chars:
		x = choice([*range(0, 500)])
		y = choice([*range(0, 400)])

		pygame.draw.rect(win, i.color, (x, y, 20, 20))

		i.x = x
		i.y = y

	while True:
		
		#decide who gots the next move
		who_attacks = choice([*range(1, 2)])

		#char 1 move
		if(who_attacks == 1):

			action = choice([*range(1, 2)])

			#action 1 = move
			if action == 1:
				#decide if it moves on x or y
				x_or_y = choice([*range(1, 3)])
				
				# 1 = x , 2 = y
				if x_or_y == 1:
					
					#decide left or right
					left_right = choice([*range(1, 3)])

					#left
					if left_right == 1:

						if (character1.x < 500 and (character1.x + 5) < 500):
							temp_x = character1.x
							character1.x += 5

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_x = character1.x
							character1.x -= 5

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(0,101)])
						if (attack % 2) == 0:
							damage = character1.atk - character1.armor
							character2.hp -= damage

					#right
					elif left_right == 2:

						if (character1.x > 0 and (character1.x - 5) > 0):
							temp_x = character1.x
							character1.x -= 5

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_x = character1.x
							character1.x += 5

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

				elif x_or_y == 2:

					#decide up or down
					up_down = choice([*range(1, 3)])

					#up
					if up_down == 1:

						if (character1.y < 400 and (character1.y + 5) < 400):

							temp_y = character1.y
							character1.y += 5

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_y = character1.y
							character1.y -= 5

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

					#down
					elif up_down == 2:

						if (character1.y > 0 and (character1.y - 5) > 0):
							temp_y = character1.y
							character1.y -= 5

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_y = character1.y
							character1.y += 5

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
			#action 2 = use potion
			# elif action == 2:

			# 	basicfont = pygame.font.SysFont("arial", 16)

			# 	text = basicfont.render(character1.name + 'used magic', True, (255, 0, 0), (0, 0, 0))
			# 	textrect = text.get_rect()
			# 	textrect.center = (250, 450)

			# 	win.blit(text, textrect)

			# 	time.sleep(10)
			# 	win.fill((0, 0, 0))
			# 	for i in chars:

			# 		pygame.draw.rect(win, i.color, (i.x, i.y, 20, 20))


		pygame.display.update()
		

if __name__ == "__main__":
	main()
