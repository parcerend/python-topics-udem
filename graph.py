from queue import Queue, PriorityQueue
from functools import reduce
import graphutils

class Arc:
    def __init__(self, weigth, initial_node, final_node):
        assert weigth > 0, "Weigth must be greather than 0"
        self.weigth = weigth
        self.initial_node = initial_node
        self.final_node = final_node


class Node:
    def __init__(self, value, heuristic=0):
        self.heuristic = heuristic
        self.value = value

    def __gt__(self, node):
        return self.value > node.value

class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = graphutils.init_edged_list(nodes, arcs)
        self.nodes_length = len(nodes)

    def a_star_search(self, initial_node, final):
        previos_visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())
        priority_queue = PriorityQueue()
        priority_queue.put((initial_node, initial_node.heuristic))

        graph_score = {}
        final_score = {}

        for node in self.nodes.keys():
            graph_score[node] = final_score[node] = 1e1000
        
        graph_score[initial_node.value] = 0
        final_score[initial_node.value] = initial_node.heuristic

        while not priority_queue.empty():
            current = priority_queue.get()

            if (current[0].value == final.value):
                break
            
            for neighboor in self.neighboors(current[0]):
                estimated_score = graph_score[current[0].value] + neighboor[1]

                if estimated_score < graph_score[neighboor[0].value]:
                    previos_visited_nodes[neighboor[0].value] = current
                    graph_score[neighboor[0].value] = estimated_score
                    final_score[neighboor[0].value] = graph_score[neighboor[0].value] + neighboor[0].heuristic

                    if not any((neighboor[0].heuristic, neighboor[0]) in nodes for nodes in priority_queue.queue):
                        priority_queue.put((neighboor[0], final_score[neighboor[0].value]))

        return {'distance': final_score, 'previous': previos_visited_nodes}

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

    def find_path(self, initial_node, final_node):
        search = self.a_star_search(initial_node, final_node)
        path = []

        if (search.get('previous')[final_node.value] == False):
            return {'path': path, 'distance': 10e2000}

        queue = Queue()
        queue.put(search.get('previous')[final_node.value])

        while not queue.empty():
            current = queue.get()
            if current is not False:
                path.append(current)
                queue.put(search.get('previous')[current[0].value])

        current_distance = reduce(lambda acumulated, current, : acumulated + current[1], path, 0)
        path.insert(0, (final_node, abs(search.get('distance')[final_node.value] - current_distance)))

        return {
            'path': list(reversed(path)),
            'distance': search.get('distance')[final_node.value]
        }

    def is_cyclic(self, initial_node):
        unvisited_nodes = graphutils.init_visited_nodes(self.nodes)
        unvisited_nodes[initial_node.value] = True
        queue = Queue()
        queue.put(initial_node)

        while not queue.empty():
            current = queue.get()
            unvisited_nodes[current.value] = True
            neighboors = self.neighboors(current)

            for neighboor in neighboors:
                if unvisited_nodes[neighboor[0].value] == True:
                    return True

                queue.put(neighboor[0])

        return False

    def is_bipartite(self, initial_node):
        unvisited_nodes = graphutils.init_visited_nodes(self.nodes)
        queue = Queue()
        queue.put(initial_node)

        while not queue.empty():
            current = queue.get()
            unvisited_nodes[current.value] = True

            for neighboor in self.neighboors(current):
                if not unvisited_nodes[neighboor[0].value]:
                    queue.put(neighboor[0])

        return len(list(filter(lambda visited: not visited, unvisited_nodes.values()))) >= 1

    def iterative_search(self, initial_node, goal_node, depth):
        def limited_search(root, final_node, limit):
            if (root.value == final_node.value):
                return True

            if (limit <= 0):
                return False

            for neighboor in self.neighboors(root):
                if limited_search(neighboor[0], final_node, limit - 1):
                    return True
                return False

        for i in range(depth):
            if limited_search(initial_node, goal_node, i):
                return True
        return False

    def neighboors(self, node):
        return self.nodes[node.value]
