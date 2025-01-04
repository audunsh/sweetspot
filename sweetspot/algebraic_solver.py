import numpy as np
from .core import ray, triangle

def algebraic_ray_triangle_intersection(Ray: ray, Triangle: triangle)->(bool, float, np.array):
    """
    The algebraic ray-triangle intersection algorithm 
    
    Author: Audun Skau Hansen (audunsh4@gmail.com) 2022

    ## Keyword arguments:

    | Arguments      | Description |
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
    

    # Get origin and direction of ray
    O = Ray.origin
    D = Ray.direction
    
    # compute the norm of the plane ( Eq.3 )
    N = Triangle.compute_norm()
    
    # assert that ray is not orthogonal to plane
    if abs(np.dot(Ray.direction, N))<1e-14:
        # ray orthogonal to plane
        return (hit, a_star, p_star)
    
    # compute the distance of the plane 
    d = Triangle.compute_distance_to_origin()
    
    
    # compute a_star (Eq. 5)
    a_star = -((N.dot(O) - d)/N.dot(D))
    
    if a_star<0:
        # triangle behind ray
        return (hit, a_star, p_star)
    

    # compute the intersection point (if any)
    p_star = O + a_star*D
    
    
    # compute barycentric coordinates
    bcent = Triangle.compute_barycentric_coordinates(p_star)
    
    
    if np.any(bcent<0):
        # point outside triangle
        return (hit, a_star, p_star)
    
    
    
    
    
    hit = True
    
    
    return hit, a_star, p_star