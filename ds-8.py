class Graph:
    def __init__(self):
        self.numVertices = 4

        self.locations = ['A', 'B', 'C', 'D']

        # Adjacency matrix for DFS
        self.adjMatrix = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ]

        # Adjacency list for BFS
        self.adjList = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C']
        }

    # DFS
    def DFS(self, start):
        visited = [False] * self.numVertices

        print("\nDFS sequence (Adjacency Matrix): ", end="")
        self.dfsHelper(self.locations.index(start), visited)
        print()

    def dfsHelper(self, node, visited):
        print(self.locations[node], end=" ")
        visited[node] = True

        for i in range(self.numVertices):
            if self.adjMatrix[node][i] == 1 and not visited[i]:
                self.dfsHelper(i, visited)

    # BFS
    def BFS(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        print("\nBFS sequence (Adjacency List): ", end="")

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.adjList[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        print()

    # Menu
    def menu(self):
        start = 'A'

        while True:
            print("\n===== MENU =====")
            print("1. DFS")
            print("2. BFS")
            print("3. Exit")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Invalid choice!")
                continue

            if choice == 1:
                self.DFS(start)
            elif choice == 2:
                self.BFS(start)
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    g = Graph()
    g.menu()
