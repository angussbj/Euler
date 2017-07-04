import os

for filename in os.listdir("."):
	if filename.startswith("problem"):
		digitcount = 0
		for character in filename[7:]:
			if character.isdigit():
				digitcount += 1
		if digitcount == 1:
			os.rename(filename, filename[:7] + '00' + filename[7:])
		elif digitcount == 2:
			os.rename(filename, filename[:7] + '0' + filename[7:])