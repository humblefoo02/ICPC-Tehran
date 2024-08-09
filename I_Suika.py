def planting_flowers(m, n):
    MOD = 1000000007

    # Handle small grids separately
    if m == 1 and n == 1:
        return 2
    elif m == 1 and n == 2:
        return 2
    elif m == 2 and n == 1:
        return 2
    elif m == 2 and n == 2:
        return 4

    # Initialize the dp array
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = dp[0][1] = 1

    # Fill the dp array
    for i in range(1, m):
        new_dp = [[0] * 2 for _ in range(n)]
        for j in range(n):
            for k in range(2):
                for dj in [-1, 0, 1]:
                    nj = j + dj
                    if 0 <= nj < n:
                        new_dp[nj][1 - k] += dp[j][k]
                        new_dp[nj][1 - k] %= MOD
        dp = new_dp

    # Sum up the results for all possible ending configurations
    result = sum(map(sum, dp))

    return result % MOD


# Taking input in a single line
m, n = map(int, input().strip().split())

# Example usage
print(planting_flowers(m, n)*2)
