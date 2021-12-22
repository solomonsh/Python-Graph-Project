# %%
import csv
from graph import Graph
from vertex import Vertex
from pyvis.network import Network


def parse_csv_to_graph(path):
    try:
        comedians = Graph("Comedians")

        # Opening the file, creating a vertex object, and adding edges to the graph

        with open(path, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                vertex1 = Vertex(row['source'])
                vertex2 = Vertex(row['target'])
                if len(row['source']) == 0 or len(row['target']) == 0:
                    continue
                else:
                    if row['source'] not in comedians.graph_dict:
                        comedians.add_vertex(vertex1)
                    if row['target'] not in comedians.graph_dict:
                        comedians.add_vertex(vertex2)
                comedians.add_edge(vertex1, vertex2)
        return comedians
    except:
        return None


comedians_graph = parse_csv_to_graph('comedians.csv')

# This function receives CSV file and creates a graph object of the comedians and return the graph object

# Test

# Graph info
comedians_graph.get_graph_info()
# print(comedians_graph)

# %%


def influence_chains(diagram, start, end=None):
    # handling edge cases
    if start == "":
        return "Please provide a comedian name to start with"
    if start not in diagram.graph_dict:
        return "The comedian is not in the graph!"

    # Using BFS to traverse through the graph and return the path
    path = [start]
    vertex_and_path = [start, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)

        for neighbor in diagram.graph_dict[current_vertex].edges:
            if neighbor not in visited:
                if neighbor == end:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])

    # If the comedians passed as the end is None return all comedians influenced(direct + indirect) by the start comedian
    # If there is no chain between the start and end return an error message
    if end == None:
        return {start: list(visited)}
    else:
        return "There is no influence chains between the comedians!"


# This function returns influence chains between two comedians

# Test
# print(influence_chains(comedians_graph,"Buster Keaton","Jessica Williams"))
# print(influence_chains(comedians_graph,"Gracie Allen"))

# %%
def top_10_influencers(diagram):
    #  Add all comedians and number of their direct + indirect influences to a dictionary
    comedians_influence = {}
    for comedian in diagram.graph_dict.keys():
        comedians_influence[comedian] = len(
            influence_chains(diagram, comedian)[comedian])
    # Sort the dictionary and return top 10 influenceres
    comedians_influence_sorted = [key[0] for key in sorted(
        comedians_influence.items(), key=lambda x: x[1])]
    comedians_influence_reversed = comedians_influence_sorted[::-1]
    return comedians_influence_reversed[:10]

# This function returns top 10 influencers from the comedian graph ( Considers both direct and indirect influences )
# Test
print(top_10_influencers(comedians_graph))


# %%
def draw_graph(diagram, node_size=4, edge_size=0.2):
    # Creating the directed network variable
    network = Network('500px', '1500px', directed=True)
    network.barnes_hut()

    # Adding nodes to the network
    for node, value in diagram.graph_dict.items():
        title = str(node).split()[0]
        network.add_node(node, title=str(node), label=title,
                         size=(len(value.edges)+5)*10)

    # Adding edges to the network
    for key, val in diagram.graph_dict.items():
        for node in val.edges:
            network.add_edge(key, node, physics=False)

    # Generating html file for the network
    network.show_buttons()
    network.show('comedians.html')


# This function creates a network of the comedian graph using pyvis library
# Test
# draw_graph(comedians_graph)

# %%
