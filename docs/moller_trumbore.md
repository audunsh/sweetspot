# The Möller-Trumbore algorithm

With a working solver for validation, we can move on to more advanced algorithms.  The Möller-Trumbore algorithm was introduced in a 2005-paper titled "Fast, minimum storage ray/triangle intersection" [1], and is based on transforming the problem into barycentric coordinates. As previously discussed, the interserction point in barycentric coordinates is, when fully expanded

$$\mathbf{P}_{*} = \mathbf{x}_1 u_1 + \mathbf{x}_2 u_2 + \mathbf{x}_3 u_3.$$

From the relation in Eq.(7) we see that this can be rewritten

$$\mathbf{P}_{*} = \mathbf{x}_1 (1-u_2 - u_3) + \mathbf{x}_2 u_2 + \mathbf{x}_3 u_3 ,$$

which can be reorganized into

$$\mathbf{P}_{*} = \mathbf{x}_1 + (\mathbf{x}_2-\mathbf{x}_1) u_2 + (\mathbf{x}_3-\mathbf{x}_1)u_3  .$$

If we now insert the explicit expression for the ray, we find

$$\mathbf{O} + a_*\mathbf{D} = \mathbf{x}_1 + (\mathbf{x}_2-\mathbf{x}_1) u_2 + (\mathbf{x}_3-\mathbf{x}_1)u_3 ,$$

which may be rearranged into

$$\mathbf{O} -\mathbf{x}_1 = - a_*\mathbf{D} + (\mathbf{x}_2-\mathbf{x}_1) u_2 + (\mathbf{x}_3-\mathbf{x}_1)u_3 ,$$

where $u_1$, $u_2$ and $a_*$ are unknown, forming a system of coupled equations:

$$\begin{align}  
     \begin{bmatrix}  
           \mathbf{-D}  ,
           (\mathbf{x}_{2}-\mathbf{x}_{1}),   
           (\mathbf{x}_{3}-\mathbf{x}_{1})  
         \end{bmatrix} \begin{bmatrix}  
            a_*  \\
           u_{2} \\  
           u_{3}  
         \end{bmatrix}=\mathbf{O} -\mathbf{x}_1 .
 \end{align}$$

Since the elements in the first row-vector on the left are vectors, this is a $3 \times 3$ matrix. Realizing this, we may simplify once more to a matrix-vector product

$$M\mathbf{u}_* = \tilde{\mathbf{O}}, \tag{8}$$

which can be solved using any standard solver (preferably not by inversion) to find:

$$\mathbf{u}_* =M^{-1} \tilde{\mathbf{O}}.$$

In their original paper [1], Möller and Trumbore solve this system using Cramers rule [2]. We have followed the same procedure, i.e. by defining $\mathbf{v}_{ij} = (\mathbf{x}_{i}-\mathbf{x}_{j})$, whereby we finally compute

$$ \begin{align}    
     \begin{bmatrix}  
            a_*  \\
           u_{2} \\  
           u_{3}  
         \end{bmatrix}=
         \frac{1}{(\mathbf{D} \times \mathbf{v}_{31}) \cdot \mathbf{v}_{21}}
         \begin{bmatrix}  
           (\tilde{\mathbf{O}} \times \mathbf{v}_{21}) \cdot \mathbf{v}_{31} \\
           (\mathbf{D} \times \mathbf{v}_{31}) \cdot \tilde{\mathbf{O}} \\  
          (\tilde{\mathbf{O}} \times \mathbf{v}_{21})\cdot{\mathbf{D}}   
         \end{bmatrix}. \tag{9}
  \end{align}$$

As the note in the paper [1], it is possible to define intermediates in the above to speed up the calculation. 

---

## Sources

[1] Möller, T., & Trumbore, B. (2005). Fast, minimum storage ray/triangle intersection. In _ACM SIGGRAPH 2005 Courses_ (pp. 7-es).

[2] https://en.wikipedia.org/wiki/Cramer%27s_rule



