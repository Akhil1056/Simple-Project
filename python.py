#this is a another new comment added in github and now in the git offline also
#another test now
# coding: utf-8

# In[133]:

import networkx as nx
import random
print('test1')
import matplotlib.pyplot as plt
print('test2')
import scipy as sp
import numpy
from itertools import permutations
G = nx.scale_free_graph(100)
pos=nx.spring_layout(G) # positions for all nodes
l=[]
# n = int(eval(input("Enter the numer of node : ")))
n=5
deg=0
if n <=30:
    deg=3.3
elif n>30 and n<=80:
    deg=3.9
elif n>80 and n<=100:
    deg=4
labels=(1,n)


nv=1/n
G = nx.gnp_random_graph(n,0.4,random.randint(1,100))
print("Nodes of graph: ")
print((G.nodes()))
print("Edges of graph: ")
print((G.edges()))
nx.draw(G, with_labels = True)
plt.savefig("path_graph1.png")

plt.show()



# In[165]:

a = nx.adjacency_matrix(G)
conn_mat=a.todense().tolist()
hop_mat=a.todense().tolist()
new_mat=numpy.zeros(shape=(n+1,n+1)).tolist()
print(a.todense())
r , c = a.shape
D = numpy.sum(a)
maxD = numpy.max(a)
MN = maxD.shape
for i in range(n):
    for j in range(n):
        if conn_mat[i][j]==1:
            for k in range(n):
                if conn_mat[j][k]==1 and j!=k and i!=j and i!=k:
                    hop_mat[i][k]=1
new2=numpy.array(hop_mat)
print('1 hop_mat')
print(new2)
#hop_mat.todense().tolist()

counter=0

for i in range(n):
    if hop_mat[0][i]==1:
        counter+=1
        sch_mat = numpy.zeros(shape=(counter,n),dtype=int).tolist()

counter=n
sch_mat = numpy.zeros(shape=(counter,n),dtype=int).tolist()
# print(sch_mat)        


sch_mat[0][0]=1
m=[]
for i in range(counter):
    for j in range(n):
        if i==j:
            sch_mat[i][j]=1
            pass
# print(sch_mat)       
talked=[]
talked_in_any_round=[]
for i in range(counter):
    talked_in_any_round.extend(talked)
    talked=[]
    for j in range(n):
#         print('checking ' + str(i) + str(j) + "  ; input:   "  + str(talked))
        if j in talked_in_any_round:
            sch_mat[i][j]=0
            continue
        if hop_mat[i][j]==1: # and j not in talked:
#             print((i,j,'nope'))
            sch_mat[i][j]=0
            continue
            
        if hop_mat[i][j]==0:
#             print('talked: ' + str(i) + str(j))
#             print('no direct 1 hop')
#             print(talked)
            for node in talked:
#                 print('checking indirect : ' + str(talked) + str(node))
#                 print(node,j, hop_mat[node][j])
                if hop_mat[node][j]==1 and j!=node:
                    sch_mat[i][j]=0
#                     print('indirect hop')
                    break
            else:
#                 print('eligible ' + str(j))
                if j not in talked_in_any_round:
                    sch_mat[i][j]=1
                    talked.append(j)
                    print(talked)
                    
#                 break
#             talked.append(j)
#     talked.append(j)
            
# print(type(sch_mat))
# print(sch_mat)
new3=numpy.array(sch_mat)
sch_mat = new3[~numpy.all(new3 == 0, axis=1)]

print('scheduler matrix')

print( sch_mat)


# TwoHopMat_1 = numpy.logical_xor(TwoHopMat_1,numpy.diag(MN,1))

nodes_not_talked = [n for n in range(n)]
nodes_talked=[]

# print(nodes_not_talked)

for node in nodes_not_talked:
    nodes_talked.append(node)
    for other_node in nodes_not_talked:
        # if other_node 
        pass
    
print(numpy.random.shuffle(new3[~numpy.all(new3 == 0, axis=1)]))
# In[159]:
def permutation(lst):
 
    # If lst is empty then there are no permutations





    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    j=1
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
           j+=1
           if(j>3):
               break
    return l
 
 
# Driver program to test above function
print("length of sch mat:",len(sch_mat))
temp = []
for i in range (0,len(sch_mat)):
    temp.append(str(i))
data = temp
l = permutation(data)
print(len(l))
full_mat = []
temp = []
for row in l:
    #print(row)
    temp = []
    for col in row:
        index = int(col)
        #print(index)
        temp.append(sch_mat[index].tolist())
    print(numpy.array(temp))
   



    
