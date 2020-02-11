# Graph is an ordered pair or Arc-edges(E) and nodes-vertices(V) G = (V, E)
# ordered pair (a, b) !== (b, a) if a !== b
# unordered {a, b} == {b, a}
# edges(arc) could be either directed or indirected
# Breadth First Search is using queue
from queue import Queue, PriorityQueue
import graphutils


class Arc:
    # TODO: Implement arc class
    def __init__(self, weigth, initial_node, final_node):
        assert weigth > 0, "Weigth must be greather than 0"
        self.weigth = weigth
        self.initial_node = initial_node
        self.final_node = final_node


class Node:
    # TODO: Implement node class
    def __init__(self, value):
        self.value = value


class Graph:
    # TODO: Implement graph
    def __init__(self, nodes, arcs):
        self.nodes = graphutils.init_edged_list(nodes, arcs)
        self.nodes_length = len(nodes)

    def deep_first_search(self, initial_node, callback):
        visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())

        def deep_first_search_alg(initial_node, callback):
            if visited_nodes[initial_node.value] == True:
                return
            callback(initial_node.value)
            visited_nodes[initial_node.value] = True
            neighboors = self.nodes[initial_node.value]

            for neighboor in neighboors:
                deep_first_search_alg(neighboor[0], callback)

        deep_first_search_alg(initial_node, callback)

    def breadth_first_search(self, initial_node, goal_node=None):
        visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())
        queue = Queue(self.nodes_length)
        queue.put(initial_node)
        visited_nodes[initial_node.value] = True
        graph_nodes = []

        while not queue.empty():
            front = queue.get()
            neighboors = self.nodes[front.value]

            for neighboor in neighboors:
                if visited_nodes[neighboor[0].value] == False:
                    graph_nodes.append(neighboor[0])
                    visited_nodes[neighboor[0].value] = True
                    queue.put(neighboor[0])

                    if goal_node is not None and neighboor[0].value == goal_node.value:
                        return graph_nodes

        return graph_nodes

    def dijkstra(self, initial_node):
        visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())
        previous = graphutils.init_visited_nodes(self.nodes.keys())

        # Dijkstra distance
        distance = {}
        for node in self.nodes.keys():
            distance[node] = 1e1000

        distance[initial_node.value] = 0
        queue = Queue()
        queue.put((initial_node, 0))

        while not queue.empty():
            current_node = queue.get()
            visited_nodes[current_node[0].value] = True
            for neighboor in self.neighboors(current_node[0]):
                if visited_nodes[neighboor[0].value] == True:
                    continue
                new_distance = distance[current_node[0].value] + neighboor[1]
                if new_distance < distance[neighboor[0].value]:
                    previous[neighboor[0].value] = current_node
                    distance[neighboor[0].value] = new_distance
                    queue.put((neighboor[0], new_distance))

        return {'distance': distance, 'previous': previous}

    def find_path(self, initial_node, final_node):
        dijkstra = self.dijkstra(initial_node)
        print(dijkstra)
        path = []

        if (dijkstra.get('previous')[final_node.value] != False):
            queue = Queue()
            queue.put(dijkstra.get('previous')[final_node.value])
            while not queue.empty():
                current = queue.get()
                print(current[0].value)
                if current != False:
                    path.append(current)
                    queue.put(dijkstra.get('previous')[current[0].value])
        return path



    # this is awesome to search smallest path in an unweigthed graph

    def neighboors(self, node):
        return self.nodes[node.value]
