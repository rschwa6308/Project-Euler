from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import LineCollection
import numpy as np

from HalfEdgeMesh import HalfEdgeMesh, Vertex, Face, HalfEdge

def plot_mesh(mesh: HalfEdgeMesh):
    # get bounding box extent
    points = np.array([v.position for v in mesh.vertices])
    width, height = np.ptp(points, axis=0)

    plot_size_inches = 0.5 * max(width, height)
    print(width, height)

    plot_size_inches = np.clip(plot_size_inches, None, 40)

    fig, ax = plt.subplots(figsize=(plot_size_inches, plot_size_inches))
    for he in mesh.halfedges:
        start = he.vertex.position
        end = he.next.vertex.position
        ax.plot([start[0], end[0]], [start[1], end[1]], color="black")

    for vertex in mesh.vertices:
        x, y = vertex.position
        ax.plot(x, y, color=vertex.color, marker="o")

    for face in mesh.faces:
        he = face.halfedge.next
        verts = [face.halfedge.vertex]
        while he is not face.halfedge:
            verts.append(he.vertex)
            he = he.next

        ax.fill([v.position[0] for v in verts], [v.position[1] for v in verts], color=face.color)

    ax.set_aspect("equal")
    return fig, ax



def reflect_point_over_line(p, segment):
    p = np.array(p)
    a, b = np.array(segment[0]), np.array(segment[1])

    # Line segment vector and its squared length
    ab = b - a
    ab_length_squared = np.dot(ab, ab)

    if ab_length_squared == 0:
        raise ValueError("Segment length cannot be zero; both endpoints of the segment are identical.")

    # Projection factor t for the closest point on the segment
    t = np.dot(p - a, ab) / ab_length_squared

    # Closest point on the segment
    closest_point = a + t * ab

    # Reflection calculation
    reflected_point = 2 * closest_point - p

    return reflected_point



def generate_tiling(num_reflections) -> HalfEdgeMesh:
    mesh = HalfEdgeMesh()

    # original kite
    r3 = np.sqrt(3)
    A = Vertex([0,    0   ], color="yellow")
    B = Vertex([1/2,  r3/2], color="blue")
    C = Vertex([2,    0   ], color="red")
    D = Vertex([1/2, -r3/2], color="blue")
    for v in [A, B, C, D]: mesh.add_vertex(v)

    mesh.add_face([A, D, C, B], color="gray")

    mesh.link_twins()

    # add a reflection over all boundary (i.e. un-twinned) edges
    reflections_count = 0
    for he in mesh.halfedges:
        if reflections_count >= num_reflections: break

        if he.twin is not None: continue

        a = he.vertex
        b = he.next.vertex
        c = he.next.next.vertex
        d = he.next.next.next.vertex

        cr_pos = reflect_point_over_line(c.position, (a.position, b.position))
        dr_pos = reflect_point_over_line(d.position, (a.position, b.position))

        # prevent creation of duplicate vertices by checking if a vertex already exists at the desired position
        cr = mesh.get_vertex_at_pos(cr_pos)
        if cr is None:
            cr = Vertex(cr_pos, color=c.color)
            mesh.add_vertex(cr)

        dr = mesh.get_vertex_at_pos(dr_pos)
        if dr is None:
            dr = Vertex(dr_pos, color=d.color)
            mesh.add_vertex(dr)

        mesh.add_face([b, a, dr, cr], color="wheat")


        mesh.link_twins()           # TODO: do this explicitly!

        reflections_count += 1
        if reflections_count % 10 == 0: print(reflections_count)

        # break   # TESTING

    return mesh



if __name__ == "__main__":
    num_reflections = 10_000

    print("Generating tiling... ", end="", flush=True)
    tiling = generate_tiling(num_reflections)
    print("done")

    fig, ax = plot_mesh(tiling)
    ax.set_title(f"num_reflections = {num_reflections}")

    plt.savefig(f"euler786/images/num_reflections={num_reflections}.png", bbox_inches="tight")
    plt.show()
