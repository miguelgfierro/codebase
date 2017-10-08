#source: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html


class Graph(object):
    """ Graphs are structures used to model pairwise relations between objects. A graph is made up of vertices, nodes,
    or points which are connected by edges, arcs, or lines. A graph may be undirected, when there is no distinction
    between the two vertices associated with each edge, or its edges may be directed from one vertex to another.
    Edges may be weighted to show that there is a cost to go from one vertex to another
    Examples:
        >>> g = Graph()
        >>> for i in range(3):
        ...     v = g.add_vertex(i)
        >>> g.add_edge(0,1,5)
        >>> g.add_edge(0,5,2)
        >>> g.add_edge(1,2,4)
        >>> g.add_edge(2,3,9)
        >>> for v in g:
        ...    for w in v.get_connections():
        ...        print("( %s , %s )" % (v.getId(), w.getId()))
        ( 0 , 1 )
        ( 0 , 5 )
        ( 1 , 2 )
        ( 2 , 3 )

    """
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self,key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self,n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None
        
    def get_vertices(self):
        return self.vert_list.keys()
    
    def __contains__(self,n):
        return n in self.vert_list

    def add_edge(self,f,t,cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def __iter__(self):
        return iter(self.vert_list.values())


class Vertex(object):
    """The vertex of a graph."""
    def __init__(self,key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self,nbr,weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected_to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self,nbr):
        return self.connected_to[nbr]

