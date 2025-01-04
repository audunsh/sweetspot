import numpy as np
class ray():
    """
    A *ray* $R$ in three-dimensional space ( $\mathbb{R}^3$ ).

    Author: Audun Skau Hansen (audunsh4@gmail.com), 2022 

    Defined as the set of all points $\mathbf{P}$  on a line 
    segment extending to infinity from the cartesian origin 
    vector $\mathbf{O}$ in the normalized *direction* $\mathbf{D}$:
    $$ \mathbf{P} = \mathbf{O} + a \mathbf{D},  \tag{1} $$
    where $a$ is a real, positive number.

    | Arguments      | Description |
    | ----------- | ----------- |
    | origin     | a 3-component numpy-array defining the rays origin   |
    | direction   | a 3-component numpy array defining the direction of the ray   (will be normalized automatically)  |

    """
    def __init__(self, origin:np.ndarray, direction:np.ndarray)->None:
        self.origin = origin
        
        # note that direction is automatically normalized
        self.direction = direction/np.dot(direction, direction)**.5
        
    def get_point_at(self, a: float)->np.ndarray:
        """
        Returns the point:

        $$\mathbf{P}(a) = \mathbf{O} + a \mathbf{D}$$
        
        """
        assert(a>=0), "Requested point is outside ray"
        return self.origin + self.direction*a
        
class triangle():
    """
    A triangle in three-dimensional space ( $\mathbb{R}^3$ ).

    Author: Audun Skau Hansen (audunsh4@gmail.com), 2022

    | Arguments      | Description |
    | ----------- | ----------- |
    | x1,x2,x3     |  3-component numpy-arrays defining the vertices of the triangle   |
   
    """
    def __init__(self, x1:np.ndarray, x2:np.ndarray, x3:np.ndarray):
        self.X = [x1,x2,x3]
        
    def compute_norm(self):
        """
        computes the norm (normalized) of the triangle
        """
        n = np.cross(self.X[0]- self.X[1], self.X[0]-self.X[2])
        return n/np.dot(n,n)**.5
    
    def compute_distance_to_origin(self)->float:
        """
        Compute distance from (0,0,0) to the plane spanned by the triangle.
        """
        return self.compute_norm().dot(self.X[0])
    
    def compute_edge_vector(self,i,j)->np.ndarray:
        """
        Computes the edge-vector between vertex $i$ and $j$.
        """
        return self.X[i] - self.X[j]
    
    def compute_area(self, points = None)->np.ndarray:
        """
        Computes the area of the triangle.
        """
        if points is None:
            points = self.X
            
        A_ = np.cross(points[1]-points[0], points[2]-points[0])
        return .5*np.dot(A_, A_)**.5
        
    
    def compute_barycentric_coordinates_area(self, point)->np.ndarray:
        """
        Compute the barycentric coordinates of point,
        assuming it is on the plane spanne by triangle
        using the area method
        [https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Barycentric_coordinates_on_triangles]
        """
        x1,x2,x3 = self.X
        
        W  = self.compute_area()
        u1 = self.compute_area(points = [x1,x2,point])/W
        u2 = self.compute_area(points = [x2,x3,point])/W
        u3 = 1-u1-u2
        #w3 = self.compute_area(points = [x1,x2,point])
        return np.array([u1,u2,u3])
    
    def compute_barycentric_coordinates(self, point)->np.ndarray:
        """
        Compute the barycentric coordinates of point,
        assuming it is on the plane spanned by triangle
        using Cramer's rule 
        [http://lavalle.pl/vr/node206.html]
        """
        x1,x2,x3 = self.X
        e1,e2 = x2-x1, x3-x1
        w = point-x1
        
        # compute matrix elements
        d00 = e1.dot(e1)
        d01 = e1.dot(e2)
        d02 = e1.dot(w)
        d11 = e2.dot(e2)
        d12 = e2.dot(w)
        
        det = 1/(d00*d11 - d01*d01)
        
        u2 = det*(d00*d12 - d01*d02)
        u1 = det*(d11*d02 - d01*d12)
        u0 = 1-u2-u1
        return np.array([u0,u1,u2])
        
        
    
    def get_corner(self, i)->np.ndarray:
        """
        Returns the corner $i$.
        """
        return self.X[i]
