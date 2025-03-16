from dataclasses import dataclass
import os
import pickle
import numpy as np
from tqdm import tqdm
# from scipy.optimize import fsolve
import sympy as sp


def solve_tangency_equation_analytically():
    x, y, a, b, Ex, Ey, Px, Py = sp.symbols('x y a b Ex Ey Px Py', real=True)

    # Ellipse equation
    ellipse_eq = (x-Ex)**2 / a**2 + (y-Ey)**2 / b**2 - 1

    # Tangency slope condition
    slope_condition = sp.Eq(
        (y - Py) / (x - Px),                    # slope of line
        (-b**2 * (x-Ex)) / (a**2 * (y-Ey))      # slope of ellipse at (x, y) (from implicit differentiation)
    )

    sol = sp.solve([ellipse_eq, slope_condition], (x, y), dict=False)
    return sol


SOLUTION_CACHE_FNAME = "euler246/sympy_solution_cache.pickle"

# Load the solution from the file
if os.path.isfile(SOLUTION_CACHE_FNAME):
    with open(SOLUTION_CACHE_FNAME, "rb") as file:
        SOLVE = pickle.load(file)

    print("Analytic solution loaded from file!")

else:
    print("Solving analytically...")
    SOLVE = solve_tangency_equation_analytically()
    print("Solving done!")

    # Save the solution to a file
    with open(SOLUTION_CACHE_FNAME, "wb") as file:
        pickle.dump(SOLVE, file)

# Lambdify solution (fast!)
VARS = list(SOLVE[0][0].free_symbols)
SOLVE_LAMBDAS = [
    [
        sp.lambdify(VARS, expr)
        for expr in solution
    ]
    for solution in SOLVE
]




@dataclass
class AxisAlignedEllipse:
    a: float
    b: float

    x0: float
    y0: float

    @staticmethod
    def from_foci(f1, f2, total_distance: float) -> "AxisAlignedEllipse":
        # Compute the ellipse center
        center = (f1 + f2) / 2

        # Compute the distance from the foci to the ellipse center
        c = np.linalg.norm(f1 - f2) / 2

        # Compute semi-major axis (a)
        a = total_distance / 2
        if a <= c:
            raise ValueError("Invalid parameters: semi-major axis must be greater than half the focal distance")

        # Compute semi-minor axis (b)
        b = np.sqrt(a**2 - c**2)

        return AxisAlignedEllipse(a=a, b=b, x0=center[0], y0=center[1])


import sympy as sp


def get_tangent_points(P, ellipse: AxisAlignedEllipse):
    "Given an ellipse defined by `x^2/a^2 + y^2/b^2 = 1` and an external point `P`, compute the tangent points `R` and `S`."

    tangent_points = []

    substitutions = {
        "a":  ellipse.a,
        "b":  ellipse.b,
        "Ex": ellipse.x0,
        "Ey": ellipse.y0,
        "Px": P[...,0],
        "Py": P[...,1]
    }

    args = []
    for var in VARS:
        args.append(substitutions[str(var)])

    for solution in SOLVE_LAMBDAS:
        xs = solution[0](*args)
        ys = solution[1](*args)

        tangent_points.append(np.column_stack([xs, ys]))
    
    # tangent_points.dims = (sol, batch, var)

    return np.array(tangent_points, dtype=np.float64).swapaxes(0, 1)


# TESTING
# Ps = np.array([
#     (3, 4),
#     (10, 20),
#     (-5, 7),
# ])
# ellipse = AxisAlignedEllipse(a=5, b=3, x0=0, y0=0)
# tangent_points = get_tangent_points(Ps, ellipse)
# print("Tangent Points:", tangent_points)


def angle3(A, B, C, degrees=True):
    "Compute the magnitude of the angle ∠ABC"
    
    BA = A - B
    BC = C - B
    
    dot_product = np.sum(BA * BC, axis=-1)
    norm_BA = np.linalg.norm(BA, axis=-1)
    norm_BC = np.linalg.norm(BC, axis=-1)

    cos_theta = dot_product / (norm_BA * norm_BC)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)   # numerical stability for arccos

    theta = np.arccos(cos_theta)
    
    return np.rad2deg(theta) if degrees else theta


assert(np.isclose(angle3(
    np.array([1, 1]),
    np.array([0, 0]),
    np.array([1, 0])
), 45))

epsilon = 1e-12

assert(not angle3(
    np.array([1, 1]),
    np.array([0, 0]),
    np.array([1, 0])
) > 45 + epsilon)



def count_valid_lattice_points(ellipse):
    "Count the number of lattice points P ∈ Z^2 outside the given ellipse such that the angle subtended by P with its two points of tangency on the ellipse is > 45 degrees"

    count = 0

    ellipse_width = 2 * ellipse.a
    MAX_DIST = int(1.5 * ellipse_width)        # should be enough

    for xoff in tqdm(np.arange(-MAX_DIST, MAX_DIST, dtype=np.float64)):
        # batch by row (for convenience)
        yoffs = np.arange(-MAX_DIST, MAX_DIST, dtype=np.float64)

        x  = ellipse.x0 + xoff
        ys = ellipse.y0 + yoffs

        batch_size = len(ys)

        Ps = np.zeros((batch_size, 2), dtype=np.int64)
        Ps[:,0] = x
        Ps[:,1] = ys

        outside_ellipse_mask = (Ps[:,0] - ellipse.x0)**2 / ellipse.a**2 + (Ps[:,1] - ellipse.y0)**2 / ellipse.b**2 > 1.0
        Ps = Ps[outside_ellipse_mask]

        batch_res = get_tangent_points(Ps, ellipse)

        Rs = batch_res[:,0]
        Ss = batch_res[:,1]

        thetas = angle3(Rs, Ps, Ss, degrees=True)

        count += np.count_nonzero(thetas > 45 + epsilon)
        # print(count)
        # print(int(round(count / SCALE**2)))
        
    return count



if __name__ == "__main__":
    ellipse = AxisAlignedEllipse.from_foci(
        f1=np.array([-2_000, 1_500]),
        f2=np.array([ 8_000, 1_500]),
        total_distance=15_000
    )

    # DEBUG
    SCALE = 1.0
    ellipse.a *= SCALE
    ellipse.b *= SCALE

    print(ellipse)

    # Naive lattice search: number of points to test grows with Ellipse Area (~10^10)
    #
    # Observation: Theta increases monotonically with distance from ellipse.
    #              The function is also smooth.
    #              Therefore, the region in which theta>45 holds is bounded by a smooth curve (quite possibly also an ellipse).
    # 
    # Region boundary search: number of points to test grows with Ellipse Circumference (~10^5)

    res = count_valid_lattice_points(ellipse)

    res = int(round(res / SCALE**2))        # DEBUG

    print(res)


# => 810834388
