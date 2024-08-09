num_pillars = int(input())
pillars = []

for _ in range(num_pillars):
    height, cost = map(int, input().split())
    pillars.append([height, cost])

# Initialize the dp array with maximum values
dp = [[float('inf')] * 3 for _ in range(num_pillars + 1)]
dp[0] = [0, 0, 0]

# Iterate over each pillar
for i in range(1, num_pillars + 1):
    # Iterate over each possible increase in height
    for k in range(3):
        # Calculate the cost to increase the height of the current pillar by k
        current_cost = dp[i - 1][k] + k * pillars[i - 1][1]

        # Update the minimum cost in dp array
        for j in range(3):
            if pillars[i - 1][0] + k != pillars[i - 2][0] + j:
                dp[i][k] = min(dp[i][k], current_cost)
            else:
                dp[i][k] = min(dp[i][k], dp[i - 1][j] + k * pillars[i - 1][1])

# Find the minimum cost to fix all pillars
answer = min(dp[num_pillars])
print(answer)
