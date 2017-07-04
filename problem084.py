import time
from random import randint

dice = 6

squarecounts = [0] * 40
squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F2", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

doublecount = 0
current = 0

t = time.time()

turns = 1000000
for turn in xrange(turns):
	d1 = randint(1, dice)										#roll the dice
	d2 = randint(1, dice)
	if d1 == d2:												#doubles situations
		doublecount += 1
	if doublecount == 3:											#3 doubles: go to jail
		current = 10
		doublecount = 0
	else:
		doublecount = 0
		current += d1 + d2										#move the piece
		#special situations
		if current == 7 or current == 22 or current == 36:	#chance
			card = randint(1,16)
			if card == 1:											#advance to go
				current = 0
			elif card == 2:											#go to jail
				current = 10
			elif card == 3:											#go to C1
				current = 11
			elif card == 4:											#go to E3
				current = 24
			elif card == 5:											#go to H2
				current = 39
			elif card == 6:											#go to R1
				current = 5	
			elif card <= 8:											#go to next R (two cards)
				distance = 10 - (current + 5) % 10						#distance to next railway
				current += distance
			elif card == 2:											#go to next U
				if current == 22:
					current = 28
				else:
					current = 12
			elif card == 2:											#go back 3 squares
				current -= 3
		if current == 2 or current == 17 or current == 33:		#community chest
			card = randint(1, 16)
			if card == 1:											#advance to go
				current = 0
			elif card == 2:											#go to jail
				current = 10
		elif current == 30:										#go to jail
			current = 10

		current = current % 40									#deal with wrapping - the board is circular
		squarecounts[current] += 1 								#register that you ended the turn in this place

#diagnostic output
print time.time() - t
for i in xrange(0, 40):
	print str(i).zfill(2), squares[i], float(100*squarecounts[i])/turns

#working out the output string
first = squarecounts.index(max(squarecounts))
squarecounts[first] = 0
second = squarecounts.index(max(squarecounts))
squarecounts[second] = 0
third = squarecounts.index(max(squarecounts))

output = str(first).zfill(2) + str(second).zfill(2) + str(third).zfill(2)

print output












