import pickle
import matplotlib.pyplot as plt
import networkx as nx
import igraph as ig
import scipy.sparse as sp
import numpy as np
import torch
import json
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

topo = json.load(open('./mri/topology.json'))
type(topo), topo.keys(), topo['links']

# get all the nodes
# hosts are represented as h* and switches as s*, where * is a number
# s1-p2 means port 2 of switch 1
# since all ports on the same switch are connected, we can ignore the port number
# each link are assumed to have the same capacity
def parse_topo(topo):
    G = nx.Graph()
    nodes = []
    for link in topo['links']:
        nodes.append(link[0].split('-')[0])
        nodes.append(link[1].split('-')[0])
    nodes = list(set(nodes))
    G.add_nodes_from(nodes)
    edges = []
    for link in topo['links']:
        edges.append((link[0].split('-')[0], link[1].split('-')[0]))
    return G

G = parse_topo(topo)
nx.draw(G, with_labels=True, font_weight='bold')