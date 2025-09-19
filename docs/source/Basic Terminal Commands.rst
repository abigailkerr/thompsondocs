|ico4| Basic Terminal Commands
=================================

.. |ico4| image:: iterm.png
   :height: 2.5ex
   :width: 2.5ex
   :target: https://commons.wikimedia.org/wiki/File:ITerm2_v3.4_icon.png


There are many commands which are most commonly used for both the terminal and the KU Cluster. Commonly used commands are shown below; however, many more commands can be found within the `KU Cluster Wiki`_.

.. _KU Cluster Wiki: https://help.ittc.ku.edu/clusterdocs/helpful_commands/

Navigating Directories
-----------------------

Entering and leaving directories (folders) is done with the ``cd`` command. You can press TAB to quickly fill out paths to a desired directory location. For example,

* ``pwd`` shows the path to your current directory. 
* ``ls`` shows all files and available directories within your current path.
* ``cd`` will return you to the root directory. For the cluster, this is your ``$HOME`` profile.
* ``cd path/to/file`` will take you to some directory. For example, ``cd /home/KUID/work/`` will take you to your ``$WORK`` directory, where ``KUID`` is your KU Username (e.g. ``a123b456``).
* ``cd ..`` returns to the previous directory.

Editing Files
--------------

To edit files, you can use either `vi`_, `emacs`_, or `VSCode`_. It is recommended to either use vim (vi) or emacs unless you are familiar with VSCode.

.. _vi: https://openvim.com
.. _emacs: https://riptutorial.com/emacs
.. _VSCode: https://code.visualstudio.com/download

Using VSCode as a visual guide when navigating the cluster can be extremely helpful. You can download files without typing the entire command, edit files with added navigation and debugging assistance, as well as quickly access files to edit. Steps to implement VSCode for ssh use can be found `here`_.

.. _here: https://code.visualstudio.com/docs/remote/ssh

Copying and Removing
---------------------

To copy or remove files/directories, ``cp`` and ``rm`` are used.

* ``cp path/to/original path/to/copy`` will copy a file to a new path. The path to the copy is required (if you are copying to the same directory, you can simply just type the name of the new copied file instead).
* ``cp -R path/to/original/ path/to/copy/`` will copy a directory to a new path. Similarly to the general ``cp`` command, a new location or name must be specified.
* ``mv path/to/file path/to/destination`` moves the file of interest without copying its contents. 
* ``rm path/to/file`` removes a single file. **This cannot be undone**. Once files are removed, the action is permanent. 
* ``rm -rf path/to/file`` removes a directory **and its included contents**.  

Other Helpful Commands
-----------------------

* ``du -sh path/to/directory/`` displays the amount of memory associated to a directory.
* ``scp KUID@login1.hpc.crc.ku.edu:path/to/file path/to/destination`` will download a file from the Cluster to your computer (where KUID is your KU Username). It is important to ``cd`` to the location you want the file to be downloaded to prior to downloading it from the Cluster itself.

   - ``scp -r KUID@login1.hpc.crc.ku.edu:path/to/file path/to/destination`` will download a directory and its contents (including subdirectories and their associated files). 

* ``stat path/to/file`` displays information including the size, creation date, and modify date for a file.
 
