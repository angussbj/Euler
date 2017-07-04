import math
import sys

def isfig(k):
	out = [0, 0, 0, 0, 0, 0]
	# Check if triangular:
	value = (math.sqrt(1+8*k)-1)/2
	if value == int(value):
		out[0] = 1
	# Check if square:
	value = math.sqrt(k)
	if value == int(value):
		out[1] = 1
	# Check if pentagonal:
	value = (math.sqrt(1+24*k)+1)/6
	if value == int(value):
		out[2] = 1
	# Check if hexagonal:
	value = (math.sqrt(1+8*k)+1)/4
	if value == int(value):
		out[3] = 1
	# Check if heptagonal:
	value = (math.sqrt(9+40*k)+3)/10
	if value == int(value):
		out[4] = 1
	# Check if triangular:
	value = (math.sqrt(4+12*k)+2)/6
	if value == int(value):
		out[5] = 1
	return out

posns = []
posfs = []
poscs = []
for a in xrange(1010, 10000): #start at 1010 for full run
	# print a
	stra = list(str(a))
	if int(stra[2]) == 0:
		continue
	fa = isfig(a)
	if sum(fa) != 0:
		startb = 10 + 100 * int(''.join(stra[2:]))
		for b in xrange(startb, startb + 90):
			fb = isfig(b)
			if sum(fb) != 0:
				strb = list(str(b))
				startc = 10 + 100 * int(''.join(strb[2:]))
				for c in xrange(startc, startc + 90):
					fc = isfig(c)
					if sum(fc) != 0:
						strc = list(str(c))
						startd = 10 + 100 * int(''.join(strc[2:]))
						for d in xrange(startd, startd + 90):
							fd = isfig(d)
							if sum(fd) != 0:
								strd = list(str(d))
								starte = 10 + 100 * int(''.join(strd[2:]))
								for e in xrange(starte, starte + 90):
									fe = isfig(e)
									if sum(fe) != 0:
										stre = list(str(e))
										f = 100 * int(''.join(stre[2:])) + int(''.join(stra[:2]))
										ff = isfig(f)
										if sum(ff) != 0:
											possible = True
											# if one of the figurate types isn't covered, ignore this pattern
											fssum = []
											for i in xrange(0, 6):
												fssum.append(fa[i]+fb[i]+fc[i]+fd[i]+fe[i]+ff[i])
											if fssum.count(0) != 0:
												continue
											# now let's check that there's a way to cover them properly
											covered = [0]*6
											oldlist = [a,b,c,d,e,f]
											numbers = oldlist[:]
											oldlist = [fa,fb,fc,fd,fe,ff]
											isfigs = oldlist[:]
											sums = [0]*6
											i = 0
											while i < len(isfigs):
												sums[i] = sum(isfigs[i])
												if sums[i] == 0:
													possible = False
													break
												if sums[i] == 1:
													for j in xrange(0,6):
														if isfigs[i][j] == 1:
															covered[j] = 1
															del isfigs[i]
															del sums[i]
															del numbers[i]
															for isfigi in isfigs:
																isfigi[j] = 0
															break
													i = -1
												i += 1
											if not possible:
												continue
											if covered.count(0) > len(numbers):
												continue
												print "continued"
											if covered.count(1) == 6:
												print [a,b,c,d,e,f]							
												print [isfig(a),isfig(b),isfig(c),isfig(d),isfig(e),isfig(f)]
												print sum([a,b,c,d,e,f])
												sys.exit()
											else:
												posns.append([a,b,c,d,e,f])						
												posfs.append([isfig(a),isfig(b),isfig(c),isfig(d),isfig(e),isfig(f)])
												poscs.append(covered)


												
for i in xrange(0, len(posns)):
	print posns[i]
	print posfs[i]
	print poscs[i]






















