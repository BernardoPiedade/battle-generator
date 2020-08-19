import pygame
from character_class import character
from random import choice
import time

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Simple Fight Generator")
win.fill((0, 0, 0))

def new_scene(chars, character1, character2):
	win.fill((0, 0, 0))

	basicfont = pygame.font.SysFont("arial", 16)

	char1_text = basicfont.render(character1.name + 'HP: ' + str(character1.hp), True, (255, 0, 0), (0, 0, 0))
	char1_textrect = char1_text.get_rect()
	char1_textrect.center = (63, 420)

	win.blit(char1_text, char1_textrect)

	char2_text = basicfont.render(character2.name + 'HP: ' + str(character2.hp), True, (0, 255, 0), (0, 0, 0))
	char2_textrect = char2_text.get_rect()
	char2_textrect.center = (430, 420)

	win.blit(char2_text, char2_textrect)

	for i in chars:
		pygame.draw.rect(win, i.color, (i.x, i.y, 20, 20))

def winner(character):
	win.fill((0, 0, 0))

	basicfont = pygame.font.SysFont("arial", 16)

	winner_text = basicfont.render(character.name + ' Wins!', True, (255, 0, 0), (0, 0, 0))
	winner_textrect = winner_text.get_rect()
	winner_textrect.center = (250, 250)


def main():
	# characters are rect with different colors
	#name, hp, atk, armor, magic, color, x, y
	character1 = character("Zollak (red) ", 50, choice([*range(10, 30)]), choice([*range(5, 10)]), ["fireball", "lighning bolt"], (255,0,0), 0, 0)
	character2 = character("Kallin (green) ", 50, choice([*range(10, 30)]), choice([*range(5, 10)]), ["iceball", "Volcanic Strike"], (0,255,0), 0, 0)

	chars = [character1, character2]

	#set random location for each character
	for i in chars:
		x = choice([*range(10, 490)])
		y = choice([*range(10, 400)])

		pygame.draw.rect(win, i.color, (x, y, 20, 20))

		i.x = x
		i.y = y

	basicfont = pygame.font.SysFont("arial", 16)


	char1_text = basicfont.render(character1.name + 'HP: ' + str(character1.hp), True, (255, 0, 0), (0, 0, 0))
	char1_textrect = char1_text.get_rect()
	char1_textrect.center = (63, 420)

	win.blit(char1_text, char1_textrect)

	char2_text = basicfont.render(character2.name + 'HP: ' + str(character2.hp), True, (0, 255, 0), (0, 0, 0))
	char2_textrect = char2_text.get_rect()
	char2_textrect.center = (430, 420)

	win.blit(char2_text, char2_textrect)

	num_round = 0
	used_pot = []

	while True:
		time.sleep(0.3)
		num_round+1

		if(num_round == 4):
			used_pot.clear()

		if(character1.hp <= 0):
			winner(character1)
			break
		elif (character2.hp <= 0):
			winner(character2)
			break

		#decide who gots the next move
		who_attacks = choice([*range(1, 3)])

		#char 1 move
		if(who_attacks == 1):

			action = choice([*range(1, 4)])

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

						if (character1.x < 490 and (character1.x + 5) < 490):
							temp_x = character1.x
							character1.x += 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_x = character1.x
							character1.x -= 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character2.armor
							defence = choice([*range(0, d)])
							damage = character1.atk - defence
							character2.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character1.name + 'used magic to hit with ' + str(damage), True, (255, 0, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)

					#right
					elif left_right == 2:

						if (character1.x > 10 and (character1.x - 5) > 10):
							temp_x = character1.x
							character1.x -= 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_x = character1.x
							character1.x += 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character1.y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character2.armor
							defence = choice([*range(0, d)])
							damage = character1.atk - defence
							character2.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character1.name + 'used magic to hit with ' + str(damage), True, (255, 0, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)

				elif x_or_y == 2:

					#decide up or down
					up_down = choice([*range(1, 3)])

					#up
					if up_down == 1:

						if (character1.y < 400 and (character1.y + 5) < 400):

							temp_y = character1.y
							character1.y += 25

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_y = character1.y
							character1.y -= 25

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character2.armor
							defence = choice([*range(0, d)])
							damage = character1.atk - defence
							character2.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character1.name + 'used magic to hit with ' + str(damage), True, (255, 0, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)

					#down
					elif up_down == 2:

						if (character1.y > 10 and (character1.y - 5) > 10):
							temp_y = character1.y
							character1.y -= 25

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)
						else:
							temp_y = character1.y
							character1.y += 25

							pygame.draw.rect(win, (0,0,0), (character1.x, temp_y, 20, 20))
							pygame.draw.rect(win, character1.color,(character1.x, character1.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character2.armor
							defence = choice([*range(0, d)])
							damage = character1.atk - defence
							character2.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character1.name + 'used magic to hit with ' + str(damage), True, (255, 0, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)
								

			#action 2 = use potion
			elif action == 2:
				for i in used_pot:
					if character1.name is not i:
						if (character1.hp < 150):

							if(character1.hp >= 150):
								basicfont = pygame.font.SysFont("arial", 16)

								text = basicfont.render(character1.name + 'tried to use a potion but his HP is full', True, (0, 255, 0), (0, 0, 0))
								textrect = text.get_rect()
								textrect.center = (250, 470)

								win.blit(text, textrect)
								pygame.display.update()
								time.sleep(1)
								new_scene(chars, character1, character2)

							potion = choice([*range(10, 51)])
							if((character1.hp + potion) > 150):
								character1.hp = 150

							character1.hp += potion

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(character1.name + 'used potion to generate ' + str(potion) + ' life points', True, (255, 0, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							pygame.display.update()
							time.sleep(1)
							new_scene(chars, character1, character2)
							used_pot.append(character1.name)

			elif action == 3:
				basicfont = pygame.font.SysFont("arial", 16)

				text = basicfont.render(character1.name + 'just stayed there ', True, (255, 0, 0), (0, 0, 0))
				textrect = text.get_rect()
				textrect.center = (250, 470)

				win.blit(text, textrect)
				pygame.display.update()
				time.sleep(1)
				new_scene(chars, character1, character2)
		#char2 move
		elif (who_attacks == 2):
			action = choice([*range(1, 4)])

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

						if (character2.x < 490 and (character2.x + 5) < 490):
							temp_x = character2.x
							character2.x += 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character2.y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)
						else:
							temp_x = character2.x
							character2.x -= 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character2.y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character1.armor
							defence = choice([*range(0, d)])
							damage = character2.atk - defence
							character1.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character2.name + 'used magic to hit with ' + str(damage), True, (0,255,0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)

					#right
					elif left_right == 2:

						if (character2.x > 10 and (character2.x - 5) > 10):
							temp_x = character2.x
							character2.x -= 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character2.y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)
						else:
							temp_x = character2.x
							character2.x += 25

							pygame.draw.rect(win, (0,0,0), (temp_x, character2.y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character1.armor
							defence = choice([*range(0, d)])
							damage = character2.atk - defence
							character1.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character2.name + 'used magic to hit with ' + str(damage), True, (0, 255, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)

				elif x_or_y == 2:

					#decide up or down
					up_down = choice([*range(1, 3)])

					#up
					if up_down == 1:

						if (character2.y < 400 and (character2.y + 5) < 400):

							temp_y = character2.y
							character2.y += 25

							pygame.draw.rect(win, (0,0,0), (character2.x, temp_y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)
						else:
							temp_y = character2.y
							character2.y -= 25

							pygame.draw.rect(win, (0,0,0), (character2.x, temp_y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character1.armor
							defence = choice([*range(0, d)])
							damage = character2.atk - defence
							character1.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character2.name + 'used magic to hit with ' + str(damage), True, (0, 255, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)

					#down
					elif up_down == 2:

						if (character2.y > 10 and (character2.y - 5) > 10):
							temp_y = character2.y
							character2.y -= 25

							pygame.draw.rect(win, (0,0,0), (character2.x, temp_y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)
						else:
							temp_y = character2.y
							character2.y += 25

							pygame.draw.rect(win, (0,0,0), (character2.x, temp_y, 20, 20))
							pygame.draw.rect(win, character2.color,(character2.x, character2.y, 20, 20))
							time.sleep(1)

						attack = choice([*range(1, 6)])
						if (attack == 2 or attack == 5):
							d = character1.armor
							defence = choice([*range(0, d)])
							damage = character2.atk - defence
							character1.hp -= damage

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(
								character2.name + 'used magic to hit with ' + str(damage), True, (0, 255, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							time.sleep(1.5)
							new_scene(chars, character1, character2)
								

			#action 2 = use potion
			elif action == 2:
				for i in used_pot:
					if character2.name is not i:
						if (character2.hp < 150):

							if(character2.hp >= 150):
								basicfont = pygame.font.SysFont("arial", 16)

								text = basicfont.render(character2.name + 'tried to use a potion but his HP is full', True, (0, 255, 0), (0, 0, 0))
								textrect = text.get_rect()
								textrect.center = (250, 470)

								win.blit(text, textrect)
								pygame.display.update()
								time.sleep(1)
								new_scene(chars, character1, character2)

							potion = choice([*range(10, 51)])
							if((character2.hp + potion) > 150):
								character2.hp = 150

							character2.hp += potion

							basicfont = pygame.font.SysFont("arial", 16)

							text = basicfont.render(character2.name + 'used potion to generate ' + str(potion) + ' life points', True, (0, 255, 0), (0, 0, 0))
							textrect = text.get_rect()
							textrect.center = (250, 470)

							win.blit(text, textrect)
							pygame.display.update()
							time.sleep(1)
							new_scene(chars, character1, character2)
							used_pot.append(character2.name)

			elif action == 3:
				basicfont = pygame.font.SysFont("arial", 16)

				text = basicfont.render(character2.name + 'just stayed there ', True, (0, 255, 0), (0, 0, 0))
				textrect = text.get_rect()
				textrect.center = (250, 470)

				win.blit(text, textrect)
				pygame.display.update()
				time.sleep(1)
				new_scene(chars, character1, character2)


		pygame.display.update()
		

if __name__ == "__main__":
	main()
