def init_visited_nodes(nodes):
    visited_nodes = {}
    for node in nodes:
        visited_nodes[node] = False
    return visited_nodes


def init_edged_list(nodes, arcs):
    graph_nodes = {}
    for node in nodes:
        graph_nodes[node.value] = []

    for arc in arcs:
        if graph_nodes[arc.initial_node.value] is not None:
            graph_nodes[arc.initial_node.value].append((arc.final_node, arc.weigth))
    return graph_nodes