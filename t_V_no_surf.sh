#!/bin/sh

#SBATCH -p F72cpu
#SBATCH -N 72
#SBATCH -n 128
#SBATCH -c 72
#SBATCH -t 24:00:00
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-user=naofuji.1220@gmail.com

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

python3 generate.py 
srun lammps < decomp.input
python3 rescale.py > rescale.atoms
srun lammps < rescale.input
