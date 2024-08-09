import sys
from heapq import heappop, heappush

def minimum_travel_cost(n, m, connections):
    if m == 0:
        return -1

    graph = [[] for _ in range(n + 1)]
    for pi, qi, ci in connections:
        graph[pi].append((qi, ci))
        graph[qi].append((pi, ci))

    pq = [(0, 1, 0)]  # Start from station 1 with cost 0 and no last company
    distances = [[float('inf')] * 101 for _ in range(n + 1)]  # Initialize distances to infinity for each company
    distances[1][0] = 0  # Distance to start node is 0 for no company

    while pq:
        current_cost, current_station, last_company = heappop(pq)
        if current_station == n:
            return current_cost  # Found the minimum cost to reach station n

        if current_cost > distances[current_station][last_company]:
            continue  # Skip if we have found a better path to this station

        for next_station, cost in graph[current_station]:
            new_cost = current_cost if last_company == 0 else current_cost + cost
            next_company = 0 if cost < distances[next_station][last_company] else last_company
            if new_cost < distances[next_station][next_company]:
                distances[next_station][next_company] = new_cost
                heappush(pq, (new_cost, next_station, next_company))

    return -1  # If station n is not reachable

def run():
    n, m = map(int, input().split())
    connections = []
    for _ in range(m):
        pi, qi, ci = map(int, input().split())
        connections.append((pi, qi, ci))

    result = minimum_travel_cost(n, m, connections)
    print(result)

if __name__ == "__main__":
    run()
