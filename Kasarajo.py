from collections import defaultdict
class Graph():
    def __init__(self):
        self.vertices = set()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.update([u, v])

    def dfs(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for node in self.graph[v]:
            if not visited.get(node, False):
                self.dfs(node, visited, component)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for node in self.graph[v]:
            if not visited.get(node, False):
                self.fill_order(node, visited, stack)
        stack.append(v)

    def reverse(self):
        rgraph = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                rgraph.add_edge(v, u)
        return rgraph

    def kosaraju(self):
        stack = []
        visited = {}
        reversed_graph = self.reverse()
        for v in reversed_graph.vertices:
            if not visited.get(v, False):
                reversed_graph.fill_order(v, visited, stack)

        visited = {}
        sccs = []
        while stack:
            v = stack.pop()
            if not visited.get(v, False):
                component = []
                self.dfs(v, visited, component)
                sccs.append(component)
        return sccs
def parse_input(text):
    g = Graph()
    for line in text.strip().splitlines():
        func, calls = line.split(':')
        func = func.strip()
        callees = [f.strip() for f in calls.strip().split(',') if f.strip()]
        for callee in callees:
            g.add_edge(func, callee)
    return g
input_text = """
foo: bar, baz, qux
bar: baz, foo, bar
qux: qux
"""
g = parse_input(input_text)

sccs = g.kosaraju()
largest_scc = max(sccs, key=len)
print(largest_scc)

funcs = set()
for comp in sccs:
    if len(comp) > 1:
        funcs.update(comp)
    else:
        f = comp[0]
        if f in g.graph[f]:
            funcs.add(f)
print("Recursiveness:")
for v in sorted(g.vertices):
    print(f"{v}: {"YES" if v in funcs else "NO"}")

