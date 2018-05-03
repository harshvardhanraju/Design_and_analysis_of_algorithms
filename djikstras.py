'''
@Harsha
Date : 17/4/18
Dijsktra's shortest path algo
'''

source_dist = []  # inf at start and update with shortest paths
adj_dict = {}
processed_list = []  # when this is size of tree, stop iterations


def relax_adj(cur_node):
    '''
    '''
    pass


def djikstra_one_node(s_node):
    '''
    runs djikstras to get updated shortest paths wrt one ip source node
    ip: Starting node
    op: list of shortest distances to all other nodes in numerolgical order
    '''
    while len(processed_list) < n_nodes:
        cur_node = source_dist.index(min(source_dist))
        processed_list.append(cur_node)
        relax_adj(cur_node)


if __name__ == "__main__":
    s_node = 1   # get from Q
    n_nodes = 5  # get from Q
    djikstra_one_node(s_node)
