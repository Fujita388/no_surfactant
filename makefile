all:

lab:
	qsub no_surf_lab.sh

issp:
	sbatch no_surf_issp.sh

clean: 
	$(RM) *.lammpstrj *.atoms *.out *.lammps no_surf_lab.sh.* 
