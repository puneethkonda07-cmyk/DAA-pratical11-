# Floyd-Warshall Algorithm to find shortest distances
# between every pair of vertices

INF = 10**9

def floydWarshall(V, graph):
    # Initialize the distance matrix
    dist = [row[:] for row in graph]

    # Apply Floyd-Warshall Algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update distance if a shorter path exists
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    # Check for negative weight cycles
    for i in range(V):
        if dist[i][i] < 0:
            print("Warning: Negative weight cycle detected!")
            return

    # Print the shortest distance matrix 
    print("Shortest distance matrix between every pair of vertices:")

    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print(f"{'INF':>5}", end="")
            else:
                print(f"{dist[i][j]:>5}", end="")
        print()


def main():
    # Number of vertices
    V = 4

    # Graph adjacency matrix
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]

    floydWarshall(V, graph)


if __name__ == "__main__":
    main()

print(92460118292)
