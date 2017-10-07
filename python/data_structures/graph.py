#source: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html


class Graph(object):
    """ Graphs are structures used to model pairwise relations between objects. A graph is made up of vertices, nodes,
    or points which are connected by edges, arcs, or lines. A graph may be undirected, when there is no distinction
    between the two vertices associated with each edge, or its edges may be directed from one vertex to another.
    Edges may be weighted to show that there is a cost to go from one vertex to another
    Examples:
        >>> g = Graph()
        >>> for i in range(3):
        ...     v = g.addVertex(i)
        >>> g.addEdge(0,1,5)
        >>> g.addEdge(0,5,2)
        >>> g.addEdge(1,2,4)
        >>> g.addEdge(2,3,9)
        >>> for v in g:
        ...    for w in v.getConnections():
        ...        print("( %s , %s )" % (v.getId(), w.getId()))
        ( 0 , 1 )
        ( 0 , 5 )
        ( 1 , 2 )
        ( 2 , 3 )

    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class Vertex(object):
    """The vertex of a graph."""
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

