#decomp.atomsとdecomp.lammpstrjを読み込んで座標を1.05倍にし、rescale.atomsをはく

class Atoms:
    def __init__(self, atoms_id, atoms_type, x, y, z, vx, vy, vz):
        self.atoms_id = atoms_id
        self.type = atoms_type
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz


def readdump(atoms, dump_file, scale):
    with open(dump_file, "r") as f:
        dump_data = f.readlines()
    step = []  #ダンプファイルにおけるstepの始まりのインデックスの配列
    for i, line in enumerate(dump_data):
        if "ITEM: TIMESTEP" in line:
            step.append(i)
    l = dump_data[step[-1]+5]  
    rescaled_L = float(l.split()[1]) * scale  #リスケールされたシミュレーションボックスのサイズ
    num_atoms = int(dump_data[3])  #atomの数
    for i in range(num_atoms):
        position = dump_data[step[-1]+9+i]  #最後のグループの座標dataの先頭
        atoms_id = int(position.split()[0])
        atoms_type = int(position.split()[1])
        x = float(position.split()[2]) * scale
        y = float(position.split()[3]) * scale
        z = float(position.split()[4]) * scale
        vx = float(position.split()[5])
        vy = float(position.split()[6])
        vz = float(position.split()[7])
        atoms.append(Atoms(atoms_id, atoms_type, x, y, z, vx, vy, vz))
    return rescaled_L


def save_file(atoms, rescaled_L):
    print("Position Data\n")
    print("{} atoms".format(len(atoms)))
    print("1 atom types\n")
    print("0.00 {} xlo xhi".format(rescaled_L))
    print("0.00 {} ylo yhi".format(rescaled_L))
    print("0.00 {} zlo zhi\n".format(rescaled_L))
    print("Atoms\n")
    for i, a in enumerate(atoms):
        print("{} {} {} {} {}".format(a.atoms_id, a.type, a.x, a.y, a.z))
    print("\n")
    print("Velocities\n")
    for i, a in enumerate(atoms):
        print("{} {} {} {}".format(a.atoms_id, a.vx, a.vy, a.vz))


atoms = []
rescaled_L = readdump(atoms, "decomp.lammpstrj", 1.05)
save_file(atoms, rescaled_L)
