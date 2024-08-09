def count_collisions(ants):
    # Dictionaries to store the positions of ants moving in different directions
    vertical_moves = {}  # Tracks ants moving upward
    horizontal_moves = {}  # Tracks ants moving rightward

    # Populate the dictionaries with potential collision points
    for x, y, direction in ants:
        if direction == 'U':
            if x not in vertical_moves:
                vertical_moves[x] = []
            vertical_moves[x].append(y)
        elif direction == 'R':
            if y not in horizontal_moves:
                horizontal_moves[y] = []
            horizontal_moves[y].append(x)

    # Sort the lists of coordinates to facilitate collision counting
    for key in vertical_moves:
        vertical_moves[key].sort()
    for key in horizontal_moves:
        horizontal_moves[key].sort()

    # Count collisions
    collisions = 0
    from bisect import bisect_left, bisect_right
    for x in vertical_moves:
        if x in horizontal_moves:
            for y in vertical_moves[x]:
                # Use binary search to find collisions efficiently if y key exists in horizontal_moves
                if y in horizontal_moves:
                    collision_count = bisect_right(horizontal_moves[y], x) - bisect_left(horizontal_moves[y], x)
                    collisions += collision_count

    return collisions


# Example Input
ants = [
    (1, 2, 'R'),
    (2, 1, 'U'),
    (3, 1, 'U')
]

print(count_collisions(ants))
