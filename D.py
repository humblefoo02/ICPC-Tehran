def binary_majid(n, t, operations):
  """
  This function finds the minimum number of times Majid needs to use his superpower
  to restore a binary string of length n that was destroyed in t steps.

  Args:
      n: Length of the binary string.
      t: Number of steps of destruction.
      operations: Sequence of integers representing the order in which the niece destroys bits.

  Returns:
      A tuple containing:
          k: Minimum number of times Majid needs to use his superpower.
          intervals: List of tuples representing the intervals that Majid should negate in each use.
  """
  # Initialize an array to store the state of the bits (0 or 1)
  bits = [1] * n

  # Process each destruction operation
  for op in operations:
    # Reverse and negate the bits from op to n-1 (inclusive)
    for i in range(op, n):
      bits[i] = 1 - bits[i]

  # Track the current state (0 or 1) and required intervals
  current_state = bits[0]
  intervals = []
  start = 0
  for i in range(1, n):
    # If the state changes, record the interval and update current state
    if bits[i] != current_state:
      intervals.append((start, i - 1))
      current_state = bits[i]
      start = i

  # Add the last interval if needed
  if start < n - 1:
    intervals.append((start, n - 1))

  return len(intervals), intervals

# Example usage
n = 5
t = 2
operations = [3, 1]  # Destroy bits 3, 1 (0-based indexing)

k, intervals = binary_majid(n, t, operations)

print(f"Minimum number of times Majid needs to use his superpower: {k}")
print(f"Intervals to negate: {intervals}")
