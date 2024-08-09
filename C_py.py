def can_win(n):
  """
  Determines whether Sara can win the game.

  Args:
      n: The number of coins Sara has.

  Returns:
      True if Sara can win, False otherwise.
  """
  return n % 5 == 0

# Example usage
print(can_win(1))  # Output: False
print(can_win(2))  # Output: True
