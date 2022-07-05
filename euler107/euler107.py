# Minimum Spanning Tree... EZ! We use Kruskal's Algorithm.


def MST(E):
    V = list(range(len(E)))

    edge_list = []
    for u in V:
        for v in V:
            if u >= v: continue
            if E[u][v] is not None:
                edge_list.append((u, v, E[u][v]))
    
    edge_list.sort(key=lambda e: e[2])

    trees = [{v} for v in V]

    def find_tree(v):
        for tree in trees:
            if v in tree:
                return tree

    mst = set()

    for u, v, w in edge_list:
        tree_u, tree_v = find_tree(u), find_tree(v)
        if tree_u is not tree_v:
            mst.add((u, v, w))
            trees.remove(tree_u)
            trees.remove(tree_v)
            trees.append(tree_u.union(tree_v))
    
    return mst


EDGES = []

with open("p107_network.txt") as f:
    for line in f.readlines():
        items = line.strip().split(",")
        EDGES.append([int(x) if x.isdigit() else None for x in items])


original_weight = sum(sum([x for x in row if x is not None]) for row in EDGES) // 2

mst = MST(EDGES)
mst_weight = sum(w for _, _, w in mst)

print(original_weight - mst_weight)

# => 259679
