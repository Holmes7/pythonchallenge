# Had to use hints

import pickle

with open('assets/banner.p', 'rb') as f:
	data = pickle.load(f)

for x in data:
	for y in x:
		for z in range(int(y[1])):
			print(y[0], end="")

	print("")
