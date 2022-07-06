import matplotlib.pyplot as plt


class Graph():
    """
    Инициализация графа
    Принимает на вход словарь, где ключами будут являться начальными вершины, а элементами этого ключа множество конечных вершин.
    Каждая вершина представляет собой кортеж (неизменяемый), например: ("a", "info_a"), где "a" название вершины, а "info_a" - какая-то информация, которую несет эта вершина.  
    """
    def __init__(self, graph_dict = None, directed = False):
        
        """
        Инициализация рандомного графа
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict
        self._directed = directed 

    def add_node(self, new_node, new_node_info):
        """
        Добавление узла в граф
        """
        if new_node not in self._graph_dict:
            self._graph_dict[(new_node, new_node_info)] = []
            
#     def edges(self, node, node_info):
#         """возвращает узлы, с которыми связана данная вершина, и её информация"""
#         return self._graph_dict[(node, node_info)]
    
#     def all_nodes(self):
#         """возвращает вершины графа и их информацию"""
#         return set(self._graph_dict.keys())
    
    
# ---------------------------------------------------------------------------------------
         
class Plot_Graph():
    
    """Отрисовка графа с помощью maptplotlib"""
    def __init__():
        """visual is a list which stores all the set of edges that constitutes a graph"""
        self.visual = []
        pass
    
    def display(self):
        pass
    

    
    

    
    
    