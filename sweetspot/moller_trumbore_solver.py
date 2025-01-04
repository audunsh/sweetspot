import numpy as np
import numba as nb
from .core import ray, triangle

def moller_trumbore_ray_triangle_intersection(Ray: ray, Triangle: triangle)->(bool, float, np.array):
    """
    The Möller-Trumbore algorithm for triangle-ray intersection evaluation

    Author: Audun Skau Hansen (audunsh4@gmail.com), 2022

    ## Keyword arguments:

    | Method      | Description |
    | ----------- | ----------- |
    | Ray      |  An instance of the sweetspot.ray class    |
    | Triangle   | An instance of the sweetspot.triangle class      |

    ## Returns  
    
    A tuple containing 'hit' (a boolean indicator of whether the ray intersected or not),
    a float value 'a_star' indicating the distance for which the ray intersected the triangle,
    and finally a vector 'p_star' indicating the cartesian vector of the intersection.

    """
    hit = False
    a_star = 0
    p_star = np.zeros(3)
    
    # the required variables
    v21 = Triangle.compute_edge_vector(1,0)
    v31 = Triangle.compute_edge_vector(2,0)
    D = Ray.direction
    O = Ray.origin
    
    x1,x2,x3 = Triangle.X
    
    
    # intermediates (to avoid recomputing stuff)
    D_x_v31 = np.cross(D, v31)

    # Computing the denominator in Eq. 9
    denom = D_x_v31.dot(v21) #**-1
    
    if abs(denom)<1e-14:
        return (hit, a_star, p_star)
    
    Otilde = O - x1
    
    det = 1.0/denom
    
    u2 = det*D_x_v31.dot(Otilde)
    
    if u2<0:
        # point outside
        return (hit, a_star, p_star)
    
    O_x_v21 = np.cross(Otilde, v21)
    
    u3 = det*O_x_v21.dot(D)
    
    if u3<0 or u2+u3>1.0:
        # point outside
        return (hit, a_star, p_star)
    
    
    # Computing the full Eq. 9 
    a_star = det * O_x_v21.dot(v31)
    
    #u1 = 1 - u2 - u3
    
    # Collect and return reults
    if a_star<0:
        # triangle behind
        return (hit, a_star, p_star)
    
    hit = True
    
    p_star = O + a_star*D
    
    return (hit, a_star, p_star)


def moller_trumbore_ray_triangle_intersection_numba(Ray: ray, Triangle: triangle)->(bool, float, np.array):
    """
    A wrapper for the numba-optimized Möller-Trumbore algorithm for triangle-ray intersection evaluation

    Author: Audun Skau Hansen (audunsh4@gmail.com), 2022

    ## Keyword arguments:

    | Method      | Description |
    | ----------- | ----------- |
    | Ray      |  An instance of the sweetspot.ray class    |
    | Triangle   | An instance of the sweetspot.triangle class      |

    ## Returns  
    
    A tuple containing 'hit' (a boolean indicator of whether the ray intersected or not),
    a float value 'a_star' indicating the distance for which the ray intersected the triangle,
    and finally a vector 'p_star' indicating the cartesian vector of the intersection.
    """
    x1,x2,x3 = Triangle.X
    D = Ray.direction
    O = Ray.origin
    a_star = mt_rt_intersect_numba(x1,x2,x3,D,O)
    if a_star is None:
        return False , 0, O
    else:
        return True, a_star, Ray.get_point_at(a_star)
    

@nb.jit(nopython=True)
def mt_rt_intersect_numba(x1,x2,x3,D,O):
    """
    A numba-optimized Möller-Trumbore algorithm for triangle-ray intersection evaluation

    Author: Audun Skau Hansen (audunsh4@gmail.com), 2022

    ## Keyword arguments:

    | Argumentts      | Description |
    | ----------- | ----------- |
    | x1,x2,x3      | 3-component numpy-arrays containing the triangle vertices   |
    | D, O   | 3-component numpy arrays contatining the direction and origin of the ray     |

    ## Returns

    The value 'a_star' if intersection occurs, None else.
    """
    
    
    v21 = x2-x1
    v31 = x3-x1
    # intermediates (to avoid recomputing stuff)
    D_x_v31 = np.cross(D, v31)

    # Computing the denominator in Eq. 9
    denom = D_x_v31.dot(v21) #**-1
    
    if abs(denom)<1e-14:
        return None
    
    Otilde = O - x1
    
    det = 1.0/denom
    
    u2 = det*D_x_v31.dot(Otilde)
    
    if u2<0:
        # point outside
        return None
    
    O_x_v21 = np.cross(Otilde, v21)
    
    u3 = det*O_x_v21.dot(D)
    
    if u3<0 or u2+u3>1.0:
        # point outside
        return None
    
    
    # Computing the full Eq. 9 
    a_star = det * O_x_v21.dot(v31)
    
    
    # Collect and return reults
    if a_star<0:
        # triangle behind
        return None
    
    
    return a_star