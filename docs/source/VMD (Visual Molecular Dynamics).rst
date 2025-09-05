|ico0| VMD (Visual Molecular Dynamics)
##################################

.. |ico0| image:: molden_images/vmd0.png
   :height: 2.5ex
   :target: https://www.ks.uiuc.edu/Research/vmd/

.. _here:  https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD

.. image:: molden_images/vmd2.png
  :height: 400px
  :align: right

VMD is a tool (similar to :doc:`PyMOL`) to visualize trajectories from simulations. ``.xyz``, ``.gro``, among other types of files can be uploaded quickly to visualize a simulation. You can download VMD and previous versions _`here`.

VMD Basics
===========

.. image:: molden_images/vmd1.png
  :height: 200px
  :align: right

Once VMD is downloaded, the application can be opened. It will open a visualization screen, a configuration menu, and a terminal for importing and viewing the file of interest. To upload a molecule, select the "File" button on the configuration panel and press "New Molecule". The following screen will allow you to upload a molecule, which you can select or type the path accordingly.

.. important::
  Make sure to press the "Load all at once" button to load the simulation quickly. Otherwise, each frame will load individually and could take several minutes to visualize the trajectory.

Once the file is loaded, you can press the play button at the bottom of the VMD Main screen to run the simulation. The scroll "speed" bar will adjust how quickly the trajectory will run through each frame. The "Loop" selection will either allow the system to replay or stop at the end of the trajectory. 

There are key features for VMD which can be used to better visualize the system.

Graphics
---------

Selecting "Graphics" and "Representations" allows for the molecule to be viewed differently. From a system, molecules can be viewed in the "Drawing Method" menu. You can select to view molecules as VDW (Van der Waals, just atoms and no bonds), CPK (Corey–Pauling–Koltun model, aka ball-and-stick), or lines (just lines, no atom spheres) are often used for different molecules. For example, displaying a solvent as lines and the solute as CPK may be of interest for better viewing. There are many other options in the Drawing Method menu selection, but these are most commonly used. The coloring method can change how the molecules are colored, and the material can be changed from the selection menu as well. For some systems, the size of the molecule spheres/bonds, etc. may need to be adjusted. This can be done below the selection pane.

Just above the "Coloring Method" selection window are tabs for each component of the system. A helpful tab to use is the "Periodic" tab, which can display the PBC images respective to the unit cell about the system, in the +/- X, Y, or Z directions. Note that in order to successfully display images, a few commands need to be stated first. Select the VMD termial window and type the following commands to view the PBC cell, **prior** to clicking the Cartesian periodic images on the Graphical Representations screen in VMD.

.. code-block::
   pbc set {x y z} -all # where x, y, and z are the box side lengths (you can find this in your data file from LAMMPS)
   pbc box -center unitcell

If you do not set the box lengths for ``pbc set``, the box cannot be drawn. Once it is drawn, however, you can then select the +/- X, Y, and Z images to appear. For more details on editing and saving visualized trajectories, the following links are recommended.

Recommended Links
-------------------

VMD ``pbc`` commands: http://www.ks.uiuc.edu/Research/vmd/plugins/pbctools/
VMD Rendering Options (for images and movies): 
   * https://rmhartkamp.github.io/Modules/VMDrender/vmdrender.pdf
   * https://www.ks.uiuc.edu/Research/vmd/vmd-1.9/ug/node43.html
