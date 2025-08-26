import qiskit
import math

# 1. Setup
# Define coefficients
epsilon = 0.2
delta = 0.05
ev_delta = 0.35


# 2. Algorithm
# Coefficients
K = 4 					# Number of elements in truncated Taylor series
l_part = 0
for i in range(1,K+1):
	l_part += 1/i
l_part = 4 * l_part / epsilon
L = math.log1p(l_part) * 1 / (ev_delta * ev_delta)
Ml_array = []
for l in range(math.ceil(L+1)):
	Ml = math.ceil(math.sqrt(math.log1p(l_part)*l/2))
	Ml_array.append(Ml)

# Calculating blk
def get_blk(K,L):
	blk_matrix = []
	for k in range(1, K + 1):
		bk_array = []
		for l in range(math.ceil(L + 1)):
			if k == 1:
				if l%2 == 0:
					blk = 0.0
				else:
					blk = 2 * math.comb(l-1,int((l-1)/2))/(math.pi*math.pow(2,l-1)*l)
				bk_array.append(blk)
			else:
				blk = 0.0
				for l_prime in range(l+1):
					blk += blk_matrix[k-2][l_prime]*blk_matrix[0][l-l_prime]
				bk_array.append(blk)

		blk_matrix.append(bk_array)

	return blk_matrix

print(get_blk(K,L))