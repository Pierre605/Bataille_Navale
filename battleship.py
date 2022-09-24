import random
import time
from ascii import title, warship_pic


emo_sea = '🌊'
strike_emo = '💥'
cold_shot = '⚫'
sunk_emo = '☠️'
emos_plus = ['🏴', '⚜️', '☠️', '🗡️', '🛡️', '💥', '✈️', '📡', '🚢', '⚔️', '🛩️', '🎯', '⚪','💦', '⚫', '💯', '🎯', '😬', '🤕', '😧', '😰', '😒', '🥳', '🥴', '😵', '⚠️']
ships = {"p": {"name": "Porte-avion", "size": 5, "emo": '✈️'}, "c": {"name": "Croiseur", "size": 4, "emo": '⚔️'}, "s": {"name": "Sous-Marin", "size": 3, "emo": '⚜️'}, "t": {"name": "Torpilleur", "size": 2, "emo": '🛡️'}}
algo_ships = {"p": {"name": "Porte-avion", "size": 5, "emo": '🛩️'}, "c": {"name": "Croiseur", "size": 4, "emo": '⚔️'}, "s": {"name": "Sous-Marin", "size": 3, "emo": '🏴'}, "t": {"name": "Torpilleur", "size": 2, "emo": '🗡️'}}
your_emos = ['⚔️', '✈️', '🛡️', '⚜️']
algo_emos = ['🏴', '🗡️', '🛩️', '⚔️']


def make_grid():
	grid = []
	for y in range(12):
		grid.append([])
		for x in range(12):
			grid[y].append(emo_sea)
	return grid


def print_grid(grid):
	print("\n")
	print("    🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯\n")
	for x in range(1, 11):
		if x == 10:
			print(x, end='  ')
		else:
			print(x, end='   ')
		for y in range(1, 11):
			print(grid[x][y], end=' ')
		print("")


def letter_to_int(letter):
	if letter.lower() == 'a':
		return 1
	elif letter.lower() == 'b':
		return 2
	elif letter.lower() == 'c':
		return 3
	elif letter.lower() == 'd':
		return 4
	elif letter.lower() == 'e':
		return 5
	elif letter.lower() == 'f':
		return 6
	elif letter.lower() == 'g':
		return 7
	elif letter.lower() == 'h':
		return 8
	elif letter.lower() == 'i':
		return 9
	elif letter.lower() == 'j':
		return 10

def str_to_int(stg):
	if stg == '1':
		return 1
	elif stg == '2':
		return 2
	elif stg == '3':
		return 3
	elif stg == '4':
		return 4
	elif stg == '5':
		return 5
	elif stg == '6':
		return 6
	elif stg == '7':
		return 7
	elif stg == '8':
		return 8
	elif stg == '9':
		return 9
	elif stg == '10':
		return 10


def place_your_ships(grid):
	SHIPS = []
	while len(SHIPS) < 4:
		print("Bateaux à placer: ")
		for k, v in ships.items():
			if k not in SHIPS:
				print(f"{ships[k]['name']} '{k}', taille du bâtiment: {ships[k]['size']}", end='  ')
				print("")
		print("\n")
		while True:
			input_ship = input("Quel bateau voulez vous placer ? ").lower()
			if ships.get(input_ship):
				if input_ship not in SHIPS:
					print(f"{ships[input_ship]['name']} sélectionné, taille du bâtiment: {ships[input_ship]['size']}")
					break
				else:
					print("⚠️ Bateau dejà placé ! chosissez en un autre ")
			else:
				print("⚠️ Entrez la première lettre du nom du navire")

		input_direction = input("Horzontalement ou verticalement ? 'h' horizontalement, 'v' verticalement : ")
		while True:
			if input_direction in ['h', 'v']:
				break
			else:
				input_direction = input("⚠️ Erreur ! Entrez 'h' ou 'v' : ")


		if input_direction.lower() == "h":
			while True:
				try:
					input_row = int(input("Sur quelle ligne ? Entrez un chiffre entre 1 et 10 compris: "))
				except:
					print("⚠️ Erreur ! Entrez un chiffre !!! ")
					continue
				if int(input_row) in range(1, 11):
					input_row = int(input_row)
					input_col = letter_to_int(input("Sur quelle colonne ? Entrez une lettre de A à J compris: "))
					if input_col in range(1, 11):					
						count = 0
						if input_col + ships[input_ship]["size"] < len(grid):
							for i in range(ships[input_ship]["size"]):
								if (grid[input_row][input_col+i] == emo_sea) and (grid[input_row +1][input_col+i] == emo_sea) and (grid[input_row -1][input_col+i] == emo_sea) and (grid[input_row][input_col+i-1] == emo_sea) and (grid[input_row][input_col+i+1] == emo_sea):
									count +=1
							if count == ships[input_ship]["size"]:
								for i in range(ships[input_ship]["size"]):
									grid[input_row][input_col +i] = ships[input_ship]["emo"]
								break
							else:
								print("⚠️ Deja pris ou trop prêt d'un autre de vos navires")
						else:
							print("⚠️ Vous dépassez les limites de la grille, vous devez placer la tête du bâtiment, qui s'étale ensuite de sa longueur vers la droite")
						
		
		elif input_direction.lower() == "v":
			while True:
				try:
					input_row = int(input("Sur quelle ligne ? Entrez un chiffre entre 1 et 10 compris: "))
				except:
					print("⚠️ Erreur ! Entrez un chiffre !!! ")
					continue
				if int(input_row) in range(1, 11):
					input_row = int(input_row)
					input_col = letter_to_int(input("Sur quelle colonne ? Entrez une lettre de A à J compris: "))
					if input_col in range(1, 11):
						count = 0
						if input_row + ships[input_ship]["size"] < len(grid):
							for i in range(ships[input_ship]["size"]):
								if (grid[input_row +i][input_col] == emo_sea) and (grid[input_row +i][input_col+1] == emo_sea) and (grid[input_row +i][input_col-1] == emo_sea) and (grid[input_row +i -1][input_col] == emo_sea) and (grid[input_row +i +1][input_col] == emo_sea):
									count +=1
							if count == ships[input_ship]["size"]:
								for i in range(ships[input_ship]["size"]):
									grid[input_row +i][input_col] = ships[input_ship]["emo"]
								break
							else:
								print("⚠️ Deja pris ou trop prêt d'un autre de vos navires")
						else:
							print("⚠️ Vous dépassez les limites de la grille, vous devez placer la tête du bâtiment, qui s'étale ensuite de sa longueur vers le bas")
		
		if input_ship not in SHIPS:
			SHIPS.append(input_ship)

		print_grid(grid)

def make_opponent_grid():
	grid_algo = make_grid()
	dir = ['h', 'v']
	for k, v in algo_ships.items():
		random_dir = random.choice(dir)

		if random_dir == 'v':
			while True:
				random_row = random.randint(1, 10)
				random_col = random.randint(1, 10)
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
					# print("dépassement des limites de la grille, ou bien l'espace est deja pris")
					random_row = random.randint(1, 8)

		elif random_dir == 'h':
			while True:
				random_row = random.randint(1, 10)
				random_col = random.randint(1, 10)
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
					# print("dépassement des limites de la grille, ou bien l'espace est deja pris")
					random_col = random.randint(1, 10)
	
	return grid_algo
	

def you_play(grid_algo, grid_attack):
	count_s = 0
	coord_s = []
	for x in range(1, 11):
		for y in range (1, 11):
			if grid_attack[x][y] == strike_emo:
				count_s += 1
				coord_s.append([x, y])
	
	while True:
		input_row = str_to_int(input("Sur quelle ligne voulez-vous tirer ? Entrez un chiffre entre 1 et 10 compris: "))
		if input_row in range(1, 11):
			input_col = letter_to_int(input("Sur quelle colonne ? Entrez une lettre de A à J compris: "))
			if input_col in range(1, 11):
				for k, v in algo_ships.items():
					if grid_algo[input_row][input_col] == algo_ships[k]["emo"]:
						grid_attack[input_row][input_col] = strike_emo
						print(f"\n{algo_ships[k]['name']} ennemi touché ! 🎯")

						# print_grid(grid_attack)
						count_s = 0
						coord_s = []
						for x in range(1, 11):
							for y in range (1, 11):
								if grid_attack[x][y] == strike_emo:
									count_s += 1
									coord_s.append([x, y])
						# print("count:", count_s)
						# print("coord:", coord_s)

						if count_s >= 2:
							for x in range(len(coord_s)-1):
								if coord_s[x][1] == coord_s[x+1][1]:
									if count_s == algo_ships[k]['size']:
										for i in range(algo_ships[k]['size']):
											grid_attack[coord_s[i][0]][coord_s[i][1]] = sunk_emo										
										print_grid(grid_attack)
										print(f"\n{algo_ships[k]['name']} ennemi coulé ! 💯")
										if check_ennemy_defeat(grid_attack) == 'bye':
											return 'end'
										return grid_attack
								else:
									if count_s == algo_ships[k]['size']:
										for i in range(algo_ships[k]['size']):
											grid_attack[coord_s[i][0]][coord_s[i][1]] = sunk_emo
										print_grid(grid_attack)
										print(f"\n{algo_ships[k]['name']} ennemi coulé ! 💯")
										if check_ennemy_defeat(grid_attack) == 'bye':
											return 'end'
										return grid_attack					

						print_grid(grid_attack)
						return grid_attack

				for k, v in algo_ships.items():
					if (grid_algo[input_row][input_col] != algo_ships[k]["emo"]) and (grid_algo[input_row][input_col] != strike_emo):
						grid_attack[input_row][input_col] = cold_shot
						print_grid(grid_attack)
						print("Coup dans l'eau ! 😒")
						return grid_attack
			else:
				print("⚠️ Erreur ! Entrez une lettre de A à J compris")
		else:
			print("⚠️ Erreur ! Entrez un chiffre entre 1 et 10 compris")


def check_ennemy_defeat(grid_attack):
	count_sunk = 0
	for x in range(1, 11):
		for y in range(1, 11):
			if grid_attack[x][y] == sunk_emo:
				count_sunk +=1
	if count_sunk == 14:
		print("\nVICTOIRE ! Vous avez coulé tous les navires ennemis 🥳\n")
		return 'bye'


def check_your_defeat(grid):
	count_your_emos = 0
	for x in range(1, 11):
		for y in range(1, 11):
			if grid[x][y] in your_emos:
				count_your_emos +=1
	if count_your_emos == 0:
		print("\nDÉFAITE ! Votre dernier navire a coulé 🥴\n")
		return 'bye'
	else:
		pass


bato =[]
coord_strike = []

def algo_player(grid):
	count_strike = 0
	count_miss = 0
	for x in range(1, 11):
		for y in range(1, 11):
			if grid[x][y] == strike_emo:
				count_strike +=1
			elif grid[x][y] == cold_shot:
				count_miss +=1

	# print(f"{count_strike} strike found !\n")
	# print(f"{count_miss} cold shots found !\n")

	while True:	
		if count_strike > 0:
			for x in range(1, 11):
				for y in range(1, 11):
						if count_strike == 1:
							if x == coord_strike[0][0] and y == coord_strike[0][1]:
								if (grid[x+1][y] != strike_emo) and (grid[x-1][y] != strike_emo) and (grid[x][y-1] != strike_emo) and (grid[x][y+1] != strike_emo):
									# print("no strikes around")

									if (grid[x+1][y] != cold_shot):
										if grid[x+1][y] == ships[bato[-1]]['emo']:
											bato.append(bato[-1])
											coord_strike.append([x+1, y])
											grid[x+1][y] = strike_emo
											print_grid(grid)
											print("Touché en bas 😧")
											# cas torpilleur size 2
											if bato[-1] == 't':
												if len(coord_strike) == ships[bato[-1]]['size']:
													for i in range(ships[bato[-1]]['size']):
														grid[x+1-i][y] = sunk_emo
													time.sleep(1.5)
													print_grid(grid)
													print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
													if check_your_defeat(grid) == 'bye':
														return 'end'
													return grid
											return grid
										
										elif grid[x+1][y] not in ships[bato[-1]]['emo']:
											grid[x+1][y] = cold_shot
											print_grid(grid)
											print("Trop bas Hahaha ! Enfin c'est pas passé loin 😬")
											return grid

									#vert check
									if (grid[x+1][y] == cold_shot) and (grid[x-1][y] != cold_shot):
										# print("vert check 1 !")
										if grid[x-1][y] == ships[bato[-1]]['emo']:
											coord_strike.append([x-1, y])
											grid[x-1][y] = strike_emo
											print_grid(grid)
											print("Touché en haut 🤕")

											# cas torpilleur size 2
											if bato[-1] == 't':
												# print("vert check 1 torpilleur")
												# print("bato:", bato)
												# print("coord_strike:", coord_strike)
												if len(coord_strike) == ships[bato[-1]]['size']:
													# print("bato:", bato)
													# print("coord_strike:", coord_strike)
													for i in range(ships[bato[-1]]['size']):
														grid[x-1+i][y] = sunk_emo
													time.sleep(1.5)
													print_grid(grid)
													print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
													if check_your_defeat(grid) == 'bye':
														return 'end'
													return grid
											return grid

										if grid[x-1][y] not in ships[bato[-1]]['emo']:
											grid[x-1][y] = cold_shot
											print_grid(grid)
											print("Juste au dessus, vous avez eu chaud ! 😮")
											# print("bato:", bato)
											# print("coord_strike:", coord_strike)
											return grid

									elif (grid[x+1][y] != cold_shot) and (grid[x-1][y] == cold_shot):
										# print("vert check 2 !")
										if grid[x+1][y] == ships[bato[-1]]['emo']:
											coord_strike.append([x+1, y])
											grid[x+1][y] = strike_emo
											print_grid(grid)
											print("Touché en bas 😧")

											# cas torpilleur size 2
											if bato[-1] == 't':
												if len(coord_strike) == ships[bato[-1]]['size']:
													# print("bato:", bato)
													# print("coord_strike:", coord_strike)
													for i in range(ships[bato[-1]]['size']):
														grid[x+1-i][y] = sunk_emo
													time.sleep(1.5)
													print_grid(grid)
													print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
													if check_your_defeat(grid) == 'bye':
														return 'end'
													return grid
											return grid

										if grid[x+1][y] not in ships[bato[-1]]['emo']:
											grid[x+1][y] = cold_shot
											print_grid(grid)
											print("Trop bas Hahaha ! Enfin c'est pas passé loin 😬")
											# print("bato:", bato)
											# print("coord_strike:", coord_strike)
											return grid

									# hor check
									elif (grid[x+1][y] == cold_shot) and (grid[x-1][y] == cold_shot):
											# print("hor check 1 !")
											if grid[x][y-1] == ships[bato[-1]]['emo']:
												coord_strike.append([x, y-1])
												grid[x][y-1] = strike_emo
												print_grid(grid)
												print("Touché à gauche 😰")

												# cas torpilleur size 2
												if bato[-1] == 't':
													# print("bato:", bato)
													# print("coord_strike:", coord_strike)
													if len(coord_strike) == ships[bato[-1]]['size']:
														# print("bato:", bato)
														# print("coord_strike:", coord_strike)
														for i in range(ships[bato[-1]]['size']):
															grid[x][y-1+i] = sunk_emo
														time.sleep(1.5)
														print_grid(grid)
														print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
														if check_your_defeat(grid) == 'bye':
															return 'end'
														return grid
												return grid

											if grid[x][y-1] not in [ships[bato[-1]]['emo'], cold_shot]:
												grid[x][y-1] = cold_shot
												print_grid(grid)
												print("Trop à gauche ! La chance est avec vous")
												# print("bato:", bato)
												# print("coord_strike:", coord_strike)
												return grid

											if (grid[x][y-1] == cold_shot) and (grid[x][y+1] != cold_shot):
												# print("hor check 2 !")
												if grid[x][y+1] == ships[bato[-1]]['emo']:
													coord_strike.append([x, y+1])
													grid[x][y+1] = strike_emo
													print_grid(grid)
													print("Touché à droite 😨")

													# cas torpilleur size 2
													if bato[-1] == 't':
														# print("bato:", bato)
														# print("coord_strike:", coord_strike)
														if len(coord_strike) == ships[bato[-1]]['size']:
															for i in range(ships[bato[-1]]['size']):
																grid[x][y+1-i] = sunk_emo
															time.sleep(1.5)
															print_grid(grid)
															print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
															if check_your_defeat(grid) == 'bye':
																return 'end'
															return grid
													return grid

												if grid[x][y+1] not in [ships[bato[-1]]['emo'], cold_shot]:
													grid[x][y+1] = cold_shot
													print_grid(grid)
													print("Manqué, trop à droite cette fois !")
													# print("bato:", bato)
													# print("coord_strike:", coord_strike)
													return grid
						
						# 2 strikes at least, direction found
						else:
							row = coord_strike[-1][0]
							col = coord_strike[-1][1]
							# print("row:", row)
							# print("col:", col)
							if (grid[row+1][col] == strike_emo) and (grid[row-1][col] not in [strike_emo, cold_shot]):
								if grid[row-1][col] == ships[bato[-1]]['emo']:
									grid[row-1][col] = strike_emo
									coord_strike.append([row-1, col])
									print_grid(grid)
									print("Touché en haut 🤕")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)

									# sunk check
									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row-1+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									return grid
								else:
									grid[row-1][col] = cold_shot

									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									
									else:
										row = coord_strike[::-1][-1][0]
										col = coord_strike[::-1][-1][1]
										# print("back_to:", row, col)

									print_grid(grid)
									print("Juste au dessus, vous avez eu chaud ! 😮")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									return grid

							elif (grid[row-1][col] == strike_emo) and (grid[row+1][col] not in [strike_emo, cold_shot]):
								if grid[row+1][col] == ships[bato[-1]]['emo']:
									grid[row+1][col] = strike_emo
									coord_strike.append([row+1, col])
									print_grid(grid)
									print("Touché en bas 😧")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)

									# sunk check
									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row+1-i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									return grid
								else:
									grid[row+1][col] = cold_shot
									
									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									
									else:
										row = coord_strike[::-1][-1][0]
										col = coord_strike[::-1][-1][1]
										# print("back_to:", row, col)
									
									print_grid(grid)
									print("Trop bas Hahaha ! Enfin c'est pas passé loin 😬")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									return grid

							elif (grid[row-1][col] == strike_emo) and (grid[row+1][col] ==  cold_shot):
								row = coord_strike[::-1][-1][0]
								col = coord_strike[::-1][-1][1]
								if grid[row-1][col] == ships[bato[-1]]['emo']:
									grid[row-1][col] = strike_emo
									coord_strike.append([row-1, col])
									print_grid(grid)
									print("Touché en haut 🤕")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)

									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row-1+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									return grid
								else:
									grid[row-1][col] = cold_shot

									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid

									print("Juste au dessus, vous avez eu chaud ! 😮")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									return grid


							elif (grid[row][col-1] == strike_emo) and (grid[row][col+1] not in [strike_emo, cold_shot]):
								if grid[row][col+1] == ships[bato[-1]]['emo']:
									coord_strike.append([row, col+1])
									grid[row][col+1] = strike_emo
									print_grid(grid)
									print("Touché à droite 😨")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)

									# sunk check
									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row][col+1-i] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									return grid

								else:
									grid[row][col+1] = cold_shot

									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									
									else:
										row = coord_strike[::-1][-1][0]
										col = coord_strike[::-1][-1][1]
										# print("back_to:", row, col)

									print_grid(grid)
									print("Manqué, trop à droite !")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									return grid
							
							elif (grid[row][col+1] == strike_emo) and (grid[row][col-1] not in [strike_emo, cold_shot]):
								if grid[row][col-1] == ships[bato[-1]]['emo']:
									coord_strike.append([row, col-1])
									grid[row][col-1] = strike_emo
									print_grid(grid)
									print("Touché à gauche 😰")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)

									# sunk check
									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row][col-1+i] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									return grid
								else:
									grid[row][col-1] = cold_shot

									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row+i][col] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									
									else:
										row = coord_strike[::-1][-1][0]
										col = coord_strike[::-1][-1][1]
										# print("back_to:", row, col)

									print_grid(grid)
									print("Trop à gauche ! La chance est avec vous")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									return grid

							elif (grid[row][col+1] == strike_emo) and (grid[row][col-1] == cold_shot):
								row = coord_strike[::-1][-1][0]
								col = coord_strike[::-1][-1][1]
								if grid[row][col+1] == ships[bato[-1]]['emo']:
									coord_strike.append([row, col+1])
									grid[row][col+1] = strike_emo
									print_grid(grid)
									print("Touché à droite 😨")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row][col+1-i] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									return grid
								else:
									grid[row][col+1] = cold_shot

									if len(coord_strike) == ships[bato[-1]]['size']:
										for i in range(ships[bato[-1]]['size']):
											grid[row][col-i] = sunk_emo
										time.sleep(1.5)
										print_grid(grid)
										print(f"Votre {ships[bato[-1]]['name']} est coulé 😵")
										if check_your_defeat(grid) == 'bye':
											return 'end'
										return grid
									
									print_grid(grid)
									print("Manqué, trop à droite !")
									# print("bato:", bato)
									# print("coord_strike:", coord_strike)
									return grid

	
		else:
			bato.clear()
			coord_strike.clear()
			random_row = random.randint(1, 10)
			random_col = random.randint(1, 10)
			if grid[random_row][random_col] == emo_sea:
				grid[random_row][random_col] = cold_shot
				print_grid(grid)
				print("Ouf! c'est Manqué")
				return grid
			else:
				for k, v in ships.items():
					if grid[random_row][random_col] == ships[k]['emo']:
						bato.append(k)
						coord_strike.append([random_row, random_col])
						grid[random_row][random_col] = strike_emo
						print_grid(grid)
						print(f"Aïe ! Votre {ships[k]['name']} est touché 😬")
						# print("bato:", bato)
						# print("coord_strike:", coord_strike)
						return grid
						


def game():
	grid = make_grid()
	grid_algo = make_opponent_grid()
	grid_attack = make_grid()

	print(warship_pic)
	print(title)
	print_grid(grid)
	place_your_ships(grid)
	print_grid(grid_attack)
	while True:
		# print_grid(grid_algo)
		print('\n')
		grid_attack = you_play(grid_algo, grid_attack)
		if grid_attack == 'end':
			print("La grille de votre adversaire était la suivante:")
			print_grid(grid_algo)
			print('\n')
			break
		grid = algo_player(grid)
		if grid == 'end':
			print("La grille de votre adversaire était la suivante:")
			print_grid(grid_algo)
			print('\n')
			break


game()
