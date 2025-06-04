import sys
input = sys.stdin.readline

# Union-Find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

# 크루스칼 알고리즘
def kruskal_mst(V, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(V)
    total_weight = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            total_weight += weight
    
    return total_weight

# 입력 처리
V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# MST 가중치 출력
print(kruskal_mst(V, edges))