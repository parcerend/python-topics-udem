class Visualize:
    def __init__(self, max_level):
        self.max_level = max_level

    def visualize(self, level, *args, **nargs):
        if level < self.max_level:
            print(*args, *nargs)


class Search(Visualize):
    def __init__(self, problem):
        self.problem = problem
        self.initialize_border()

    def initialize_border(self):
        self.border = []

    def empty_border(self):
        return len(self.border) == 0

    def add_border(self, path):
        self.border.append(path)
    
    def search(self):
      while not self.empty_border():
        path = self.border.pop()
        self.visualize(3, "Expand: ", path, f"Weight {10}")
        self.expand_num += 1
        break

