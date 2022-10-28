#!/bin/bash
#PBS -M naofuji.1220@gmail.com
#PBS -m be
#PBS -l nodes=1:ppn=20

cd $PBS_O_WORKDIR

# 20プロセス並列
python3 generate.py
mpirun -np 20 /home/Fujita388/github/lammps/src/lmp_mpi < decomp.input > decomp.out
python3 rescale.py > rescale.atoms
mpirun -np 20 /home/Fujita388/github/lammps/src/lmp_mpi < rescale.input > rescale.out
