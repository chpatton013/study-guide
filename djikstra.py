#!/usr/bin/env python3

from collections import defaultdict
from typing import Generator, List, Optional, Set, Tuple


class Edge:
    def __init__(self, source: str, destination: str, cost: float):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.source} --[{self.cost}]-> {self.destination}"


class Graph:
    def __init__(self, nodes: Set[str], edges: List[Edge]):
        self.nodes = nodes
        self.edges = edges

    def __str__(self) -> str:
        as_str = ""
        as_str += "Graph(\n"
        as_str += "  nodes: {\n"
        for node in sorted(self.nodes):
            as_str += f"    {node}\n"
        as_str += "  }\n"
        as_str += "  edges: {\n"
        for edge in self.edges:
            as_str += f"    {edge}\n"
        as_str += "  }\n"
        as_str += ")"
        return as_str


class PathNode:
    def __init__(self, node: str, cost: Optional[float]):
        self.node = node
        self.cost = cost

    def __str__(self) -> str:
        return f"PathNode({self.node}, {self.cost})"

    def __eq__(self, other) -> bool:
        return self.node == other.node and self.cost == other.cost


class Path:
    def __init__(self, source: str, nodes: List[PathNode]):
        self.source = source
        self.nodes = nodes

    def __str__(self) -> str:
        as_str = ""
        as_str += f"Path({self.cost}: {self.source}"
        for node in self.nodes:
            as_str += f" --[{node.cost}]-> {node.node}"
        as_str += ")"
        return as_str

    @property
    def cost(self) -> float:
        return sum(node.cost for node in self.nodes)


class Frame:
    def __init__(self, destination: str, sources: List[PathNode]):
        self.destination = destination
        self.sources = sources

    def __str__(self) -> str:
        return f"Frame({self.destination}: [{', '.join(str(s) for s in self.sources)}])"


class Djikstra:
    def __init__(self, graph: Graph, source: str, destination: str):
        self.source = source
        self.destination = destination

        reverse_edges = defaultdict(list)
        for edge in graph.edges:
            reverse_edges[edge.destination].append(
                PathNode(edge.source, edge.cost)
            )

        self.frames = {
            node: Frame(node, reverse_edges[node])
            for node in graph.nodes
        }

    def __str__(self) -> str:
        as_str = ""
        as_str += "Djikstra(\n"
        as_str += f"  source: {self.source}\n"
        as_str += f"  destination: {self.destination}\n"
        as_str += "  frames: [\n"
        for node, frame in sorted(self.frames.items()):
            as_str += f"    {node}: {frame}\n"
        as_str += "  ]\n"
        as_str += ")"
        return as_str

    def _generate(self, source: str, destination: str,
                  visited: Set[str]) -> Generator[Path, None, None]:
        if destination in visited:
            return
        visited.add(destination)

        if source == destination:
            yield Path(source, [])
        else:
            for path_node in self.frames[destination].sources:
                next_path_node = PathNode(destination, path_node.cost)
                for path in self._generate(
                    source, path_node.node, visited.copy()
                ):
                    path.nodes.append(next_path_node)
                    yield path

    def generate(self) -> Generator[Path, None, None]:
        yield from self._generate(self.source, self.destination, set())


GRAPH = Graph(
    {
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7",
        "n8",
        "n9",
    },
    [
        Edge("n1", "n2", 1.0),
        Edge("n1", "n3", 1.0),
        Edge("n1", "n4", 1.0),
        Edge("n2", "n4", 1.0),
        Edge("n3", "n2", 1.0),
        Edge("n3", "n2", 2.0),
        Edge("n4", "n5", 1.0),
        Edge("n5", "n6", 1.0),
        Edge("n6", "n7", 1.0),
        Edge("n7", "n8", 1.0),
        Edge("n7", "n9", 1.0),
        Edge("n8", "n9", 1.0),
        Edge("n9", "n8", 1.0),
    ],
)

DJIKSTRA = Djikstra(GRAPH, "n1", "n8")

print(GRAPH)
print(DJIKSTRA)

for path in DJIKSTRA.generate():
    print(path)
