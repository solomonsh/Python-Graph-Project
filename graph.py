class Graph:
    def __init__(self, name=""):
        self.graph_dict = {}
        self.name = name

    # Add vertex to the graph.
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    # Add edge to the graph
    def add_edge(self, from_vertex, to_vertex):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)

    # Get how many nodes there are in the graph
    def get_graph_info(self):
        print(f"The Graph {self.name} has {len(self.graph_dict.keys())} nodes")

    # print the graph
    def __repr__(self):
        graph_rep = ""
        for key, val in self.graph_dict.items():
            graph_rep += f"{key} influences {val.edges}\n"

        return graph_rep
