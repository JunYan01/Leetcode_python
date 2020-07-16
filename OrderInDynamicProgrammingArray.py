# OrderInDynamicProgrammingArray.py

# m = 5
# n = 8

# dp = [[0]*n for _ in range(m)]

# count = 0
# for i in range(m):
# 	for j in range(n):
# 		count += 1
# 		dp[i][j] = count

# for i in range(m):
# 	print(i,dp[i])

# for i in range(m-1,-1,-1):
# 	count += 1
# 	dp[i][i] = count
# 	for j in range(i+1,n):
# 		count += 1
# 		dp[i][j] = count

# for i in range(m):
# 	print(i,dp[i])

# m = 5
# n = 5

# dp = [[0]*n for _ in range(m)]

# count = 0

# for l in range(0,m):
# 	# count += 1
# 	# dp[i][i] = count
# 	j = 0+ l
# 	count += 1
# 	dp[0][j] = count


# 	for i in range(1,m-l):
# 		j = i+l
# 		count += 1
# 		dp[i][j] = count

# for i in range(m):
# 	print(i,dp[i])

m = 5
n = 5

dp = [[0]*n for _ in range(m)]

count = 0

for l in range(0,m):
	# count += 1
	# dp[i][i] = count
	
	for i in range(m-l-1,0,-1):
		j = i+l
		count += 1
		dp[i][j] = count

	j = 0+ l
	count += 1
	dp[0][j] = count

for i in range(m):
	print(i,dp[i])
