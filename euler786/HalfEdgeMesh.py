import numpy as np

from scipy.spatial import KDTree


def MAKE_POS_KEY(position):
    x, y = position

    if np.isclose(x, 0): x = 0      # prevent "-0.00"
    if np.isclose(y, 0): y = 0

    key = f"({x:.2f}, {y:.2f})"
    return key


class HalfEdge:
    def __init__(self, vertex=None, face=None):
        self.vertex: Vertex = vertex  # Target vertex of the half-edge
        self.face: Face = face  # Face this half-edge borders
        self.next: HalfEdge = None  # Next half-edge around the face
        self.twin: HalfEdge = None  # Twin half-edge

class Vertex:
    def __init__(self, position, color=None):
        self.position = np.array(position, dtype=np.float64)  # 3D coordinates of the vertex
        self.halfedge: HalfEdge = None  # One of the outgoing half-edges
        self.color = color

class Face:
    def __init__(self, color=None):
        self.halfedge: HalfEdge = None  # One of the half-edges bordering the face
        self.color = color

class HalfEdgeMesh:
    def __init__(self):
        self.vertices: list[Vertex] = []  # List of vertices
        self.halfedges: list[HalfEdge] = []  # List of half-edges
        self.faces: list[Face] = []  # List of faces

        self.vertex_pos_LUT = {}

    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)

        key = MAKE_POS_KEY(vertex.position)
        self.vertex_pos_LUT[key] = vertex

    def get_vertex_at_pos(self, position) -> Vertex | None:
        "Get a vertex at the given position if one exists"

        key = MAKE_POS_KEY(position)
        return self.vertex_pos_LUT.get(key)

        # for v in self.vertices:
        #     if np.all(np.isclose(v.position, position, atol=1e-5)):
        #         return v

        # return None

    def add_face(self, vertices: list[Vertex], color=None):
        # Create the half-edges for the face
        n = len(vertices)
        halfedges = [HalfEdge() for _ in range(n)]

        for i in range(n):
            halfedges[i].vertex = vertices[(i + 1) % n]
            halfedges[i].next = halfedges[(i + 1) % n]

        # Link the half-edges to the face
        face = Face(color=color)
        face.halfedge = halfedges[0]
        self.faces.append(face)

        for he in halfedges:
            he.face = face
            self.halfedges.append(he)

        # Assign half-edges to vertices
        for i, v in enumerate(vertices):
            if v.halfedge is None:
                v.halfedge = halfedges[i]

        return face

    def add_face_by_indices(self, vertex_indices):
        self.add_face([self.vertices[i] for i in vertex_indices])

    def link_twins(self):
        edge_map = {}

        for he in self.halfedges:
            v_start = he.vertex
            v_end = he.next.vertex
            edge_key = (v_end, v_start)

            if edge_key in edge_map:
                twin = edge_map[edge_key]
                he.twin = twin
                twin.twin = he
            else:
                edge_map[(v_start, v_end)] = he

    def __repr__(self):
        return f"HalfEdgeMesh(vertices={len(self.vertices)}, faces={len(self.faces)}, halfedges={len(self.halfedges)})"

# Example usage
if __name__ == "__main__":
    mesh = HalfEdgeMesh()

    # Add vertices
    v0 = mesh.add_vertex(Vertex((0, 0)))
    v1 = mesh.add_vertex(Vertex((1, 0)))
    v2 = mesh.add_vertex(Vertex((0, 1)))

    # Add face
    mesh.add_face_by_indices([0, 1, 2])

    # Link twin half-edges
    mesh.link_twins()

    print(mesh)
