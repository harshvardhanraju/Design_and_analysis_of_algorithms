"""
@Harsha
Date: 20/3/18
"""

import sys


def bfs(n, m, edges, s):
    # Complete this function
    adj_dict = {}
    result = []
    for node in range(n):
        adj_dict[node + 1] = []
    for connection in edges:
        adj_dict[connection[0]].append(connection[1])
        adj_dict[connection[1]].append(connection[0])
    # print (adj_dict)
    for node in range(n):
        connect = False
        new_start = s
        for it in range(len(adj_dict[s]) + 1):  # max iterations = of elms in the adjacency list of 's'
            if node + 1 == s:
                break
            if node + 1 in adj_dict[new_start]:
                connect = True
                break
            elif it == len(adj_dict[s]):
                connect = False
                break
            elif node + 1 not in adj_dict[new_start]:
                new_start = adj_dict[s][it]
        print(node + 1, connect, adj_dict[new_start])
        if connect is True:
            dist = (it + 1) * 6
        if connect is not True:
            dist = -1
        if node + 1 != s:
            result.append(dist)
    return result


if __name__ == "__main__":
    q = 1
    for a0 in range(q):
        n, m = 3, 1
        n, m = [int(n), int(m)]
        edges = []
        # for edges_i in range(m):
        #   edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
        #   edges.append(edges_t)
        edges = [[2, 3]]
        s = 2
        result = bfs(n, m, edges, s)
        print (" ".join(map(str, result)))
