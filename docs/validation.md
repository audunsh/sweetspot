# Evaluation

## Validation 

Although the algebraic approach may seem more transparent (and thus less prone to implementational errors) from as purely conceptual perspective, the resulting Python-script has about the same readability as the Möller-Trumbore script. Thus, the validation has been performed as follows:

1. The barycentric coordinate transform was tested against a trusted algorithm in the Trimesh [1] module (A well maintained and 2.2K starred github repo). 
2. A few tailored cases for intersecting and non-intersecting rays and triangles was tested with the algebraic solver.
3. A randomly generated set containing both intersecting and non-intersecting rays and triangles (500 cases) was visually inspected and compared to the results from the algebraic solver.  
4. The Möller-Trumbore algorithm was tested against the algebraic solver for 100000 randomly generated cases.
5. Finally, a Numba[2]-optimized Möller-Trumbore algorithm was tested against the algebraic solver.

The algorithms reproduce eachother exactly, and agrees well with both the designed and visually inspected results. We may thus have confidence in these implementations.

## Notes on performance

An internal benchmark comparison was made between the algebraic solver, the pure Python Möller-Trembore algorithm, and the numba-accelerated variant. The time per iteration (measuring 1e6 randomly generated pairs with a hit-rate of about 5%) in seconds was respectively 88.3e-6, 51.1e-6 and 2.2e-6 on my laptop CPU (Macbook Pro, 2018) - quite far above the state-of-the art 0.05e-6 seconds performance reported in the literature [3]. This can be due to many factors, probably overhead in Python, difference in the hardware, and probably most notably that these algorithms in general should be devised to work on batches of data (not single instances). 



---

## Sources

[1] https://trimsh.org/index.html

[2] https://numba.pydata.org/

[3] Pichler, T. A., Ferko, A., Ferko, M., Kán, P., & Kaufmann, H. (2022). Precomputed fast rejection ray-triangle intersection. _Graphics and Visual Computing_, 200047.

