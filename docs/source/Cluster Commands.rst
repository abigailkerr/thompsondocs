Cluster Commands
=================

.. note::

   This page is adapted from the group document, "Getting Access to the KU Community Cluster", written by Dr. Ashley Borkowski.

While the commands for the terminal are still applicable for the Cluster, there exist unique commands (and clever devices) which are only accessable when you are online.

.. _Basic Commands:

Basic Commands
---------------

Some of the most used commands for the cluster are:

* ``sbatch name.sh`` submits a job called "name" to the cluster. ``.sh`` files are known as SLURM scripts, and are what tells the cluster what job(s) to run.
* ``squeue -u KUID`` shows what jobs you currently have running, where KUID is your KU Username.
* ``scancel JOBID`` cancels a job for the given JOBID. Job IDs are shown when a job is submitted, and when viewing the queue. 
* ``sshare`` shows your FairShare score. The FairShare describes the priority of your jobs to ensure that the cluster is shared fairly amongst the KU community. As you submit more jobs, your weekly FairShare will decrease. This implies that the priority listing for submitted jobs will adjust accordingly. Therefore, someone who has a high FairShare score will have a much higher priority for submitted jobs to run.
* ``crctool`` shows the storage available within your cluster profile, along with how much storage you have used specifically. If you use all the storage available, you will receive an automatic email from the cluster and will need to clear out space. 

.. _Modules on the Cluster:

Modules on the Cluster
----------------------

* ``module avail`` shows the available modules within the Cluster.
* ``module purge`` clears all the loaded modules within your current profile. Unless you load modules within your ``.bash_profile`` (more on this later), modules are not automatically loaded upon login.
* ``module list`` shows the loaded modules in your current profile.
* ``module load <modulename>`` loads in the desired module (replace ``<modulename>`` with the module from the list, e.g. ``module load grace``).

.. _Editing Your .bash_profile:

Editing Your .bash_profile
--------------------------- 

* Enter your ``$HOME`` directory (``cd``).
* Using ``vi``, enter your ``.bash_profile`` (``vi .bash_profile``). Enter insert mode by pressing ``i``. 
* Type in the module load commands and specify what modules to load upon login.

	* Recommended modules are (but not limited to):

		* ``module load grace`` (plotting software, XMGrace)
		* ``module load vmd`` (Visual Molecular Dynamics, to visualize simulations)
		* When you are finished adding modules, press ESC and type ``:wq!``. This writes and saves the bash profile.

	* It is recommended to load python via Conda environment within your ``.bash_profile``. The steps are as follows:

		1. Login to the Cluster. 
		2. Within your ``$HOME`` directory, type the following commands: ``module load conda``
		3. ``conda create -n NAME python=VERSION`` (current version is ``python=3.11``. It is recommended you give the name something you will remember, such as ``python3-11``).
		4. Enter your bash profile, ``vi .bash_profile`` and toggle insert mode with ``i``.
		5. Within the module commands, type ``module load conda``.
		6. ``conda activate NAME``
		7. Exit your bash profile by pressing ESC and typing ``:wq!``. 
		8. Make sure that you source your bash profile with the command ``source .bash_profile`` before logging out. This will make sure to load and activate your conda environment for every time you enter the Cluster.
		9. To add packages to your python profile, type ``conda install PACKAGE``, where ``PACKAGE`` is the package of interest. For example, ``conda install numpy`` adds numpy to your environment. 

* Once modules are loaded and the bash profile is saved, you can source the profile with ``source .bash_profile`` to save changes and allow for the commands to run each time you enter the Cluster. 

.. _Creating Alias Commands:

Creating Alias Commands
------------------------

When **off** the Cluster
``````````````````````````

To add an alias on your home device (and **not** on the cluster), the following commands are used (Mac specific):

1. Open a terminal and enter your bash profile: ``vi .bash_profile``
2. Enter insert mode (``i``) and enter the aliases you want for your terminal. It is recommended to have an alias for logging onto the cluster:

	* ``alias *your initials here*=‘ssh -XY username@hpc.crc.ku.edu’``

3. Press ESC and type ``:wq!`` to save your bash profile. 
4. Type ``source .bash_profile`` to add the alias to your computer. Exit and reopen the terminal, and type in your alias. You should be prompted to enter your password and then connect to the cluster.

When **on** the Cluster
``````````````````````````

Aliases are located in the same ``$HOME`` directory bash profile as modules. 

1. When you are editing your ``.bash_profile``, the following commands are helpful:

	* ``alias queue=‘squeue -u username’`` (allows you to type ``queue`` to see what jobs you have submitted)
	* ``alias pgi=‘module load compiler/pgi/19’`` (for running Fortran code)
	* ``alias pgi=‘module load compiler/gcc/8.3’`` (to switch back to gcc for running XMGrace)
	* ``alias watch=‘watch -n 5 squeue -u username’`` (allows you to type ``watch`` to watch the queue with 5 second updates to see when your jobs complete)

.. note::
	If you use the ``watch`` alias, make sure to open a new tab on your terminal and login to the cluster. When the ``watch`` command is used, that entire terminal tab is used solely for viewing the queue.

2. Save and close the file (ESC + ``:wq!`` for vi users)
3. Source the profile (``source .bash_profile``) 
