class Network:
    def __init__(self,file):
        self.net={}
        self.file_name=file
        self.readNet()
        #self.readNetwokGml()


    def readNet(self):
        f = open(self.file_name, "r")
        n = int(f.readline())
        self.net['noNodes'] = n
        mat = []
        for i in range(n):
            mat.append([])
            line = f.readline()
            elems = line.split(",")
            for j in range(n):
                mat[-1].append(int(elems[j]))
        self.net["mat"] = mat
        degrees = []
        noEdges = 0
        for i in range(n):
            d = 0
            for j in range(n):
                if (mat[i][j] == 1):
                    d += 1
                if (j > i):
                    noEdges += mat[i][j]
            degrees.append(d)
        self.net["noEdges"] = noEdges
        self.net["degrees"] = degrees
        f.close()

    # def readNetwokGml(self):
    #     graph=nx.readwrite.read_gml(self.file_name,label = 'id')
    #     self.net['graph']=graph
    #     print(" ")
    #     self.net['noNodes']=len(graph.nodes)
    #     self.net['noEdges']=len(graph.edges)
    #     degrees=[]
    #     for node in graph.degree:
    #         degrees.append(node[1])
    #     self.net['degrees']=degrees
    #     mat=[]
    #     for edge in graph.adj:
    #         vecini=graph.adj[edge]
    #         #inod=graph.nodes.index(edge)
    #         adiac=[0]*self.net['noNodes']
    #         i=0
    #         for vec in vecini:
    #             jnod=(list(graph.nodes())).index(vec)
    #             adiac[jnod]=1
    #         mat.append(adiac)
    #     self.net['mat']=mat
    #     self.net['fN']=list(graph.nodes.keys())[0]
    #     self.net['lN']=list(graph.nodes.keys())[-1]
    #
    # def getNodeNumber(self,node):
    #     return self.net['graph'].nodes().index(node)
    #
    # def getNodeName(self,nr):
    #     return self.net['graph'].nodes[nr]
    #
    #
    # def getNetworkPlot(self):
    #     warnings.simplefilter('ignore')
    #     A=np.matrix(self.net["mat"])
    #     G=nx.from_numpy_matrix(A)
    #     pos = nx.spring_layout(G)  # compute graph layout
    #     plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
    #     nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
    #     nx.draw_networkx_edges(G, pos, alpha=0.3)
    #     plt.show(G)
