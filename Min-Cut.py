import random
import copy

minimum_list = []

graph = {}

def load_data():
    graph = {}
    f = open('./p3-matrix.txt', 'r')
    lines = f.readlines()
    n = len(lines)
    count = 0
    for line in lines:
        if (count % 2 == 0):
            ids = [int(id) for id in line.split()]
            graph[count/2] = []
            for id in range(len(ids)):
                if ids[id] == 1:
                    graph[count/2].extend([id,])
            count += 1
        else:
            count += 1
    return graph




def karger(graph):

    deleted_nodes = []
    temp_list = []
    
    while(len(graph) > 2):
        
        v = random.choice(list(graph.keys()))
        w = random.choice(graph[v])

        if w not in graph.keys():
            for i in graph[v]:
                temp_list.append(i)
            for j in temp_list:
                if j in deleted_nodes:
                    temp_list = filter(lambda a: a != j, temp_list)
            w = random.choice(temp_list)

        while (v == w):
            v = random.choice(list(graph.keys()))
            for i in graph[v]:
                temp_list.append(i)
            for j in temp_list:
                if j in deleted_nodes:
                    temp_list = filter(lambda a: a != j, temp_list)
            w = random.choice(temp_list)

        deleted_nodes.append(w)


        #print(v,w)
        #print(deleted_nodes)
        #print(temp_list)

        for node in graph[w]:
            if node != v:
                graph[v].append(node)
        for node1 in graph[w]:
            if node1 in graph.keys():
                if w in graph[node1]:
                    graph[node1].remove(w)
                if node1 != v:
                    graph[node1].append(v)
        del graph[w]

    minimum_cut = len(graph[list(graph.keys())[0]])
    minimum_list.append(minimum_cut)


graph2 = load_data()
count = 10000
i = 0

while i < count:
    graph1 = copy.deepcopy(graph2)
    karger(graph1)
    i += 1
    

print(min(minimum_list))


#10 runs
#trial 1 min-cut: 27
#trial 2 min-cut: 27
#trial 3 min-cut: 28
#trial 4 min-cut: 25
#trial 5 min-cut: 25
#trial 6 min-cut: 27
#trial 7 min-cut: 26
#trial 8 min-cut: 33
#trial 9 min-cut: 25
#trial 10 min-cut: 28

#20 runs
#trial 1 min-cut: 26
#trial 2 min-cut: 26
#trial 3 min-cut: 26
#trial 4 min-cut: 25
#trial 5 min-cut: 25
#trial 6 min-cut: 26
#trial 7 min-cut: 25
#trial 8 min-cut: 26
#trial 9 min-cut: 25
#trial 10 min-cut: 24


#30 runs
#trial 1 min-cut: 25
#trial 2 min-cut: 25
#trial 3 min-cut: 25
#trial 4 min-cut: 27 
#trial 5 min-cut: 25
#trial 6 min-cut: 25
#trial 7 min-cut: 26
#trial 8 min-cut: 25
#trial 9 min-cut: 26
#trial 10 min-cut: 25


#50 runs
#trial 1 min-cut: 26
#trial 2 min-cut: 26
#trial 3 min-cut: 26
#trial 4 min-cut: 25
#trial 5 min-cut: 25
#trial 6 min-cut: 26
#trial 7 min-cut: 25
#trial 8 min-cut: 25
#trial 9 min-cut: 25
#trial 10 min-cut: 25


#100 runs
#trial 1 min-cut: 23
#trial 2 min-cut: 25
#trial 3 min-cut: 25
#trial 4 min-cut: 24
#trial 5 min-cut: 25
#trial 6 min-cut: 26
#trial 7 min-cut: 25
#trial 8 min-cut: 25
#trial 9 min-cut: 25
#trial 10 min-cut: 26



#10000 runs
#trial 1 min-cut: 22
#trial 2 min-cut: 22
#trial 3 min-cut: 21
#trial 4 min-cut: 22
#trial 5 min-cut: 22
