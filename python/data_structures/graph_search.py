from .graph import Graph, Vertex
from .queue import Queue
from .stack import Stack


def breadth_first_search_paths(graph, start, goal):
    """Breadth-first search (BFS) is an algorithm for searching a path from
    start to goal in graph data structures. It starts at the tree root and
    explores the neighbor nodes first, before moving to the next level
    neighbours.
    Args:
        graph (Graph): A graph.
        start (key): The key of the initial vertex
        goal (key): The key of the goal vertex
    Examples:
        >>> g = Graph()
        >>> for v in ['1', '2', '4', '7', '3']:
        ...     _ = g.add_vertex(v)
        >>> g.add_edge('1','2')
        >>> g.add_edge('1','3')
        >>> g.add_edge('1','4')
        >>> g.add_edge('2','5')
        >>> g.add_edge('2','6')
        >>> g.add_edge('4','7')
        >>> g.add_edge('4','8')
        >>> g.add_edge('7','11')
        >>> g.add_edge('7','12')
        >>> g.add_edge('3','11')
        >>> path = breadth_first_search_paths(g, '1', '11')
        >>> [node.get_id() for node in path]
        ['1', '3', '11']
        >>> path = breadth_first_search_paths(g, '1', '12')
        >>> [node.get_id() for node in path]
        ['1', '4', '7', '12']

    """
    v_start = graph.get_vertex(start)
    v_goal = graph.get_vertex(goal)
    queue = Queue()
    queue.enqueue([v_start])
    while not queue.is_empty():
        path = queue.dequeue()
        last_node = path[-1]
        # path found
        if last_node.get_id() == v_goal.get_id():
            return path
        for adjacent in last_node.get_connections():
            new_path = list(path)
            new_path.append(adjacent)
            queue.enqueue(new_path)


def depth_first_search_paths(graph, start, goal):
    """Depth First Search is an algorithm for for searching a path from start
    to goal in graphs data structures. It starts at the root and explores as
    far as possible along each branch before backtracking.
    Args:
        graph (Graph): A graph.
        start (Vertex): The start vertex
        goal (Vertex): The goal vertex
    Examples:
        >>> g = Graph()
        >>> for v in ['1', '2', '4', '7', '3']:
        ...     _ = g.add_vertex(v)
        >>> g.add_edge('1','2')
        >>> g.add_edge('1','3')
        >>> g.add_edge('1','4')
        >>> g.add_edge('2','5')
        >>> g.add_edge('2','6')
        >>> g.add_edge('4','7')
        >>> g.add_edge('4','8')
        >>> g.add_edge('7','11')
        >>> g.add_edge('7','12')
        >>> g.add_edge('3','11')
        >>> path = depth_first_search_paths(g, '1', '11')
        >>> [node.get_id() for node in path]
        ['1', '4', '7', '11']
        >>> path = depth_first_search_paths(g, '1', '12')
        >>> [node.get_id() for node in path]
        ['1', '4', '7', '12']
    """
    v_start = graph.get_vertex(start)
    v_goal = graph.get_vertex(goal)
    stack = Stack()
    stack.push([v_start])
    while not stack.is_empty():
        path = stack.pop()
        last_node = path[-1]
        # path found
        if last_node.get_id() == v_goal.get_id():
            return path
        for adjacent in last_node.get_connections():
            new_path = list(path)
            new_path.append(adjacent)
            stack.push(new_path)
