import numpy as np
import random
import math

# setup colors
red = '\033[91m'
green = '\33[32m'
yellow = '\33[43m'
clearColor = '\033[0m'

def distance(x,y,i,z):
	dist = (i-x)**2 + (y-z)**2
	#print dist
	dist = math.sqrt(dist)
	return dist

# sets up random grid of mines
grid = np.zeros((8,8), dtype=np.int8)
for i in range(8):
	# 0 = safe hiden
	# 1 = mine
	# 2 = revealed
	for z in range(8):
		if random.getrandbits(32) % 6 == 1:
			grid[z][i] = 1

		z = z + 1
	i = i + 1
#print grid

# get nearby mines and clear all zeros
def near(grid, x, y):
	position = grid[x][y]
	count = 0

	for i in range(8):
	        for z in range(8):
			if distance(x,y,z,i) < 2:
				if grid[z][i] == 1:
					count = count + 1
				if grid[z][i] == 0:
					gridView[z][i] = "O"

               		z = z + 1
        	i = i + 1

	# should return str number
	return str(count)

gridView = np.chararray((8,8))
gridView[:] = '?'

#i = 0
#for x in gridView:
#	gridView[i] = "?"
#	i = i+1

# clean up grid and add colors
print str(gridView).replace("'","").replace("]]","]").replace("[["," [").replace("?","{0}?{1}").format(yellow, clearColor)

while 1:
	choice = list(str(raw_input("Select Square X,Y> ")))
	#choice = choice.split(',')


	#x=int(choice[0].replace('(','')) - 1
	#y=int(choice[1].replace(')','').replace(' ', '')) - 1
	y = int(choice[0]) -1
	x = int(choice[1]) -1
	# m for mine, f for flag
	action = choice[2]

	# user mined a mine
	if grid[x][y] == 1 and action == "m":
		print "game over."
		exit()

	# user mined a safe square
	if grid[x][y] == 0 and action == "m":
		gridView[x][y] = near(grid,x,y)
	if action == "f":
		gridView[x][y] = "!"

	print str(gridView).replace("'","").replace("]]","]").replace("[["," [").replace("?","{0}?{1}").format(yellow, clearColor).replace("O","{0}O{1}").format(green, clearColor)




