import random
# TO DO: output to log file

startseq()

def startseq():
	print("Welcome to Secret Hitler!")

	noplayers = input("How many people are playing?")
	noplayers = int(noplayers)
	if noplayers < 5:
		print("ERROR: There aren't enough players!")
	elif noplayers > 10:
		print("ERROR: There are too many players!")
	# Asks for p number of players and adds them to a list
	else:
		players = []
		while p < noplayers:
			name = input("Enter name of a player")
			player = {
				'id': p,
				'name': name,
			}
			players.append(player)
			p += 1

	# continues to assign role phase 
	rolecount()

def rolecount():
	# passes correct no of lib/fasc to roleassign
	if noplayers == 5:
		roleassign(3, 1) 
	elif noplayers == 6:
		roleassign(4, 1) 
	elif noplayers == 7:
		roleassign(4, 2) 
	elif noplayers == 8:
		roleassign(5, 2)
	elif noplayers == 9:
		roleassign(5, 3)
	elif noplayers == 10:
		roleassign(6, 3)
	else:
		print("ERROR: Number of players seems invalid?")

def roleassign(l, f):
	print("Assigning roles...")
	random.shuffle(players)
	# assign liberals
	while x < l:
		lib = players.pop(0)
		i = lib['id']
		name = lib['name']
		players[-1] = {
			'id': i,
			'name': name,
			'role': liberal,
			'party': liberal,
		}
		x += 1
	while y < f:
		fasc = players.pop(0)
		i = fasc['id']
		name = fasc['name']
		players[-1] = {
			'id': i,
			'name': name,
			'role': fascist,
			'party': fascist,
		}
	hitler = players.pop(0)
	i = hitler['id']
	name = hitler['name']
	players[-1] = {
		'id': i,
		'name': name,
		'role': hitler,
		'party': fascist,
	}

def rolecom():










