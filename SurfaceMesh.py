from HyperPanel import HyperPanel
from Vect3D import *


class SurfaceMesh:

    def __init__(self, u, v, sde):
        self.u = len(u)
        self.v = len(v)

        self.U = u
        self.V = v

        self.mesh = [] * self.u * self.v

        self.side = sde

    def get_point(self, ui, vi):
        r0 = c0 = 0

        for i, elem in enumerate(self.U):
            if elem >= ui:
                c0 = i - 1
                break

        for i, elem in enumerate(self.V):
            if elem >= vi:
                r0 = i - 1
                break

        print("r0: %s, c0: %s" % r0, c0)

        uu = float((ui - self.U[c0]) / (self.U[c0 + 1] - self.U[c0]) * 2 - 1)
        vv = float((vi - self.V[r0]) / (self.V[r0 + 1] - self.V[r0]) * 2 - 1)











