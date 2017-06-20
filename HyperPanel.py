from Vect3D import *
import numpy as np

class HyperPanel:

    a0 = Vect3D()
    a1 = Vect3D()
    a2 = Vect3D()
    a3 = Vect3D()

    def __init__(self, v0, v1, v2, v3):
        self.a0.x = 0.25 * (v0.x + v1.x + v3.x + v2.x)
        self.a1.x = 0.25 * (-v0.x + v1.x - v3.x + v2.x)
        self.a2.x = 0.25 * (-v0.x - v1.x + v3.x + v2.x)
        self.a3.x = 0.25 * (v0.x - v1.x - v3.x + v2.x)

        self.a0.y = 0.25 * (v0.y + v1.y + v3.y + v2.y)
        self.a1.y = 0.25 * (-v0.y + v1.y - v3.y + v2.y)
        self.a2.y = 0.25 * (-v0.y - v1.y + v3.y + v2.y)
        self.a3.y = 0.25 * (v0.y - v1.y - v3.y + v2.y)

        self.a0.z = 0.25 * (v0.z + v1.z + v3.z + v2.z)
        self.a1.z = 0.25 * (-v0.z + v1.z - v3.z + v2.z)
        self.a2.z = 0.25 * (-v0.z - v1.z + v3.z + v2.z)
        self.a3.z = 0.25 * (v0.z - v1.z - v3.z + v2.z)

    def get_panel_point_uv(self, u, v):
        point = Vect3D()

        point.x = self.a0.x + self.a1.x * u + self.a2.x * v + self.a3.x * u * v
        point.y = self.a0.y + self.a1.y * u + self.a2.y * v + self.a3.y * u * v
        point.z = self.a0.z + self.a1.z * u + self.a2.z * v + self.a3.z * u * v

        return point

    def get_panel_point(self, x, y):
        point = Vect3D()

        return point

    # u, v point position: u=v=0 for middle of panel
    def get_panel_normal(self, u, v):
        dp1 = Vect3D()
        dp2 = Vect3D()

        dp1.x = self.a1.x + self.a3.x * v
        dp1.y = self.a1.y + self.a3.y * v
        dp1.z = self.a1.z + self.a3.z * v

        dp2.x = self.a2.x + self.a3.x * u
        dp2.y = self.a2.y + self.a3.y * u
        dp2.z = self.a2.z + self.a3.z * u

        res = dp1.cross(dp2)
        res = res.normalize()

        return res
# v:
#   4___3
#   |___|
#   1   2

v0 = Vect3D(0,0,0)
v1 = Vect3D(1,0,0)
v2 = Vect3D(2,1,1)
v3 = Vect3D(1,2,1)


hp = HyperPanel(v0, v1, v2, v3)

print(hp.get_panel_point_uv(0.4244711851623297, 0.5253720071346776))

x = 1.1
y = 0.3
p = [x, y]

p1 = [(v1.x + v0.x) / 2, (v1.y + v0.y) / 2]
p2 = [(v3.x + v2.x) / 2, (v3.y + v2.y) / 2]
p3 = [v1.x, v1.y]
p4 = [v2.x, v2.y]

d = np.linalg.norm(np.cross(np.subtract(p2, p1), np.subtract(p1, p))) / np.linalg.norm(np.subtract(p2, p1))
e = np.linalg.norm(np.cross(np.subtract(p3, p2), np.subtract(p2, p))) / np.linalg.norm(np.subtract(p3, p2))

#############################################

p1 = [(v3.x + v0.x) / 2, (v3.y + v0.y) / 2]
p2 = [(v2.x + v1.x) / 2, (v2.y + v1.y) / 2]
p3 = [v0.x, v0.y]
p4 = [v1.x, v1.y]


f = np.linalg.norm(np.cross(np.subtract(p2, p1), np.subtract(p1, p))) / np.linalg.norm(np.subtract(p2, p1))
g = np.linalg.norm(np.cross(np.subtract(p3, p2), np.subtract(p2, p))) / np.linalg.norm(np.subtract(p3, p2))



print(d)
print(e)
print(f)
print(g)
print(d/(d+e))
print( f/(f+g))

print(hp.get_panel_point_uv(0,0))


#e = norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)
#np.linalg.norm(np.cross())


