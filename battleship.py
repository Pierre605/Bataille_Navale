import random

grid = []
grid_2 = []
grid_bot_opponent = []
emo_sea = '🌊'
strike_emo = '💥'
cold_shot = '⚪'
sunk_emo = '☠️'
emos_plus = ['🏴', '⚜️', '☠️', '🗡️', '🛡️', '💥', '✈️', '📡', '🚢', '⚔️', '🛩️', '🎯', '⚪','💦']
ships = {"p": {"name": "Porte-avion", "size": 5, "emo": '✈️'}, "c": {"name": "Croiseur", "size": 4, "emo": '⚔️'}, "s": {"name": "Sous-Marin", "size": 3, "emo": '⚜️'}, "t": {"name": "Torpilleur", "size": 2, "emo": '🛡️'}}
algo_ships = {"p": {"name": "Porte-avion", "size": 5, "emo": '🛩️'}, "c": {"name": "Croiseur", "size": 4, "emo": '⚔️'}, "s": {"name": "Sous-Marin", "size": 3, "emo": '🏴'}, "t": {"name": "Torpilleur", "size": 2, "emo": '🗡️'}}
algo_emos = ['🏴', '🗡️', '🛩️', '⚔️']

def make_grid():
	grid = []
	for y in range(10):
		grid.append([])
		for x in range(10):
			grid[y].append(emo_sea)
	return grid


def print_grid(grid):
	print("\n")
	print("    🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯\n")
	for x in range(10):
		if x == 9:
			print(x+1, end='  ')
		else:
			print(x+1, end='   ')
		for y in range(10):
				print(grid[x][y], end=' ')
		print("")


def letter_to_int(letter):
	if letter.lower() == 'a':
		return 0
	elif letter.lower() == 'b':
		return 1
	elif letter.lower() == 'c':
		return 2
	elif letter.lower() == 'd':
		return 3
	elif letter.lower() == 'e':
		return 4
	elif letter.lower() == 'f':
		return 5
	elif letter.lower() == 'g':
		return 6
	elif letter.lower() == 'h':
		return 7
	elif letter.lower() == 'i':
		return 8
	elif letter.lower() == 'j':
		return 9

def str_to_int(stg):
	if stg == '1':
		return 0
	elif stg == '2':
		return 1
	elif stg == '3':
		return 2
	elif stg == '4':
		return 3
	elif stg == '5':
		return 4
	elif stg == '6':
		return 5
	elif stg == '7':
		return 6
	elif stg == '8':
		return 7
	elif stg == '9':
		return 8
	elif stg == '10':
		return 9


def place_your_ships(grid):
	S = []
	while len(S) < 4:
		print("Bateaux à placer: ")
		for k, v in ships.items():
			if k not in S:
				print(f"{ships[k]['name']} '{k}', taille du bâtiment: {ships[k]['size']}", end='  ')
				print("")
		print("\n")
		while True:
			input_ship = input("Quel bateau voulez vous placer ? ").lower()
			if ships.get(input_ship):
				if input_ship not in S:
					print(f"{ships[input_ship]['name']} sélectionné, taille du bâtiment: {ships[input_ship]['size']}")
					break
				else:
					print("Bateau dejà placé ! chosissez en un autre ")
			else:
				print("Entrez la première lettre du nom du navire")

		input_direction = input("horzontalement ou verticalement ? 'h' horizontalement, 'v' verticalement : ")
		while True:
			if input_direction in ['h', 'v']:
				break
			else:
				input_direction = input("Erreur ! Entrez 'h' ou 'v' : ")

		while True:
			try:
				input_row = int(input("sur quelle ligne ? Entrez un chiffre entre 1 et 10 compris: ")) - 1
				if int(input_row) in range(10):
					input_row = int(input_row)
					break
				else:
					input_row = int(input("Erreur ! Entrez un chiffre entre 1 et 10 compris: ")) - 1
			except:
				print("Erreur ! Entrez un chiffre !!! ")
				continue
			
			

		input_col = letter_to_int(input("sur quelle colonne ? Entrez une lettre de A à J compris: "))
		while True:
			if input_col in range(10):
				break
			else:
				input_col = letter_to_int(input("Erreur ! Entrez une lettre de A à J compris: "))

		if input_direction.lower() == "h":
			while True:
				count = 0
				if input_col + ships[input_ship]["size"] < len(grid)+1:
					for emo in grid[input_row][input_col: input_col + ships[input_ship]["size"]]:
						if emo == emo_sea:
							count +=1
					if count == ships[input_ship]["size"]:
						for i in range(ships[input_ship]["size"]):
							grid[input_row][input_col +i] = ships[input_ship]["emo"]
						break
					else:
						print("Deja pris")
						input_col = letter_to_int(input("Sur quelle colonne ? Entrez un chiffre une lettre de A à J compris: "))
						while True:
							if input_col in range(10):
								break
							else:
								input_col = letter_to_int(input("Erreur ! Entrez une lettre de A à J compris: "))
				else:
					print("Vous dépassez les limites de la grille, vous devez placer la tête du bâtiment, qui s'étale ensuite de sa longueur vers la droite")
					input_col = letter_to_int(input("sur quelle colonne ? Entrez un chiffre une lettre de A à J compris: "))
		
		elif input_direction.lower() == "v":
			while True:
				count = 0
				if input_row + ships[input_ship]["size"] < len(grid)+1:
					for i in range(ships[input_ship]["size"]):
						if grid[input_row +i][input_col] == emo_sea:
							count +=1
					if count == ships[input_ship]["size"]:
						for i in range(ships[input_ship]["size"]):
							grid[input_row +i][input_col] = ships[input_ship]["emo"]
						break
					else:
						print("Deja pris")
						while True:
							try:
								input_row = int(input("sur quelle ligne ? Entrez un chiffre entre 1 et 10 compris: ")) - 1
								if int(input_row) in range(10):
									input_row = int(input_row)
									break
								else:
									input_row = int(input("Erreur ! Entrez un chiffre entre 1 et 10 compris: ")) - 1
							except:
								print("Erreur ! Entrez un chiffre !!! ")
								continue

				else:
					print("Vous dépassez les limites de la grille, vous devez placer la tête du bâtiment, qui s'étale ensuite de sa longueur vers le bas")
					input_row = int(input("sur quelle ligne ? Entrez un chiffre entre 1 et 10 compris: ")) - 1
		
		if input_ship not in S:
			S.append(input_ship)

		print_grid(grid)

def make_opponent_grid():
	grid_algo = make_grid()
	dir = ['h', 'v']
	for k, v in algo_ships.items():
		random_dir = random.choice(dir)

		if random_dir == 'v':
			while True:
				random_row = random.randint(1, 8)
				random_col = random.randint(1, 8)
				count = 0
				if random_row + algo_ships[k]["size"] < len(grid_algo):
					for i in range(algo_ships[k]["size"]):
						if grid_algo[random_row +i][random_col] == emo_sea and (grid_algo[random_row +i][random_col+1] not in algo_emos) and (grid_algo[random_row +i][random_col-1] not in algo_emos) and (grid_algo[random_row +i -1][random_col] not in algo_emos) and (grid_algo[random_row +i +1][random_col] not in algo_emos):
							count +=1
					if count == algo_ships[k]["size"]:
						for i in range(ships[k]["size"]):
							grid_algo[random_row +i][random_col] = algo_ships[k]['emo']
						break
				else:
					print("dépassement des limites de la grille, ou bien l'espace est deja pris")
					random_row = random.randint(1, 8)

		elif random_dir == 'h':
			while True:
				random_row = random.randint(1, 8)
				random_col = random.randint(1, 8)
				count = 0	
				if random_col + algo_ships[k]["size"] < len(grid_algo):
					for i in range(algo_ships[k]["size"]):
						if grid_algo[random_row][random_col+i] == emo_sea and (grid_algo[random_row +1][random_col+i] not in algo_emos) and (grid_algo[random_row -1][random_col+i] not in algo_emos) and (grid_algo[random_row][random_col+i -1] not in algo_emos) and (grid_algo[random_row][random_col +i+1] not in algo_emos):
							count +=1
					if count == algo_ships[k]["size"]:
						for i in range(algo_ships[k]["size"]):
							grid_algo[random_row][random_col +i] = algo_ships[k]['emo']
						break
				else:
					print("dépassement des limites de la grille, ou bien l'espace est deja pris")
					random_col = random.randint(1, 8)
	
	return grid_algo

def you_play(grid_algo, grid_attack):
	while True:
		input_row = str_to_int(input("Sur quelle ligne voulez-vous tirer ? Entrez un chiffre entre 1 et 10 compris: "))
		if input_row in range(10):
			input_col = letter_to_int(input("Sur quelle colonne ? Entrez un chiffre une lettre de A à J compris: "))
			if input_col in range(10):
				grid_attack = render_attack_grid(grid_algo, grid_attack, input_row, input_col)
				return grid_attack
			else:
				print("Erreur ! Entrez une lettre de A à J compris: ")
		else:
			print("Erreur ! Entrez un chiffre entre 1 et 10 compris: ")

def render_attack_grid(grid_algo, grid_attack, input_row, input_col):
	for k, v in algo_ships.items():
		if grid_algo[input_row][input_col] == algo_ships[k]["emo"]:
			grid_attack[input_row][input_col] = strike_emo
			print(f"\n{algo_ships[k]['name']} ennemi touché !")
			print_grid(grid_attack)
			return grid_attack
	for k, v in algo_ships.items():
		if (grid_algo[input_row][input_col] != algo_ships[k]["emo"]) and (grid_algo[input_row][input_col] != strike_emo):
			grid_attack[input_row][input_col] = cold_shot
			print("\nCoup dans l'eau")
			print_grid(grid_attack)
			return grid_attack

def check_sunk(grid, k, x, y):
	count = 0
	for i in range(algo_ships[k]['size']):
		if grid[x+i][y] == strike_emo:
			count +=1
	if count == algo_ships[k]['size']:
		print(f"{algo_ships[k]['name']} ennemi coulé")

	for i in range(algo_ships[k]['size']):
		grid[x+i][y] = sunk_emo

def check_defeat(grid):
	count_algo_emos = 0
	for x in range(10):
		for y in range(10):
			if grid[x][y] in algo_emos:
				count_algo_emos +=1
	if count_algo_emos == 0:
		print("\nDéfaite ! Votre dernier navire a coulé\n")
		return 'bye'
	else:
		pass

bato =[]
coord_strike = []

def algo_player(grid):
	count_strike = 0
	count_miss = 0
	for x in range(10):
		for y in range(10):
			if grid[x][y] == strike_emo:
				count_strike +=1
			elif grid[x][y] == cold_shot:
				count_miss +=1

	print(f"{count_strike} strike found !\n")
	print(f"{count_miss} cold shots found !\n")

	while True:	
		if count_strike > 0:
			for x in range(10):
				for y in range(10):
						if (x > 0 and x < 9) and (y > 0 and y < 9):
							if count_strike == 1:
								if x == coord_strike[0][0] and y == coord_strike[0][1]:
									if (grid[x+1][y] != strike_emo) and (grid[x-1][y] != strike_emo) and (grid[x][y-1] != strike_emo) and (grid[x][y+1] != strike_emo):
										print("no strikes around")

										if (grid[x+1][y] != cold_shot):
											# print("here first strike !")
											if grid[x+1][y] == algo_ships[bato[-1]]['emo']:
												bato.append(bato[-1])
												coord_strike.append([x+1, y])
												grid[x+1][y] = strike_emo
												print_grid(grid)
												print("touché en bas")
												# cas torpilleur size 2
												if bato[-1] == 't':
													if len(coord_strike) == algo_ships[bato[-1]]['size']:
														for i in range(algo_ships[bato[-1]]['size']):
															grid[x+1-i][y] = sunk_emo
														print_grid(grid)
														print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
														if check_defeat(grid) == 'bye':
															return 'end'
														return grid
												return grid
											
											elif grid[x+1][y] not in algo_ships[bato[-1]]['emo']:
												grid[x+1][y] = cold_shot
												print_grid(grid)
												print("rien en bas")
												return grid

										#vert check
										if (grid[x+1][y] == cold_shot) and (grid[x-1][y] != cold_shot):
											print("vert check 1 !")
											if grid[x-1][y] == algo_ships[bato[-1]]['emo']:
												coord_strike.append([x-1, y])
												grid[x-1][y] = strike_emo
												print_grid(grid)
												print("touché en haut")

												# cas torpilleur size 2
												if bato[-1] == 't':
													print("vert check 1 torpilleur")
													print("bato:", bato)
													print("coord_strike:", coord_strike)
													if len(coord_strike) == algo_ships[bato[-1]]['size']:
														print("bato:", bato)
														print("coord_strike:", coord_strike)
														for i in range(algo_ships[bato[-1]]['size']):
															grid[x-1+i][y] = sunk_emo
														print_grid(grid)
														print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
														if check_defeat(grid) == 'bye':
															return 'end'
														return grid
												return grid

											if grid[x-1][y] not in algo_ships[bato[-1]]['emo']:
												grid[x-1][y] = cold_shot
												print_grid(grid)
												print("rien en haut")
												print("bato:", bato)
												print("coord_strike:", coord_strike)
												return grid

										elif (grid[x+1][y] != cold_shot) and (grid[x-1][y] == cold_shot):
											print("vert check 2 !")
											if grid[x+1][y] == algo_ships[bato[-1]]['emo']:
												coord_strike.append([x+1, y])
												grid[x+1][y] = strike_emo
												print_grid(grid)
												print("touché en bas")

												# cas torpilleur size 2
												if bato[-1] == 't':
													if len(coord_strike) == algo_ships[bato[-1]]['size']:
														print("bato:", bato)
														print("coord_strike:", coord_strike)
														for i in range(algo_ships[bato[-1]]['size']):
															grid[x+1-i][y] = sunk_emo
														print_grid(grid)
														print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
														if check_defeat(grid) == 'bye':
															return 'end'
														return grid
												return grid

											if grid[x+1][y] not in algo_ships[bato[-1]]['emo']:
												grid[x+1][y] = cold_shot
												print_grid(grid)
												print("rien en bas")
												print("bato:", bato)
												print("coord_strike:", coord_strike)
												return grid

										# hor check
										elif (grid[x+1][y] == cold_shot) and (grid[x-1][y] == cold_shot):
												print("hor check 1 !")
												if grid[x][y-1] == algo_ships[bato[-1]]['emo']:
													coord_strike.append([x, y-1])
													grid[x][y-1] = strike_emo
													print_grid(grid)
													print("touché à gauche")

													# cas torpilleur size 2
													if bato[-1] == 't':
														print("bato:", bato)
														print("coord_strike:", coord_strike)
														if len(coord_strike) == algo_ships[bato[-1]]['size']:
															print("bato:", bato)
															print("coord_strike:", coord_strike)
															for i in range(algo_ships[bato[-1]]['size']):
																grid[x][y-1+i] = sunk_emo
															print_grid(grid)
															print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
															if check_defeat(grid) == 'bye':
																return 'end'
															return grid
													return grid

												if grid[x][y-1] not in [algo_ships[bato[-1]]['emo'], cold_shot]:
													grid[x][y-1] = cold_shot
													print_grid(grid)
													print("rien à gauche")
													print("bato:", bato)
													print("coord_strike:", coord_strike)
													return grid

												if (grid[x][y-1] == cold_shot) and (grid[x][y+1] != cold_shot):
													print("hor check 2 !")
													if grid[x][y+1] == algo_ships[bato[-1]]['emo']:
														coord_strike.append([x, y+1])
														grid[x][y+1] = strike_emo
														print_grid(grid)
														print("touché à droite")

														# cas torpilleur size 2
														if bato[-1] == 't':
															print("bato:", bato)
															print("coord_strike:", coord_strike)
															if len(coord_strike) == algo_ships[bato[-1]]['size']:
																for i in range(algo_ships[bato[-1]]['size']):
																	grid[x][y+1-i] = sunk_emo
																print_grid(grid)
																print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
																if check_defeat(grid) == 'bye':
																	return 'end'
																return grid
														return grid

													if grid[x][y+1] not in [algo_ships[bato[-1]]['emo'], cold_shot]:
														grid[x][y+1] = cold_shot
														print_grid(grid)
														print("rien à droite")
														print("bato:", bato)
														print("coord_strike:", coord_strike)
														return grid
							
							# 2 strikes at least, direction found
							else:
								row = coord_strike[-1][0]
								col = coord_strike[-1][1]
								# print("row:", row)
								# print("col:", col)
								if (grid[row+1][col] == strike_emo) and (grid[row-1][col] not in [strike_emo, cold_shot]):
									if grid[row-1][col] == algo_ships[bato[-1]]['emo']:
										grid[row-1][col] = strike_emo
										coord_strike.append([row-1, col])
										print_grid(grid)
										print("touché en haut")
										print("bato:", bato)
										print("coord_strike:", coord_strike)

										# sunk check
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row-1+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										return grid
									else:
										grid[row-1][col] = cold_shot
										print("coord_strike:", coord_strike)

										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										
										else:
											row = coord_strike[::-1][-1][0]
											col = coord_strike[::-1][-1][1]
											print("back_to:", row, col)

										print_grid(grid)
										print("rien en haut")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										return grid

								elif (grid[row-1][col] == strike_emo) and (grid[row+1][col] not in [strike_emo, cold_shot]):
									if grid[row+1][col] == algo_ships[bato[-1]]['emo']:
										grid[row+1][col] = strike_emo
										coord_strike.append([row+1, col])
										print_grid(grid)
										print("touché en bas")
										print("bato:", bato)
										print("coord_strike:", coord_strike)

										# sunk check
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row+1-i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										return grid
									else:
										grid[row+1][col] = cold_shot
										print("coord_strike:", coord_strike)
										
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										
										else:
											row = coord_strike[::-1][-1][0]
											col = coord_strike[::-1][-1][1]
											print("back_to:", row, col)
										
										print_grid(grid)
										print("rien en bas")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										return grid

								elif (grid[row-1][col] == strike_emo) and (grid[row+1][col] ==  cold_shot):
									row = coord_strike[::-1][-1][0]
									col = coord_strike[::-1][-1][1]
									if grid[row-1][col] == algo_ships[bato[-1]]['emo']:
										grid[row-1][col] = strike_emo
										coord_strike.append([row-1, col])
										print_grid(grid)
										print("touché en haut")
										print("bato:", bato)
										print("coord_strike:", coord_strike)

										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row-1+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										return grid
									else:
										grid[row-1][col] = cold_shot
										print("coord_strike:", coord_strike)

										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid

										print("rien en haut")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										return grid


								elif (grid[row][col-1] == strike_emo) and (grid[row][col+1] not in [strike_emo, cold_shot]):
									if grid[row][col+1] == algo_ships[bato[-1]]['emo']:
										coord_strike.append([row, col+1])
										grid[row][col+1] = strike_emo
										print_grid(grid)
										print("touché à droite")
										print("bato:", bato)
										print("coord_strike:", coord_strike)

										# sunk check
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row][col+1-i] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										return grid

									else:
										grid[row][col+1] = cold_shot
										print("coord_strike:", coord_strike)
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										
										else:
											row = coord_strike[::-1][-1][0]
											col = coord_strike[::-1][-1][1]
											print("back_to:", row, col)

										print_grid(grid)
										print("rien à droite")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										return grid
								
								elif (grid[row][col+1] == strike_emo) and (grid[row][col-1] not in [strike_emo, cold_shot]):
									if grid[row][col-1] == algo_ships[bato[-1]]['emo']:
										coord_strike.append([row, col-1])
										grid[row][col-1] = strike_emo
										print_grid(grid)
										print("touché à gauche")
										print("bato:", bato)
										print("coord_strike:", coord_strike)

										# sunk check
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row][col-1+i] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										return grid
									else:
										grid[row][col-1] = cold_shot
										print("coord_strike:", coord_strike)

										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row+i][col] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										
										else:
											row = coord_strike[::-1][-1][0]
											col = coord_strike[::-1][-1][1]
											print("back_to:", row, col)

										print_grid(grid)
										print("rien à gauche")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										return grid

								elif (grid[row][col+1] == strike_emo) and (grid[row][col-1] == cold_shot):
									row = coord_strike[::-1][-1][0]
									col = coord_strike[::-1][-1][1]
									if grid[row][col+1] == algo_ships[bato[-1]]['emo']:
										coord_strike.append([row, col+1])
										grid[row][col+1] = strike_emo
										print_grid(grid)
										print("touché à droite")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row][col+1-i] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										return grid
									else:
										grid[row][col+1] = cold_shot
										print("coord_strike:", coord_strike)

										if len(coord_strike) == algo_ships[bato[-1]]['size']:
											for i in range(algo_ships[bato[-1]]['size']):
												grid[row][col-i] = sunk_emo
											print_grid(grid)
											print(f"Votre {algo_ships[bato[-1]]['name']} est coulé")
											if check_defeat(grid) == 'bye':
												return 'end'
											return grid
										
										print_grid(grid)
										print("rien à droite")
										print("bato:", bato)
										print("coord_strike:", coord_strike)
										return grid

	
		else:
			bato.clear()
			coord_strike.clear()
			random_row = random.randint(0, 9)
			random_col = random.randint(0, 9)
			if grid[random_row][random_col] == emo_sea:
				grid[random_row][random_col] = cold_shot
				print_grid(grid)
				print("Ouf! c'est Manqué")
				return grid
			else:
				for k, v in algo_ships.items():
					if grid[random_row][random_col] == algo_ships[k]['emo']:
						bato.append(k)
						coord_strike.append([random_row, random_col])
						grid[random_row][random_col] = strike_emo
						print_grid(grid)
						print(f"Votre {ships[k]['name']} est touché")
						print("bato:", bato)
						print("coord_strike:", coord_strike)
						return grid
						


def game():
	# grid = make_grid()
	grid = make_opponent_grid()
	grid_algo = make_opponent_grid()
	grid_attack = make_grid()
	print_grid(grid)
	# place_your_ships(grid)
	print('\n')
	# print_grid(grid_algo)
	while True:
		# print_grid(grid)
		print_grid(grid_algo)
		print('\n')
		grid_attack = you_play(grid_algo, grid_attack)
		grid = algo_player(grid)
		if grid == 'end':
			break
		# print_grid(grid)
	# place_your_ships(grid)
	# print('\n')
	# print("Votre grille est prête")


game()
# make_opponent_grid()
