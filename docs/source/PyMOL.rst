|ico1| PyMOL
===============

.. |ico1| image:: icon2.png
   :height: 2.5ex
   :width: 2.5ex
   :target: https://sourceforge.net/p/pymol/code/HEAD/tree/trunk/pymol/data/pymol/icons/icon2.svg

.. note::

   This page is adapted from the group document, "PyMOL Intro", written by Elle Bartlett. PyMOL logo: https://sourceforge.net/p/pymol/code/HEAD/tree/trunk/pymol/data/pymol/icons/icon2.svg.

.. _Installation:

Installation
-------------

* At https://pymol.org/, click download now. Click on the corresponding installation package for your device. Follow the corresponding instructions. Save the license file anywhere on your device (email Dr. Thompson or ask one of the group members for the latest PyMOL license). When you open PyMOL, you will see a popup called "activation". Click browse for license file and navigate to wherever you have saved it. 

.. _Basics GUI:

Basics: GUI
-------------

Opening a Trajectory
`````````````````````

* Opening a trajectory or visualization state can be done in three separate ways:
	* You can open a file via File -> Open and select the file you want to view. 
	* Drag and drop file into PyMOL itself.
	* Use the command ``load_traj`` (see https://pymolwiki.org/index.php/Load_traj). 

.. note::

   Large files may take some time to load. Accepted file types are given in https://pymol.org/dokuwiki/doku.php?id=format. 

.. note::
   Any dcd trajectories require loading of a topology file, commonly .pbd or .cif. For .xyz files, single frames can be loaded as a topology file as well.

Working with an Object
`````````````````````````

* When making a selection:
	
	* ``select name X`` where ``X`` is your naming convention in the trajectory.
	* You can also select with the mouse and use the right margins to adjustcolors or labels.

* Changing representation on right panel:
	
	* There are rows that exist within the panel for each loaded state in PyMOL. You can use the "all" section to change the visualization, color, labels, etc. for all species in the system. As more trajectories are added, specific sites can be rendered differently than others. 
	* S (show) -> as -> (select options here)
	* C (color) -> (select color palette here)

Common Commands
`````````````````

* ``hide lines`` hides all bonds connecting atoms
* ``show sticks`` shows bonds as sticks (easier to see bonds explicitly)
* ``show spheres`` shows all atoms as spheres
* ``set stick_radius, 0.1, (all)`` sets the stick radius
* ``set sphere_scale, 0.25, (all)`` sets the sphere radius

Saving Images
```````````````

* On the top toolbar, within File. You can select "Export Image As" or "Export Movie" for frame images or trajectories, respectively. 
* Draw/Ray on the top of the right margin for specifications of specific images.
* Display on the top toolbar has options for resolution, background, etc.

Scripting
```````````

* Command ``run path/to/script/example.py`` will run a script of interest.
* An example script can be found within Elle's cluster profile: ``/kuhpc/work/thompson/pymol/``. 
* For an online example: https://pymolwiki.org/index.php/DrawBoundingBox

 
