|ico4| GitHub
#################

.. |ico4| image:: github.png
   :height: 2.5ex
   :width: 2.5ex
   :target: https://github.com/

Syncing a VS Code Remote SSH Workspace with GitHub
==================================================

.. note::

This page was written by Elizabeth (Elle) R. Bartlett.

This guide assumes you are connected to a remote cluster using VS Code
Remote SSH and want to synchronize files with a GitHub repository.

1. Verify Git Is Available on the Cluster
-----------------------------------------

Open a terminal in VS Code and run:

.. code:: bash

   git --version

--------------

2. Navigate to Your Project Directory
-------------------------------------

.. code:: bash

   cd /path/to/project

Check whether it is already a Git repository:

.. code:: bash

   git status

If you receive:

.. code:: text

   fatal: not a git repository

initialize a repository:

.. code:: bash

   git init

--------------

3. Configure Git (First Time Only)
----------------------------------

Check your Git configuration:

.. code:: bash

   git config --global user.name
   git config --global user.email

If necessary, set them:

.. code:: bash

   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"

Use the email associated with your GitHub account.


--------------

4. Create a GitHub Repository
-----------------------------

1. Log in to GitHub.
2. Click **New Repository**.
3. Enter a repository name.
4. If your project already contains files, do **not** initialize the
   repository with a README.
5. Create the repository.

GitHub will display a repository URL such as:

.. code:: text

   git@github.com:username/repository.git

--------------

5. Set Up SSH Authentication
----------------------------

Check for an existing SSH key:

.. code:: bash

   ls ~/.ssh

Look for files such as:
.. code:: text

   id_ed25519
   id_ed25519.pub

If no key exists, create one:

.. code:: bash

   ssh-keygen -t ed25519 -C "your_email@example.com"

Accept the defaults unless you have a reason to change them.

--------------

6. Add the SSH Key to GitHub
----------------------------

Display the public key:

.. code:: bash

   cat ~/.ssh/id_ed25519.pub

Copy the entire output.

On GitHub:

1. Go to **Settings**.
2. Select **SSH and GPG keys**.
3. Click **New SSH key**.
4. Paste the key.
5. Save.

--------------

7. Test GitHub Authentication
-----------------------------

.. code:: bash

   ssh -T git@github.com

Expected output:

.. code:: text

   Hi username! You've successfully authenticated, but GitHub does not provide shell access.

This confirms that SSH authentication is working correctly.

--------------

8. Connect the Local Repository to GitHub
-----------------------------------------

Add the remote repository:

.. code:: bash

   git remote add origin git@github.com:username/repository.git


Verify:

.. code:: bash

   git remote -v

--------------

9. Create a .gitignore File
---------------------------

Create a ``.gitignore`` file in the repository root:

.. code:: bash

   touch .gitignore

Example contents:

.. code:: text

   # Python
   __pycache__/
   *.pyc

   # VS Code
   .vscode/

   # Logs
   *.log
   *.out

   # Slurm
   slurm-*.out

   # Simulation outputs
   *.traj
   *.dcd
   *.lammpstrj

   # Temporary files
   *.tmp

   #Entire directories
   logs/
   RESTART/

Commit the ``.gitignore`` file:

.. code:: bash

   git add .gitignore
   git commit -m "Add gitignore"

--------------

10. Add Files
-------------

Stage all files recursively:

.. code:: bash

   git add .

Review staged changes:

.. code:: bash

   git status

--------------

11. Commit Changes
------------------

.. code:: bash

   git commit -m "Initial commit"

--------------

12. Push to GitHub
------------------

First push:

.. code:: bash

   git push -u origin main

The ``-u`` option sets the upstream branch so future pushes can be
performed with:

.. code:: bash

   git push

--------------

Troubleshooting: “Can’t push refs to remote”
--------------------------------------------

If VS Code reports:

.. code:: text

   Can't push refs to remote. Try running "Pull" first to integrate your changes.

the GitHub repository likely contains commits that your local repository
does not have (for example, a README).

Try:

.. code:: bash

   git pull origin main --allow-unrelated-histories

Resolve any merge conflicts, then:

.. code:: bash

   git push -u origin main

If the GitHub repository contains no important content and you want to
overwrite it with your local repository:

.. code:: bash

   git push -u origin main --force

Use ``--force`` with caution.

--------------

Daily Workflow
--------------

After making changes:

.. code:: bash

   git status
   git add .
   git commit -m "Describe changes"
   git push

To obtain updates from GitHub:

.. code:: bash

   git pull

Helpful commands
----------------

To run a quicker status check if you have many untracked files in your
working directory (large data files, trajectories, etc.), use the ``-uno`` or ``-ufalse`` option with ``git status`` to ignore any untracked files

To learn about the options for any command, run

.. code:: bash

   git help <command>
