# The classic algebraic solution

## Intersecting the plane

The set of points $\{ \mathbf{x}_p \}$ on the  plane spanned by $T$ are uniquely determined by the norm $\mathbf{N}$ of the triangle, given by the cross product

$$\mathbf{N} = \frac{ (\mathbf{x}_2 - \mathbf{x}_1) \times (\mathbf{x}_3 - \mathbf{x}_1)}{\lVert (\mathbf{x}_2 - \mathbf{x}_1) \times (\mathbf{x}_3 - \mathbf{x}_1) \rVert}, \tag{3}$$

together with the distance $d$ from $(0,0,0)$ to the center of the plane $\mathbf{C}$:

$$ d = \lVert  \mathbf{C} \rVert ,$$

through the equation

$$\mathbf{N}\cdot \mathbf{x}_p - d =0.\tag{4}$$

Thus, for the point $x_* = P_*$ where $R$ intersects the plane, we find that inserting Eq.(1) in Eq.(3) yields 

$$\mathbf{N}\cdot(\mathbf{O} + a_* \mathbf{D}) - d =0.$$

The above may be solved for $a_*$ to find the relation

$$a_* = -\frac{\mathbf{N}\cdot \mathbf{O}+d}{\mathbf{N} \cdot \mathbf{D}}, \tag{5}$$

providing us with an explicit algebraic expression for the intersection point

$$ \mathbf{P}_* = \mathbf{O} -\Big{(} \frac{\mathbf{N}\cdot \mathbf{O}+d}{\mathbf{N} \cdot \mathbf{D}}\Big{)} \mathbf{D}.  \tag{6} $$

We note that (i) the expression is singular when $\mathbf{D}$ is orthogonal to $\mathbf{N}$, indicating that the ray is parallel to the plane (they don't intersect) and (ii) the equation may yield a negative $a_*$, indicating that the ray does not intersect the triangle (from our definition of $a$ in Eq.(1).

## Boundary check on triangle

A standard way to determine whether or not the point $\mathbf{P}_*$ is within the triangle $T$ is a so called *point-in-polygon-test* [1,2], which can be based on the fact that the cross-product between the vectors from the vertices of the triangle to the point $\mathbf{P}_i=\mathbf{x}_i - \mathbf{P}_*$  and the vertex vectors $\mathbf{X}_{ij}=\mathbf{x}_j-\mathbf{x}_i$, where $i$ and $j$ are always chosen in the same cyclic (increasing) order should be aligned *with* the norm of the plane $\mathbf{N}$ whenever $\mathbf{P}_*$ is to the left of $\mathbf{X}_ij$ and oppositely aligned if not. 

Thus, the point $\mathbf{P}_*$ is inside the triangle $T$ if

$$\mathbf{N} \cdot (\mathbf{X}_{ij} \times \mathbf{P}_i)>0 \: \: \forall \: i \in (1,2,3). $$

Another approach is to do a coordinate transform into barycentric coordinates $\{u_i\}$  [3], where any negative coordinate will indicate the point being outside of the triangle. The barycentric unit vectors are simply the vertices of the triangle $\{\mathbf{x}_i\}$, so that the intersection point may now be expressed

$$\mathbf{P}_{*}=\sum_i \mathbf{x}_i u_i.$$

In order to determine the coordinates, we may compute the fractional area of the of the triangles formed by $\{\mathbf{x}_i, \mathbf{x}_j, \mathbf{P}_*\}_{i\neq j}$, such that

$$u_1= \frac{\text{Area}(\mathbf{x}_1, \mathbf{x}_2, \mathbf{P}_*)}{\text{Area}(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3)},$$ 

and

$$u_2= \frac{\text{Area}(\mathbf{x}_2, \mathbf{x}_3, \mathbf{P}_*)}{\text{Area}(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3)},$$

and finally using the fact that $\sum_i u_i = 1$  to obtain

$$u_3 = 1 - u_1 - u_2. \tag{7}$$

For this project, we shall employ the latter method, since it also forms the basis for the more efficient Möller-Trumbore algorithm we'll implement later on. 

---

## Sources

[1] https://en.wikipedia.org/wiki/Point_in_polygon

[2] https://erich.realtimerendering.com/ptinpoly/

[3] https://en.wikipedia.org/wiki/Barycentric_coordinate_system