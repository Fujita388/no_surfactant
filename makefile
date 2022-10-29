all:

lab:
	qsub bubble_no_surf_lab.sh

issp:
	sbatch bubble_no_surf_ohtaka.sh

kugui:
	qsub bubble_no_surf_kugui.sh

clean: 
	$(RM) *.lammpstrj *.atoms *.out *.lammps bubble_no_surf.* 
