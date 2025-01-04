import sweetspot as sp
import numpy as np

# test ray class

def test_ray():
    R = sp.ray(np.zeros(3), np.array([1.0, 1.0, 1.0]))
    assert(np.allclose(R.get_point_at(1) , np.ones(3)*np.sqrt(3)**-1))

def test_x_ray():
    R = sp.ray(np.zeros(3), np.array([1.0, 0.0, 0.0]))
    assert(np.allclose(R.get_point_at(10) , np.array([10.0, 0.0, 0.0])))

def test_y_ray():
    R = sp.ray(np.zeros(3), np.array([0.0, 1.0, 0.0]))
    assert(np.allclose(R.get_point_at(10) , np.array([0.0, 10.0, 0.0])))

def test_z_ray():
    R = sp.ray(np.zeros(3), np.array([0.0, 0.0, 1.0]))
    assert(np.allclose(R.get_point_at(10) , np.array([0.0, 0.0, 10.0])))

def test_negative_ray():
    R = sp.ray(np.zeros(3), np.array([-1.0, -1.0, -1.0]))
    assert(np.allclose(R.get_point_at(1) , -1*np.ones(3)*np.sqrt(3)**-1))

def test_triangle_area():
    x1 = np.array([.5,-.4, .9])
    x2 = np.array([-.5,1.0, 5])
    x3 = np.array([1.0,3.0, -.2])
    t = sp.triangle(x1,x2,x3)
    assert(abs(t.compute_area()-8.02095536703702)<=1e-14)
    
def test_triangle_barycentric():
    x1 = np.array([.5,-.4, .9])
    x2 = np.array([-.5,1.0, 5])
    x3 = np.array([1.0,3.0, -.2])
    t = sp.triangle(x1,x2,x3)
    assert(np.allclose(t.compute_barycentric_coordinates(.5*x1 + .5*x2),np.array([0.5,0.5,0.0])))
    
def test_triangle_edge_vectors():
    x1 = np.array([.5,-.4, .9])
    x2 = np.array([-.5,1.0, 5])
    x3 = np.array([1.0,3.0, -.2])
    t = sp.triangle(x1,x2,x3)
    assert(np.allclose(t.compute_edge_vector(0,1),x1-x2))
    assert(np.allclose(t.compute_edge_vector(1,2),x2-x3))
    assert(np.allclose(t.compute_edge_vector(2,0),x3-x1))
    assert(np.allclose(t.compute_edge_vector(1,0),x2-x1))
    assert(np.allclose(t.compute_edge_vector(2,1),x3-x2))
    assert(np.allclose(t.compute_edge_vector(0,2),x1-x3))


def test_moller_trombore_numba_hit():
    Nt = 1000
    test_triangles = np.random.uniform(-5,5,(Nt,3,3))
    test_rays = np.random.uniform(-5,5,(Nt,2,3))
    hit_integrity=True
    

    for i in range(Nt):
        x1,x2,x3 = test_triangles[i]
        t = sp.triangle(x1,x2,x3)
        o, d = test_rays[i]
        r = sp.ray(o,d)

        hit1,a_star1, p_star1 = sp.algebraic_ray_triangle_intersection(r,t)
        hit2,a_star2, p_star2 = sp.moller_trumbore_ray_triangle_intersection_numba(r,t)
        if hit1!=hit2:
            hit_integrity = False

    assert(hit_integrity)

def test_moller_trumbore_hit():
    Nt = 1000
    test_triangles = np.random.uniform(-5,5,(Nt,3,3))
    test_rays = np.random.uniform(-5,5,(Nt,2,3))
    hit_integrity=True
    

    for i in range(Nt):
        x1,x2,x3 = test_triangles[i]
        t = sp.triangle(x1,x2,x3)
        o, d = test_rays[i]
        r = sp.ray(o,d)

        hit1,a_star1, p_star1 = sp.algebraic_ray_triangle_intersection(r,t)
        hit2,a_star2, p_star2 = sp.moller_trumbore_ray_triangle_intersection(r,t)
        if hit1!=hit2:
            hit_integrity = False

    assert(hit_integrity)
