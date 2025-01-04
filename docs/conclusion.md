# Prospects and conclusion

Has there been any recent developement in the field? In a recent publication [1], Pichler et al. claims to demonstrate their algorithm named *"The Precomputed fast rejection ray-triangle intersection"* to promise speedups of up to 35% over the standard Möller-Trumbore algorithm [2] by either (i) transforming the triangle into a unit triangle, simplifying certain aspects of the problem, or (ii) doing a similarity transform of the triangle onto a 2D surface, allowing for pruning of areas surrounding the triangle.

Instead of replicating their review of the current state of the art here, I'd just like to point out that the paper offers an informative insight into the various venues which has been explored in order to reduce this computational bottleneck. However, the paper essentially indicates that under general conditions, the Möller-Trumbore algorithm has yet to be defeated (altough there are algorithms able to compete and even superseed it under special conditions).

The proposed method consists of the following steps:
1. Test for intersection between the ray and the bounding sphere, discard triangle if no intersection.
2. Calculate the ray-plane intersection point
3. Test whether the intersection point is inside the axis-aligned bounding-box (AABB) [3], discard if not.
4. Apply a 2D transform, and perform tests in 2D to determine if point is inside the triangle.


# Speculations and ideas

As an afterthought - how does the human brain perform the same operation? Intuitively, we need only see the ray and triangle in front of us, and immediately recognize wheter or not they intersect. The effectiveness is essentially due to our ability to rapidly interpret complex stereoscopic information. It is however prone to misinterpretation and inaccuracies. Furthermore, it is clear that the visual representation we observe is not the same as the mathematical representation intetrpreted by the code (thus the need for projections in the first place).

During this project, I've had some ideas however. Perhaps it could be useful to do a two step projection of the ray and the triangle; first onto the three planes spanned by the x-y, x-z and y-z unit vectors. Thereafter, for each of the three projections, the (2D triangle) and ray may now be projected as a section and point respectively on a circle around the rays origin. If the rays point (or angle) is within the section of the disc constituting the triangle in all three planes, I believe this would indicate that the ray intersects the triangle. (Unclear to me where exactly, though). This idea is gemetrically simple and on the face of it cheap (but I'm sure there is something I havent thought completely through still).

A second idea would be to do something inspired by wavelets, having the triangles nested inside of eachother. I believe this procedure is similar to the recent Nanite-engine by Unreal.

On a side-node, could ML-techniques (neural nets) be used? This is probably not such a good idea, since the core algorithms discussed here are significantly faster than what you achieve with moderately sized matrix-products, meaning that unless it were to be implemented on batches or a higher hiearchical level than the explicit triangles, it would probably perform slower than the standard algorithms used today. 

Finally, I'd like to just point out that there is room for further optimization of these algorithms. Actually, as you of course are aware, there is no need to reinvent the wheel here. A pragmatic approach would be to reuse standard implementations in OpenGL, WebGPU, CUDA or the platform of choice, to achieve optimal performance in whatever application one desires. 

---

## Sources

[1] Pichler, T. A., Ferko, A., Ferko, M., Kán, P., & Kaufmann, H. (2022). Precomputed fast rejection ray-triangle intersection. _Graphics and Visual Computing_, 200047.

[2] Möller, T., & Trumbore, B. (2005). Fast, minimum storage ray/triangle intersection. In _ACM SIGGRAPH 2005 Courses_ (pp. 7-es).

[3] Áfra, A. T. (2012). Incoherent Ray Tracing without Acceleration Structures. In _Eurographics (Short Papers)_ (pp. 97-100).





