all:
	qsub no_surf_lab.sh

clean: 
	$(RM) *.lammpstrj *.atoms *.out *.lammps no_surf_lab.sh.* 
