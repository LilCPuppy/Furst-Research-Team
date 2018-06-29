from sys import *
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt 


class FurstGraph:


    def __init__(self, adj_mat=np.array([])):

        self.myGraph = None
        self.eigenvals = None
        if adj_mat.any():
            self.myGraph = nx.from_numpy_matrix(adj_mat)



    def get_spectrum(self):

        self.eigenvals = nx.laplacian_spectrum(self.myGraph)
        return self.eigenvals


    def std_plot(self):

        print('Eigenvalues of the Laplacian\n')
        print(self.eigenvals)
        nx.draw(self.myGraph)
        plt.show()



adj = np.ones((5,5))
for i in range(5):
    adj[i][i] = 0
our_graph = FurstGraph(adj)

our_graph.get_spectrum()


our_graph.std_plot()


