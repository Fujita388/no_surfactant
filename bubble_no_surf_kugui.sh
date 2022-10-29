#!/bin/bash

#PBS -q F16cpu
#PBS -l select=16:ncpus=128:mpiprocs=128:ompthreads=1
#PBS -l walltime=24:00:00
#PBS -N bubble_no_surf

module load intel intel-mpi
python3 generate.py
mpiexec -n 128 ../../lammps/src/lmp_mpi < decomp.input > ./decomp.log 2>&1
python3 rescale.py > rescale.atoms
mpiexec -n 128 ../../lammps/src/lmp_mpi < rescale.input > ./rescale.log 2>&1
