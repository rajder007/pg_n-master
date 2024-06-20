import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Graph:

    def __init__(self, start_node, end_node) -> None:
        self.start_node = start_node
        self.end_node = end_node

    def generate_graph(self):
        G = nx.Graph()
        # Dodawanie wierzchołków
        G.add_node(1)
        G.add_nodes_from([2, 3, 5, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
        G.add_weighted_edges_from([(1,2,1),(1,3,1),(1,4,1), (2,5,1), (2,6,1), (3,6,1), (3,7,1), (4,7,1), (7,8,1), (7,9,1),
                                    (9,10,1), (9,13,1), (9,14,1), (5,11,1), (6,11,1), (6,12,1), (11,15,1), (11,16,1), 
                                    (12,16,1), (12,17,1), (16,19,1), (17,20,1), (19,22,1), (20,22,1), (13,18,1),
                                    (18,20,1),(18,21,1),(22,23,1)])

        pos = nx.spring_layout(G)
        nx.draw(G,pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        return G

    def a_star(self, graph, start, end):
        open_set = [(0, start)]  # Priorytetowa kolejka wierzchołków do odwiedzenia
        come_from = {}
        g_score = {node: float('inf') for node in graph.nodes()}  # Koszt dotarcia do wierzchołka
        g_score[start] = 0
        f_score = {node: float('inf') for node in graph.nodes()}  # Szacowany koszt do celu
        f_score[start] = self.heuristic(start, end)

        while open_set:
            open_set.sort(key=lambda x: x[0])
            current_cost, current_node = open_set.pop(0)

            if current_node == end:
                path = [current_node]
                while current_node in come_from:
                    current_node = come_from[current_node]
                    path.append(current_node)
                path.reverse()
                return path
                
            for neighbor in graph.neighbors(current_node):
                tentative_g_score = g_score[current_node] + graph[current_node][neighbor]['weight']
                if tentative_g_score < g_score[neighbor]:
                    come_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, end)
                    open_set.append((f_score[neighbor], neighbor))
        return None

    def heuristic(self, u, v):
        # Przykładowa heurystyka (np. odległość euklidesowa)
        return abs(u - v)

    def dijkstry(self):
        pass

    def bfs(self, graph, start, end):
        visited = set()
        queue = deque([(start, [start])])  # Kolejka wierzchołków do odwiedzenia, wraz z ich ścieżką

        while queue:
            node, path = queue.popleft()  # Pobierz wierzchołek i jego ścieżkę z kolejki
            if node == end:  # Jeśli znaleziono wierzchołek końcowy
                return path  # Zwróć ścieżkę
            if node not in visited:
                visited.add(node)  # Oznacz wierzchołek jako odwiedzony
                neighbors = graph.neighbors(node)  # Pobierz sąsiadów wierzchołka
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))  # Dodaj nieodwiedzonych sąsiadów do kolejki wraz z ich ścieżką

        return None

    def dfs(self):
        pass

    def Bellman_Ford(self, graph, start, end):
        
        distance = {node: float('inf') for node in graph.nodes()}
        predecessor = {}  # Słownik przechowujący poprzednie wierzchołki na najkrótszej ścieżce
        distance[start] = 0 

        # wykonywanie relaksacji krawędzi dla każdego wieszchołka
        for _ in range(len(graph.nodes()) - 1):
            for u, v, weight in graph.edges(data='weight'):
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

        # Sprawdzamy czy istnieje cykl o ujemnej wadze
        for u, v, weight in graph.edges(data='weight'):
            if distance[u] + weight < distance[v]:
                raise ValueError("graf zawiera ujemny cykl")
            
        # Odtwarzanie najkrótszej ścieżki od wierzchołka końcowego do początkowego
        path = [end]
        while path[-1] != start:
            path.append(predecessor[path[-1]])
        path.reverse()

        return distance[end], path    

    def Floyd_Warshalla(self):
        pass

# Przykład użycia
graph = Graph(1, 23)
g = graph.generate_graph()
path = graph.bfs(g, graph.start_node, graph.end_node)
print(path)
path_2 = graph.a_star(g, graph.start_node, graph.end_node)
print(path_2)
path_3 = graph.Bellman_Ford(g, graph.start_node, graph.end_node)
print(path_3)
