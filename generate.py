import random
import numpy as np
from math import cos, sin, sqrt


random.seed(101)


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        v0 = 1.0
        z = random.random()*2.0-1
        s = random.random()*3.14*2.0
        self.vx = v0*sqrt(1.0-z**2)*cos(s)
        self.vy = v0*sqrt(1.0-z**2)*sin(s)
        self.vz = v0*z


#密度から格子数を計算　L: シミュレーションボックス　rho: 密度
def get_lattice_number(L, rho):
    m = np.floor((L**3 * rho / 4.0)**(1.0 / 3.0))
    drho1 = np.abs(4.0 * m **3 / L**3 - rho)
    drho2 = np.abs(4.0 * (m + 1)**3 / L**3 - rho)
    if drho1 < drho2:
        return m
    else:
        return m + 1


def add_ball(atoms, l, rho):
    m = int(get_lattice_number(l, rho))  #格子数
    s = 1.7     #単位格子の一辺の長さ
    h = 0.5 * s
    for ix in range(0, m):   #原子数は8倍になる
        for iy in range(0, m):
            for iz in range(0, m):
                x = ix * s
                y = iy * s
                z = iz * s
                atoms.append(Atom(x, y, z))
                atoms.append(Atom(x, y+h, z+h))
                atoms.append(Atom(x+h, y, z+h))
                atoms.append(Atom(x+h, y+h, z))


def save_file(filename, atoms):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("0.00 119.00 xlo xhi\n")
        f.write("0.00 119.00 ylo yhi\n")
        f.write("0.00 119.00 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))


atoms = []

add_ball(atoms, 119, 0.8)

save_file("decomp.atoms", atoms)
