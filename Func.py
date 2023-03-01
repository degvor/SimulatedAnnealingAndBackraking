import random
import math
import networkx as nx
import matplotlib.pyplot as plt


class General:
    def __init__(self):
        self.GRAPH = [
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
        self.EDGES = ["red", "blue", "yellow", "green", "silver", "gray", "maroon", "olive", "lime", "aqua",
                      "teal", "navy", "fuchsia", "purple", "indianred", "khaki", "salmon", "peachpuff", "lightyellow",
                      "chocolate", "firebrick", "azure", "coral", "orange", "tan"]
        self.COLORS = ["red", "blue", "yellow", "green"]
        self.POSITION = {1: (600, 550), 2: (346, 281), 3: (196, 94), 4: (608, 310), 5: (747, 314), 6: (348, 144), 7: (101, 302),
               8: (668, 387), 9: (175, 289),
               10: (442, 188), 11: (487, 307), 12: (800, 228), 13: (150, 215), 14: (486, 383), 15: (421, 421),
               16: (560, 210), 17: (276, 122), 18: (565, 104),
               19: (228, 234), 20: (665, 200), 21: (560, 430), 22: (285, 235), 23: (450, 250), 24: (237, 332),
               25: (490, 84)}
        self.Start_edge = self.Edge = 0
        self.Result = None

        self.Number_of_iterations = 0
        self.Number_of_conditions = 0
        self.Number_of_dead_ends = 0
        return

    def drow_graph(self, edges):
        Graph = nx.Graph()
        plt.gca().invert_yaxis()
        Graph.add_nodes_from(self.POSITION.keys())
        for i in range(len(self.GRAPH)):
            for j in range(i):
                if self.GRAPH[i][j]:
                    Graph.add_edge(i + 1, j + 1)
        for n, p in self.POSITION.items():
            Graph.nodes[n]['pos'] = p
        nx.draw(Graph, node_color=edges, with_labels=True, pos=self.POSITION)
        plt.show()
        return

    def set_random_Start_edge(self):
        self.Start_edge = self.Edge = random.randint(0, len(self.GRAPH) - 1)
        return self.Start_edge

    def set_Start_edge(self, edge):
        self.Start_edge = self.Edge = edge
        return self.Start_edge

    def number_of_colors(self, edges):
        colors = []
        for i in edges:
            if not i in colors:
                colors += [i]
        return len(colors)

class Algorithm_Simmulated_Annealing(General):
    def __init__(self):
        super().__init__()
        random.shuffle(self.EDGES)
        return

    def check(self, index, edges, color):
        for i in range(len(self.GRAPH[index])):
            self.Number_of_iterations += 1
            if self.GRAPH[index][i] == 1:
                if color == edges[i]:
                    return False
        return True

    def sim_anneal(self):
        edges = self.EDGES.copy()
        temperature = 1000
        flags = [True for i in range(len(edges))]
        iteration = 0
        number_of_colors = []
        solution = None
        while temperature > 0:
            self.Number_of_iterations += 1
            if flags[self.Edge]:
                self.Number_of_conditions += 1
                for color in self.COLORS:
                    self.Number_of_iterations += 1
                    if self.check(self.Edge, edges, color):
                        edges[self.Edge] = color
                        flags[self.Edge] = False
                        break
            colors = []
            for color in self.COLORS:
                if self.check(self.Edge, edges, color):
                    colors += [color]
            if len(colors) > 0:
                flag = True
                for i in colors:
                    self.Number_of_iterations += 1
                    temp = edges.copy()
                    temp[self.Edge] = i
                    if self.number_of_colors(temp) < self.number_of_colors(edges):
                        edges[self.Edge] = i
                        flag = False
                        break
                if flag:
                    colour = random.choice(colors)
                    edges[self.Edge] = colour
            number_of_colors.append(self.number_of_colors(edges))
            if iteration > 0:
                color_diff = number_of_colors[iteration-1] - number_of_colors[iteration]
                if color_diff > 0:
                    solution = edges
                else:
                    if random.uniform(0, 1) < math.exp(-color_diff/temperature):
                        # self.Number_of_dead_ends += 1
                        solution = edges
            iteration += 1
            self.set_random_Start_edge()
            temperature = 1000 - 0.1 * iteration
        return solution

    def start(self):
        self.Result = self.EDGES.copy()
        edges = self.sim_anneal()
        if self.number_of_colors(edges) > 1:
            self.Result = edges
            return self.Result
        else:
            raise Exception('No solution')


class Algorithm_Backtracking(General):
    def __init__(self):
        super().__init__()
        self.iteration = 0
        return

    def from_dict_to_list(self, result):
        res = []
        for i in range(len(self.GRAPH)):
            if i in result:
                res += [result[i]]
            else:
                for color in self.EDGES:
                    if not color in res:
                        res += [color]
                        break
        return res

    def calculate_start_graph(self):
        graph_degree = {}
        tmp = 0
        for i in range(len(self.GRAPH)):
            for j in range(len(self.GRAPH[i])):
                if self.GRAPH[i][j] == 1:
                    tmp += 1
            graph_degree[i] = tmp
            tmp = 0
        self.Start_edge = max(graph_degree, key=graph_degree.get) + 1

    def dgr(self, edges):
        numbers = {}
        for i in range(len(self.GRAPH)):
            self.Number_of_iterations += 1
            if not i in edges:
                numbers[i] = self.COLORS.copy()
                for j in range(len(self.GRAPH)):
                    self.Number_of_iterations += 1
                    if self.GRAPH[i][j]:
                        if j in edges:
                            if edges[j] in numbers[i]:
                                numbers[i].remove(edges[j])
        graph_degree = {}
        tmp = 0
        for i in range(len(self.GRAPH)):
            for j in range(len(self.GRAPH[i])):
                if self.GRAPH[i][j] == 1:
                    tmp += 1
            graph_degree[i] = tmp
            tmp = 0
        if self.iteration == 0:
            graph_degree.pop(self.Start_edge)
        if self.iteration >= 1:
            graph_degree.pop(self.Start_edge)
            for i in range(self.iteration):
                index = max(graph_degree, key=graph_degree.get)
                graph_degree.pop(index)
        if graph_degree:
            index = max(graph_degree, key=graph_degree.get)
            self.iteration += 1
        else:
            return -1, []
        return index, numbers[index]

    def Backtracking(self, edge, edges, colors):
        for i in colors:
            self.Number_of_iterations += 1
            self.Number_of_conditions += 1
            if len(edges) == len(self.GRAPH):
                self.Result = edges
                break
            edges[edge] = i
            edge, colours = self.dgr(edges)
            if edge == -1:
                self.Number_of_dead_ends += 1
                if len(self.Result) < len(edges):
                    self.Result = edges
                break
            edges = self.Backtracking(edge, edges, colours)
        return edges

    def start(self):
        self.Result = {}
        result = self.Backtracking(self.Start_edge, {}, self.COLORS.copy())
        self.Result = self.from_dict_to_list(result)
        return self.Result