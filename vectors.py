import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def module(self):
        return (self.x**2 + self.y**2)**(0.5)
    
    def scalar_prod(self, n =1):
        self.x *= n
        self.y *= n

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    @classmethod
    def suma(cls, vector_1, vector_2):
        return cls(vector_1.x + vector_2.x, vector_1.y + vector_2.y)
    
    @classmethod
    def substract(cls, vector_1, vector_2):
        return cls(vector_1.x - vector_2.x, vector_1.y - vector_2.y)
    
    @staticmethod
    def dot_product(vector_1, vector_2):
        return vector_1.x*vector_2.x + vector_1.y*vector_2.y
        
    @classmethod
    def distance(cls, vector_1, vector_2):
        return cls.substract(vector_1, vector_2).module()
    
    def extend_to_3D(self, z=0):
        return Vector3D(self.x, self.y, z)

    
class Vector3D(Vector2D):
    
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z = z
    
    def __str__(self):
        return super().__str__()[:-1] + ", {})".format(self.z)
        
    def module(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def scalar_prod(self, n):
        super().scalar_prod(n)
        self.z *= n
    
    @classmethod
    def suma(cls,u,v):
        return cls(u.x+v.x, u.y+v.y, u.z+v.z)
    
    @classmethod
    def substract(cls,u,v):
        return cls(u.x-v.x, u.y-v.y, u.z-v.z)
    
    @staticmethod
    def dot_product(u,v):
        return super().dot_product(u,v) + u.z*v.z
    
    @staticmethod
    def distance(u,v):
        return Vector3D.substract(u,v).module()
    
    @classmethod
    def zero(cls):
        return cls(0,0,0)
    
    @classmethod
    def horizontal(cls):
        return cls(1,0,0)
    
    @classmethod
    def vertical(cls):
        return cls(0,1,0)
    
    @classmethod
    def forward(cls):
        return cls(0,0,1)
    
    
    
    
    
    