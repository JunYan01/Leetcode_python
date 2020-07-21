# 877. Stone Game

piles = [3, 9, 1, 2]

n = len(piles)

dp = [[(0,0)]*n for _ in range(n)]

for i in range(n):
	dp[i][i] = (piles[i],0)
	# print(dp[i])

# for i in range(n-2,-1,-1):
# 	for j in range(i+1,n):
# 		left = piles[i] + dp[i+1][j][1]
# 		right = piles[j] + dp[i][j-1][1]
# 		if left >= right:
# 			dp[i][j] = (left,dp[i+1][j][0])
# 		else:
# 			dp[i][j] = (right,dp[i][j-1][0])

for l in range(1,n):
	for i in range(0,n-l):
		j = i + l
		left = piles[i] + dp[i+1][j][1]
		right = piles[j] + dp[i][j-1][1]
		if left >= right:
			dp[i][j] = (left,dp[i+1][j][0])
		else:
			dp[i][j] = (right,dp[i][j-1][0])

for i in range(n):
	print(dp[i])

# 
print(dp[0][n-1][0])

