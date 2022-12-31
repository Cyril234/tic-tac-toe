import pygame,sys,random

def display_blit():
	for value in range(9):
		if Tic_Tac_Toe_field_numbers[value] == 1:
			if value == 0:
				display_surface.blit(x, (34,34))
			if value == 1:
				display_surface.blit(x, (300,34))
			if value == 2:
				display_surface.blit(x, (566,34))
			if value == 3:
				display_surface.blit(x, (34,300))
			if value == 4:
				display_surface.blit(x, (300,300))
			if value == 5:
				display_surface.blit(x, (566,300))
			if value == 6:
				display_surface.blit(x, (34,566))
			if value == 7:
				display_surface.blit(x, (300,566))
			if value == 8:
				display_surface.blit(x, (566,566))

		if Tic_Tac_Toe_field_numbers[value] == 2:
			if value == 0:
				display_surface.blit(o, (34,34))
			if value == 1:
				display_surface.blit(o, (300,34))
			if value == 2:
				display_surface.blit(o, (566,34))
			if value == 3:
				display_surface.blit(o, (34,300))
			if value == 4:
				display_surface.blit(o, (300,300))
			if value == 5:
				display_surface.blit(o, (566,300))
			if value == 6:
				display_surface.blit(o, (34,566))
			if value == 7:
				display_surface.blit(o, (300,566))
			if value == 8:
				display_surface.blit(o, (566,566))

def player_input_x():
	global x_turn
	if event.type == pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos()

		if 266 > pos[0] and 266 > pos[1]:
			if Tic_Tac_Toe_field_numbers[0] == 0:
				Tic_Tac_Toe_field_numbers[0] = 1
				x_turn = False

		elif 266 < pos[0] and 532 > pos[0] and 266 > pos[1]:
			if Tic_Tac_Toe_field_numbers[1] == 0:
				Tic_Tac_Toe_field_numbers[1] = 1
				x_turn = False

		elif 532 < pos[0] and 266 > pos[1]:
			if Tic_Tac_Toe_field_numbers[2] == 0:
				Tic_Tac_Toe_field_numbers[2] = 1
				x_turn = False

		elif 266 > pos[0] and 266 < pos[1] and 532 > pos[1]:
			if Tic_Tac_Toe_field_numbers[3] == 0:
				Tic_Tac_Toe_field_numbers[3] = 1
				x_turn = False

		elif 266 < pos[0] and 532 > pos[0] and 266 < pos[1] and 532 > pos[1]:
			if Tic_Tac_Toe_field_numbers[4] == 0:
				Tic_Tac_Toe_field_numbers[4] = 1
				x_turn = False

		elif 532 < pos[0] and 266 < pos[1] and 532 > pos[1]:
			if Tic_Tac_Toe_field_numbers[5] == 0:
				Tic_Tac_Toe_field_numbers[5] = 1
				x_turn = False

		elif 266 > pos[0] and 532 < pos[1]:
			if Tic_Tac_Toe_field_numbers[6] == 0:
				Tic_Tac_Toe_field_numbers[6] = 1
				x_turn = False

		elif 266 < pos[0] and 532 > pos[0] and 532 < pos[1]:
			if Tic_Tac_Toe_field_numbers[7] == 0:
				Tic_Tac_Toe_field_numbers[7] = 1
				x_turn = False

		elif 532 < pos[0] and 532 < pos[1]:
			if Tic_Tac_Toe_field_numbers[8] == 0:
				Tic_Tac_Toe_field_numbers[8] = 1
				x_turn = False

def player_input_o():
	global x_turn
	if event.type == pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos()

		if 266 > pos[0] and 266 > pos[1]:
			if Tic_Tac_Toe_field_numbers[0] == 0:
				Tic_Tac_Toe_field_numbers[0] = 2
				x_turn = True

		elif 266 < pos[0] and 532 > pos[0] and 266 > pos[1]:
			if Tic_Tac_Toe_field_numbers[1] == 0:
				Tic_Tac_Toe_field_numbers[1] = 2
				x_turn = True

		elif 532 < pos[0] and 266 > pos[1]:
			if Tic_Tac_Toe_field_numbers[2] == 0:
				Tic_Tac_Toe_field_numbers[2] = 2
				x_turn = True

		elif 266 > pos[0] and 266 < pos[1] and 532 > pos[1]:
			if Tic_Tac_Toe_field_numbers[3] == 0:
				Tic_Tac_Toe_field_numbers[3] = 2
				x_turn = True

		elif 266 < pos[0] and 532 > pos[0] and 266 < pos[1] and 532 > pos[1]:
			if Tic_Tac_Toe_field_numbers[4] == 0:
				Tic_Tac_Toe_field_numbers[4] = 2
				x_turn = True

		elif 532 < pos[0] and 266 < pos[1] and 532 > pos[1]:
			if Tic_Tac_Toe_field_numbers[5] == 0:
				Tic_Tac_Toe_field_numbers[5] = 2
				x_turn = True

		elif 266 > pos[0] and 532 < pos[1]:
			if Tic_Tac_Toe_field_numbers[6] == 0:
				Tic_Tac_Toe_field_numbers[6] = 2
				x_turn = True

		elif 266 < pos[0] and 532 > pos[0] and 532 < pos[1]:
			if Tic_Tac_Toe_field_numbers[7] == 0:
				Tic_Tac_Toe_field_numbers[7] = 2
				x_turn = True

		elif 532 < pos[0] and 532 < pos[1]:
			if Tic_Tac_Toe_field_numbers[8] == 0:
				Tic_Tac_Toe_field_numbers[8] = 2
				x_turn = True	

def computer_logic():
	while True:
		random_number = random.randrange(0, 9)

		if Tic_Tac_Toe_field_numbers[random_number] == 0:
			Tic_Tac_Toe_field_numbers[random_number] = 2
			break

def winning_x():
	global won, won_x, won_xo

	if Tic_Tac_Toe_field_numbers[0] == 1 and Tic_Tac_Toe_field_numbers[1] == 1 and Tic_Tac_Toe_field_numbers[2] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[3] == 1 and Tic_Tac_Toe_field_numbers[4] == 1 and Tic_Tac_Toe_field_numbers[5] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[6] == 1 and Tic_Tac_Toe_field_numbers[7] == 1 and Tic_Tac_Toe_field_numbers[8] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[0] == 1 and Tic_Tac_Toe_field_numbers[3] == 1 and Tic_Tac_Toe_field_numbers[6] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[1] == 1 and Tic_Tac_Toe_field_numbers[4] == 1 and Tic_Tac_Toe_field_numbers[7] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[2] == 1 and Tic_Tac_Toe_field_numbers[5] == 1 and Tic_Tac_Toe_field_numbers[8] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[0] == 1 and Tic_Tac_Toe_field_numbers[4] == 1 and Tic_Tac_Toe_field_numbers[8] == 1:
		won = True
		won_x = True

	elif Tic_Tac_Toe_field_numbers[2] == 1 and Tic_Tac_Toe_field_numbers[4] == 1 and Tic_Tac_Toe_field_numbers[6] == 1:
		won = True
		won_x = True

	elif won_x == False:
		draw_number = 0
		for number in Tic_Tac_Toe_field_numbers:
			draw_number += number
		if draw_number == 13:
			won = True
			won_xo = True

def winning_o():
	global won, won_o, won_xo
	if Tic_Tac_Toe_field_numbers[0] == 2 and Tic_Tac_Toe_field_numbers[1] == 2 and Tic_Tac_Toe_field_numbers[2] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[3] == 2 and Tic_Tac_Toe_field_numbers[4] == 2 and Tic_Tac_Toe_field_numbers[5] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[6] == 2 and Tic_Tac_Toe_field_numbers[7] == 2 and Tic_Tac_Toe_field_numbers[8] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[0] == 2 and Tic_Tac_Toe_field_numbers[3] == 2 and Tic_Tac_Toe_field_numbers[6] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[1] == 2 and Tic_Tac_Toe_field_numbers[4] == 2 and Tic_Tac_Toe_field_numbers[7] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[2] == 2 and Tic_Tac_Toe_field_numbers[5] == 2 and Tic_Tac_Toe_field_numbers[8] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[0] == 2 and Tic_Tac_Toe_field_numbers[4] == 2 and Tic_Tac_Toe_field_numbers[8] == 2:
		won = True
		won_o = True

	elif Tic_Tac_Toe_field_numbers[2] == 2 and Tic_Tac_Toe_field_numbers  == 2 and Tic_Tac_Toe_field_numbers[6] == 2:
		won = True
		won_o = True

	elif won_x == False:
		draw_number = 0
		for number in Tic_Tac_Toe_field_numbers:
			draw_number += number
		if draw_number == 13:
			won = True
			won_xo = True

def won_def():
	global won_x, won_o, won_xo
	font = pygame.font.Font("grafik/GROBOLD.ttf",150)
	font1 = pygame.font.Font("grafik/GROBOLD.ttf",50)
	won_loop = True

	while won_loop:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if 311 <= pos[0] and 487 >= pos[0] and 489 <= pos[1] and 609 >= pos [1]:
					won_loop = False
					play()

		if won_x:
			wintext = "x won"
		if won_o:
			wintext = "o won"
		if won_xo:
			wintext = "draw"

		display_surface.fill((27, 158, 141))
		text_surf = font.render(f"{wintext}",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (399, 399))
		display_surface.blit(text_surf, text_rect)
		
		#restart blit
		text_surf = font1.render("restart",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (399, 549))
		display_surface.blit(text_surf,(text_rect))
		pygame.draw.rect(display_surface,(255,255,255),text_rect.inflate(30,30), width = 10, border_radius = 5)
		
		pygame.display.update()

def play():
	global start, player_against_player, Tic_Tac_Toe_field_numbers, x_turn, won, won_x, won_o, won_xo, start
	
	font = pygame.font.Font("grafik/GROBOLD.ttf",50)
	
	Tic_Tac_Toe_field_numbers = [0,0,0,0,0,0,0,0,0]
	player_against_player = True
	x_turn = True
	won = False
	won_x = False
	won_o = False
	won_xo = False
	start = True
	
	play_loop = True

	while play_loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if 249 <= pos[0] and 549 >= pos[0] and 249 <= pos[1] and 329 >= pos [1]:
					start = False
					player_against_player = False
					play_loop = False

				if 249 <= pos[0] and 549 >= pos[0] and 449 <= pos[1] and 629 >= pos [1]:
					start = False
					player_against_player = True
					play_loop = False
		
		#display update
		display_surface.fill((27, 158, 141))
		display_surface.blit(Tic_Tac_Toe_field, (0,0))
		display_surface.blit(single_player, (249,249))
		display_surface.blit(multiplayer, (249,449))
		
		pygame.display.update()

#basic setup
pygame.init()
display_surface = pygame.display.set_mode((798, 798))
pygame.display.set_caption("Tic Tac Toe")

#field logic
Tic_Tac_Toe_field_numbers = [0,0,0,0,0,0,0,0,0]

#import asset
Tic_Tac_Toe_field = pygame.image.load("grafik/hintergrund.png").convert_alpha()
Tic_Tac_Toe_field = pygame.transform.scale(Tic_Tac_Toe_field, (798,798))
x = pygame.image.load("grafik/x.png").convert_alpha()
x = pygame.transform.scale(x, (200,200))
o = pygame.image.load("grafik/o.png").convert_alpha()
o = pygame.transform.scale(o, (200,200))
single_player =  pygame.image.load("grafik/Single Player.png").convert_alpha()
multiplayer =  pygame.image.load("grafik/multiplayer.png").convert_alpha()

font = pygame.font.Font("grafik/GROBOLD.ttf",150)
text_surf_single = font.render("single player",True,(255,255,255))
text_rect_single = text_surf_single.get_rect(center = (399, 449))

text_surf_multi = font.render("single player",True,(255,255,255))
text_rect_multi = text_surf_multi.get_rect(center = (399, 249))

#variable
player_against_player = True
x_turn = True
won = False
won_x = False
won_o = False
won_xo = False
start = True

#main gameloop
while True:

	if start:
		play()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if x_turn:
			player_input_x()

	if won:
		won_def()

	#display update
	winning_x()
	display_blit()
	pygame.display.update()

	if won == False:
		if x_turn == False:
			if player_against_player:
				player_input_o()

			else:
				computer_logic()
				x_turn = True

	if won:
		won_def()

	#display blit/fill
	display_surface.fill((27, 158, 141))
	display_surface.blit(Tic_Tac_Toe_field, (0,0))

	#display update
	winning_o()
	display_blit()
	pygame.display.update()

#Dieses Game wurde von Cyril Seitz entwickelt!!!