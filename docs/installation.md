# Installation and execution

The project has been implemented as a Python-module, dependent only on Numpy [1] and Numba [2]. 

You may install the project and its dependencies using the standard pip command from the projects root directoy:

```
pip install .
```

# Running tests

# Using the module

## Import 

The module is imported as

```
import sweetspot
```

## Triangles and rays

You may thereafter create triangles:

```
t1 = sweetspot.triangle(x1,x2,x3)
```

...where ```xn``` are 3-component numpy arrays. A ray is instantiated as follows:

```
r1 = sweetspot.ray(o,d)
```

...where ```o``` and ```d``` are 3-component numpy-arrays defining the rays origin and direction respectively (note that ```d``` will automatically be normalized).

## Intersections

Finally, you may compute intersections using either the algebraic approach:

```
hit, a_star, p_star = sweetspot.algebraic_ray_triangle_intersection(r,t)
```

...the Möller-Trumbore algorithm...

```
hit, a_star, p_star = sweetspot.moller_trumbore_ray_triangle_intersection(r,t)
```

...or a numba-optimized Möller-Trumbore algorithm (which should be the goto choice at least within this module):

```
hit, a_star, p_star = sweetspot.moller_trumbore_ray_triangle_intersection_numba(r,t)
```



