num_pillars = int(input())
pillars = []

for _ in range(num_pillars):
    height, cost = map(int, input().split())
    pillars.append([height, cost])


cost = 0
for _ in range(2):
    for i in range(num_pillars-1):
        if pillars[i][0] == pillars[i+1][0]:
            if pillars[i][1] <= pillars[i+1][1]:
                pillars[i][0] += 1
                cost += pillars[i][1]
            elif pillars[i][1] > pillars[i+1][1]:
                pillars[i+1][0] += 1
                cost += pillars[i+1][1]

print(cost)


