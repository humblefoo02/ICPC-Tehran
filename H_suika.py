from collections import deque

def min_button_presses(f, s, g, u, d):
    if s == g:
        return 0
    queue = deque([(s, 0)])
    visited = set([s])

    while queue:
        current_floor, presses = queue.popleft()
        for next_floor in (current_floor + u, current_floor - d):
            if next_floor == g:
                return presses + 1
            if 1 <= next_floor <= f and next_floor not in visited:
                visited.add(next_floor)
                queue.append((next_floor, presses + 1))

    return "use the stairs"


# Example usage
inputs = input().split()
f = int(inputs[0])
s = int(inputs[1])
g = int(inputs[2])
u = int(inputs[3])
d = int(inputs[4])
print(min_button_presses(f, s, g, u, d))
