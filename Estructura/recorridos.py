from Estructura.ciudad import Ciudad
from Estructura.barrio import Barrio


class Recorridos:
    def Kruskal(self):
        def __init__(self):
            self.barrios = []
            self.tubos = []
            self.visitados = []
            self.minimo = None

        self.minimo = Ciudad()
        aux_tubos = list(self.tubos)
        aux_tubos.sort(key=lambda tubo: tubo.capacidad)

        for barrio in self.barrios:
            self.minimo.agregarBarrio(Barrio(barrio.id))

        for tubo in aux_tubos:
            if tubo.A in self.visitados:
                continue
            self.minimo.agregarTuberia(tubo.origen, tubo.destino, tubo.capacidad)
            self.visitados.append(tubo.destino)

    def ford_fulkerson(ciudad, source, sink, debug=None):
        fluido, path = 0, True

        while path:
            # search for path with flow reserve
            path, reserve = depth_first_search(graph, source, sink)
            flow += reserve
            # increase flow along the path
            for v, u in zip(path, path[1:]):
                if graph.has_edge(v, u):
                    graph[v][u]["flow"] += reserve
                else:
                    graph[u][v]["flow"] -= reserve

            # show intermediate results
            if callable(debug):
                debug(graph, path, reserve, flow)

    def depth_first_search(graph, source, sink):
        undirected = graph.to_undirected()
        explored = {source}
        stack = [(source, 0, undirected[source])]

        while stack:
            v, _, neighbours = stack[-1]
            if v == sink:
                break

            # search the next neighbour
            while neighbours:
                u, e = neighbours.popitem()
                if u not in explored:
                    break
            else:
                stack.pop()
                continue

            # current flow and capacity
            in_direction = graph.has_edge(v, u)
            capacity = e["capacity"]
            flow = e["flow"]
            # increase or redirect flow at the edge
            if in_direction and flow < capacity:
                stack.append((u, capacity - flow, undirected[u]))
                explored.add(u)
            elif not in_direction and flow:
                stack.append((u, flow, undirected[u]))
                explored.add(u)
        # (source, sink) path and its flow reserve
        reserve = min((f for _, f, _ in stack[1:]), default=0)
        path = [v for v, _, _ in stack]

        return path, reserve
