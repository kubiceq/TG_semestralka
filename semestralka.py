try:
  import networkx as nx
except ImportError:
  print ("Trying to Install required module: networkx\n")
  os.system('python -m pip install networkx')
try:
  import numpy as np
except ImportError:
  print ("Trying to Install required module: numpy\n")
  os.system('python -m pip install numpy')
try:
  import matplotlib.pyplot as plt
except ImportError:
  print ("Trying to Install required module: matplotlib\n")
  os.system('python -m pip install -U matplotlib')


#legenda
#???????????????????????????????? -> zadaj tvoje hodnoty
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -> odkomentuj pre grafy
# pre odkomentovanie bloku textu oznac a stlac 'Ctrl' + '/'





COLOR = "tab:blue"
i=0
print('#*********************************************Uloha_1**********************************************************************************')
#definuj graf
Graf_z_ulohy_1 = nx.Graph()
# navod:
# https://youtu.be/7fujbpJ0LB4?t=69

#matica susednosti
#????????????????????????????????????????????????????????????????????
matica_susednosti = np.array([[0,0,0,0,1,0,0,0],
                              [0,0,0,1,0,1,0,0],
                              [1,0,0,0,0,1,0,1],
                              [0,0,0,0,0,0,0,1],
                              [0,0,1,1,0,0,0,1],
                              [0,0,0,1,0,0,1,1,],
                              [0,1,0,1,1,0,0,0],
                              [1,0,0,0,0,0,0,0]])
#????????????????????????????????????????????????????????????????????
#vytvorenie grafu z matice susednosti
Graf_z_ulohy_1 = nx.from_numpy_matrix(matica_susednosti)
#nakresli graf z ulohy 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#i+=1
#plt.figure(i)
#plt.title('Graf z ulohy 1')
#nx.draw(Graf_z_ulohy_1, with_labels=True, font_weight='bold')
#plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#prehladaj do hlbky
print("Stromy pri prehladani do hlbky")
for vrchol in range(Graf_z_ulohy_1.order()):
    Strom_hlbky = nx.dfs_tree(Graf_z_ulohy_1, source=vrchol)
    print(list(Strom_hlbky.edges()))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   i+=1
#   plt.figure(vrchol+i)
#   string = 'Strom do hlbky pre vrchol:' + str(vrchol)
#   plt.title(string)
#   nx.draw(Strom_hlbky, with_labels=True)
#plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#prehladaj do sirky
print("Stromy pri prehladani do sirky")
for vrchol in range(Graf_z_ulohy_1.order()):
    Strom_sirky = nx.bfs_tree(Graf_z_ulohy_1, source=vrchol)
    print(list(Strom_sirky.edges()))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     i+=1
#     plt.figure(vrchol+i)
#     string = 'Strom do sirky pre vrchol:' + str(vrchol)
#     plt.title(string)
#     nx.draw(Strom_sirky, with_labels=True)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('#*********************************************Uloha_2**********************************************************************************')
#navod:
# https://blog.devgenius.io/floyd-warshall-all-pairs-shortest-path-matrix-multiplication-1ae24f3312e4
# Pocet vrcholov, ktore dosiahnem dnes v noci
#????????????????????????????????????????????????????????????????????
nV = 6
#????????????????????????????????????????????????????????????????????
INF = 9999

# Algorithm
def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        sol(dist)
        print('**********************************************************************')
# Printing the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")
#Cenova Matica
#????????????????????????????????????????????????????????????????????
G =      [[0, 3, 1, 5, INF, INF],
         [3, 0, 4, INF, INF, 2],
         [1, 4, 0, INF, 7, INF],
         [5, INF, INF, 0, 3, INF],
         [INF, INF, 7, 3, 0, 5 ],
         [INF, 2, INF, INF, 5, 0]]
#????????????????????????????????????????????????????????????????????
#matica z navodu
#navod:
# https://blog.devgenius.io/floyd-warshall-all-pairs-shortest-path-matrix-multiplication-1ae24f3312e4
# G =      [[0,10,INF,5],
#          [INF,0,INF,9],
#          [-2,4,0,INF],
#          [INF,-3,1,0]]
floyd(G)

print('#*********************************************Uloha_3**********************************************************************************')
from networkx.algorithms import tree
from networkx.drawing.nx_pydot import graphviz_layout
Graf_z_ulohy_3 = nx.Graph()
# navod:
# https://www.youtube.com/watch?v=71UQH7Pr9kU
# pekne vysvetlenie je aj na wiki
# https://sk.wikipedia.org/wiki/Minimálna_kostra_grafu


#definuj hrany
#????????????????????????????????????????????????????????????????????
Graf_z_ulohy_3.add_edge("1","2", weight = 6)
Graf_z_ulohy_3.add_edge("1","3", weight = 5)
Graf_z_ulohy_3.add_edge("1","4", weight = 1)
Graf_z_ulohy_3.add_edge("2","4", weight = 4)
Graf_z_ulohy_3.add_edge("2","5", weight = 7)
Graf_z_ulohy_3.add_edge("2","7", weight = 2)
Graf_z_ulohy_3.add_edge("3","4", weight = 2)
Graf_z_ulohy_3.add_edge("3","6", weight = 8)
Graf_z_ulohy_3.add_edge("3","8", weight = 1)
Graf_z_ulohy_3.add_edge("4","5", weight = 11)
Graf_z_ulohy_3.add_edge("4","6", weight = 10)
Graf_z_ulohy_3.add_edge("4","7", weight = 9)
Graf_z_ulohy_3.add_edge("5","8", weight = 3)
Graf_z_ulohy_3.add_edge("6","7", weight = 3)
Graf_z_ulohy_3.add_edge("7","8", weight = 5)
#????????????????????????????????????????????????????????????????????

#nakresli graf 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Graf 3')
# pos=nx.spring_layout(Graf_z_ulohy_3) # pos = nx.nx_agraph.graphviz_layout(Graf_z_ulohy_3)
# nx.draw_networkx(Graf_z_ulohy_3,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_3,'weight')
# nx.draw_networkx_edge_labels(Graf_z_ulohy_3,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#najdi minimalny strom grafu 3
print("minimalny strom / kostra: ")
minst = tree.minimum_spanning_edges(Graf_z_ulohy_3, algorithm='kruskal', data=False)
edgelist = list(minst)
print(sorted(edgelist))



#vykresli minimalny strom grafu 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Tmin = nx.Graph();
#Tmin.add_edges_from(edgelist)
#i+=1
#plt.figure(i)
#plt.title('Minimalna kostra grafu 3')
#nx.draw(Tmin, with_labels=True)
#plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#vykresli minimalny strom V grafe 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Graf 3')
# pos=nx.spring_layout(Minimalny strom v grafe 3)
# nx.draw_networkx(Graf_z_ulohy_3,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_3,'weight')
# nx.draw_networkx_edges(Graf_z_ulohy_3,pos,edgelist=edgelist,edge_color= COLOR,width=4)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_3,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#najdi maximalny strom
print("maximalny strom / kostra: ")
maxst = tree.maximum_spanning_edges(Graf_z_ulohy_3, algorithm='kruskal', data=False)
edgelist = list(maxst)
print(sorted(edgelist))

#vykresli maximalny strom
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Tmax = nx.Graph();
#Tmax.add_edges_from(edgelist)
#i+=1
#plt.figure(i)
#plt.title('Maximalna kostra grafu 3')
#nx.draw(Tmax, with_labels=True)
#plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#vykresli maximalny strom V grafe 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Maximalny strom v grafe 3')
# pos=nx.spring_layout(Graf_z_ulohy_3)
# nx.draw_networkx(Graf_z_ulohy_3,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_3,'weight')
# nx.draw_networkx_edges(Graf_z_ulohy_3,pos,edgelist=edgelist,edge_color= COLOR,width=4)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_3,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



print('#*********************************************Uloha_4**********************************************************************************')
Graf_z_ulohy_4 = nx.DiGraph()

#definuj hrany
#z - zdroj
#u - ustie
# navod:
# https://www.youtube.com/watch?v=Tl90tNtKvxs
#????????????????????????????????????????????????????????????????????
Graf_z_ulohy_4.add_edge("z","1", capacity = 14)
Graf_z_ulohy_4.add_edge("z","2", capacity = 15)
Graf_z_ulohy_4.add_edge("z","3", capacity = 13)
Graf_z_ulohy_4.add_edge("1","2", capacity = 6)
Graf_z_ulohy_4.add_edge("1","4", capacity = 4)
Graf_z_ulohy_4.add_edge("1","5", capacity = 8)
Graf_z_ulohy_4.add_edge("2","5", capacity = 4)
Graf_z_ulohy_4.add_edge("2","3", capacity = 3)
Graf_z_ulohy_4.add_edge("2","u", capacity = 10)
Graf_z_ulohy_4.add_edge("3","6", capacity = 8)
Graf_z_ulohy_4.add_edge("4","u", capacity = 9)
Graf_z_ulohy_4.add_edge("5","4", capacity = 7)
Graf_z_ulohy_4.add_edge("6","2", capacity = 9)
Graf_z_ulohy_4.add_edge("6","u", capacity = 11)
#????????????????????????????????????????????????????????????????????

#vykresli Graf 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Graf 4')
# pos=nx.spring_layout(Graf_z_ulohy_4) # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(Graf_z_ulohy_4,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_4,'capacity')
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
kapacita, flow_dict = nx.maximum_flow(Graf_z_ulohy_4,"z","u")
print("Maximalny tok:",flow_dict)
print('Kapacita maximalneho toku: ',kapacita)




#vykresli maximalny tok v grafe 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# edgelist = []
# edgeLabels = {}
# for vrchol in flow_dict:
#     #print(flow_dict[vrchol])
#     for protiVrchol in flow_dict[vrchol]:
#         edgelist.append([vrchol,protiVrchol])
#         edgeLabels[(vrchol,protiVrchol)] = flow_dict[vrchol][protiVrchol]
# i+=1
# plt.figure(i)
# plt.title('Graf 4')
# pos=nx.spring_layout(Graf_z_ulohy_4) # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(Graf_z_ulohy_4,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_4,'capacity')
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
#
# i+=1
# plt.figure(i)
# plt.title('Graf 4 s maximalnou kapacitou toku')
# nx.draw_networkx(Graf_z_ulohy_4,pos)
# labels = edgeLabels
# nx.draw_networkx_edges(Graf_z_ulohy_4,pos,edgelist=edgelist,edge_color= COLOR,width=2)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kapacita, flow_dict = nx.minimum_cut(Graf_z_ulohy_4,"z","u")
print("Minimalmy rez:",flow_dict)
print('Kapacita minimalneho rezu: ',kapacita)

#vykresli rozdelenie vrcholov
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# color_map = list(Graf_z_ulohy_4)
# edgelist = []
# pom = 0
# for skupina in flow_dict:
#     pom+=1
#     if pom == 1:
#         for vrchol in skupina:
#             index = list(Graf_z_ulohy_4).index(vrchol)
#             color_map[index] = 'blue'
#             print(index)
#     if pom == 2:
#         for vrchol in skupina:
#             index = list(Graf_z_ulohy_4).index(vrchol)
#             color_map[index] = 'red'
#             print(index)
# nx.draw(Graf_z_ulohy_4,node_color = color_map, with_labels=True)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#by kubqo, FLO, LJ