import itertools

turns = 15
outcomes = itertools.product([0, 1], repeat = turns)
tprob = 0
for outcome in outcomes:
	if sum(outcome) <= turns/2.0:
		continue
	oprob = 1
	for i in xrange(0, turns):
		if outcome[i] == 1:
			oprob *= 1.0/(i+2)
		else:
			oprob *= (i+1.0)/(i+2)
	tprob += oprob
print tprob

i = 0
while (i+1)*tprob < 1:
	i += 1
print i