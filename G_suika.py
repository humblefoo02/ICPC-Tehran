def count_partitions(n):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one way to partition 0: using no bricks at all

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] = (dp[j] + dp[j - i]) % MOD

    return dp[n]

# Example usage
n = int(input())
print(count_partitions(n))
