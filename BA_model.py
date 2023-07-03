import argparse
import heapq
import csv
import matplotlib.pyplot as plt
import numpy as np

def save_dataset(edges, path):
    f = open(path, 'w', newline='')
    csvout = csv.writer(f, delimiter='\t')
    for edge in edges:
        csvout.writerow(edge)


def BA_model(m_0, m, t, path):
    if m > m_0:
        print("初始节点个数不能小于每个时间点增加的边数")
    edges = []
    degree = []
    for i in range(m_0):
        degree.append(0)

    total_degree = 0
    for i in range(m_0, t+m_0):
        if total_degree == 0:
            p_degree = np.array([1. / len(degree) for _ in degree])
        else:
            p_degree = np.array([dg / total_degree for dg in degree])

        pval = np.random.multinomial(m, p_degree)
        neighbor_list = heapq.nlargest(m, range(len(degree)), pval.take)
        for edge in neighbor_list:
            degree[edge] += 1
            edges.append((i, edge))
        degree.append(m)
        #print(neighbor_list)
        total_degree += 2 * m

    degree_cnt = {}
    for i in range(len(degree)):
        if not degree_cnt.__contains__(degree[i]):
            degree_cnt[degree[i]] = 1
        else:
            degree_cnt[degree[i]] += 1
    distribution = []
    #print(distribution)
    for key, val in degree_cnt.items():
        distribution.append((key, val))
    distribution.sort()
    #print(distribution)
    plt.yscale('log')
    plt.xscale('log')
    plt.scatter(np.array(distribution)[:, 0], np.array(distribution)[:, 1])
    plt.show()

    save_dataset(edges, path)

def parse_args():
    '''
    parse args from the command line
    '''
    parser = argparse.ArgumentParser(description="sns algorithm for hyperbolic embedding")

    parser.add_argument("--edgelist", dest="edgelist", type=str, default='',
                        help="edgelist to save.")

    parser.add_argument("--m0", dest="m0", type=int, default=3,
                        help="初始节点个数")
    parser.add_argument("--m", dest="m", type=int, default=3,
                        help="每个时间点增加边数")
    parser.add_argument("--t", dest="t", type=int, default=1000,
                        help="运行时间")





    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    BA_model(args.m0, args.m, args.t, args.edgelist)
