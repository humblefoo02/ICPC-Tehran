def max_height_difference(heights):
    # Sort the list of heights
    heights.sort()

    # This will store the optimal arrangement of guests
    arranged = [0] * len(heights)

    # Start filling from the middle of the arranged array
    mid_index = len(heights) // 2
    arranged[mid_index] = heights[0]

    # Alternate placements from the sorted list
    left = mid_index - 1
    right = mid_index + 1
    left_heights = True  # This flag helps alternate between placing to the left and right

    for height in heights[1:]:
        if left_heights:
            if left >= 0:
                arranged[left] = height
                left -= 1
            else:
                arranged[right] = height
                right += 1
        else:
            if right < len(heights):
                arranged[right] = height
                right += 1
            else:
                arranged[left] = height
                left -= 1
        left_heights = not left_heights

    # Compute the maximum height difference
    max_diff = abs(arranged[0] - arranged[-1])
    for i in range(1, len(arranged)):
        max_diff = max(max_diff, abs(arranged[i] - arranged[i - 1]))

    return max_diff


# Example input
n = int(input())
heights = list(map(int, input().split()))

# Calculate and print the result
result = max_height_difference(heights)
print(result)
