A typical use-case scenario can be as follows

```Python

import numpy as np

from sweetspot import ray, triangle, moller_trumbore_ray_triangle_intersection_numba

# set up a triangle
x1,x2,x3 = np.random.uniform(-1,1,(3,3))
t = triangle(x1,x2,x3)

# set up a ray
o,d = np.random.uniform(-1,1,(2,3))
r = ray(o,d)

# check if they intersect
hit, a_star, p_star = moller_trumbore_ray_triangle_intersection_numba(r,t)

# print results
if hit:
    print("ray intersects triangle at", p_star)
    print("in a distance", p_star, "from the origin.")
else:
    print("ray does not intersect triangle")

    
```