class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    # Add edge to the vertex
    def add_edge(self, vertex):
        self.edges.append(vertex)

    # Return edges of the vertex
    def get_edges(self):
        return self.edges
