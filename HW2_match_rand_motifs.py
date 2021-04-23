import numpy as np

N = 90000
x = 0.6
seq = 'ATAGCCGA'

nucl = ['A', 'T', 'G', 'C']
PA = 0.5*(1 - x)
PT = 0.5*(1 - x)
PG = 0.5*x
PC = 0.5*x
probs = [PA, PT, PG, PC]

Ntests = 100 # more tests, better precision
success = 0 # one rndseq equals seq
# perform simulations
for i in range(Ntests):
	count = 0
	for j in range(N):
		# generate random sequence with probs as python string
		rndseq = np.random.choice(nucl, len(seq), p=probs).astype('|S1').tostring().decode('utf-8')
		# count events with equal strings
		if rndseq == seq:
			count += 1
	print(i, count) # just for information
	# if at least one is found - success
	if count > 0:
		success += 1

# probability to find at least one
print(success/Ntests)
