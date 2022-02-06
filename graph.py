class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([(0,-1) for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2, dist):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = (1,dist)
        self.adjMatrix[v2][v1] = (1,dist)

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = (0,-1)
        self.adjMatrix[v2][v1] = (0,-1)

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(f'({val[0],val[1]})', end = ":"),
            print
            print

    def get_children(self, i):
        row = self.adjMatrix[i]
        children = []
        for j in range(len(row)):
            if row[j][0] == 1:
                children.append(j)
        return children