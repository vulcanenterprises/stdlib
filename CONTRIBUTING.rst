################################
Contributing to Standard Library
################################

Fork Process
------------
1. Visit https://github.com/vulcanenterprises/stdlib
2. Click Fork in the top right
3. Choose your personal profile

You've now got a forked version of this repository

** NOTE:
    * You'll still need to clone your forked repo
    * Once you've cloned your forked repo, you'll need to add upstream remotes

To check your git remotes::

    $ git remote -v

To add a new remote::

    $ git remote add <NAME> <URL>
    $ git remote add upstream git@github.com:vulcanenterprises/stdlib.git

Pull Request Process
^^^^^^^^^^^^^^^^^^^^
1. Ensure you either list the dependencies explicitly or ensure there are none
2. Update the README.md if any changes were made to the interface, or key applications
3. Create a pull request


Setting Up a Development Environment
------------------------------------

Installing pyenv on Linux / Mac
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pyenv allows you to install different versions of python and create virtual environments with those versions

Install::

    $ curl https://pyenv.run | bash

The curl command will install pyenv and pyenv-virtualenv.
We will use these to install python 3.7.0 and create a virtual environment

To update pyenv run::

    $ pyenv update

After pyenv installation you'll need to add::

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"


to your bash profile. You'll only ever have to do this once.

Restart your shell::

    $ exec "$SHELL"


Linux Notes
***********

On linux you'll need these extra packages installed.

CentOS::

    $ yum install gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
    openldap-devel libffi-devel  -y

Creating Your virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install Python 3.7.0
********************


Install::

    pyenv install 3.7.0

Create your stdlib virtual environment::

    pyenv virtualenv 3.7.0 stdlib

Activate and use your virtual environment::

    pyenv activate stdlib

** NOTE:
    * To deactivate a virtual environment use::

        pyenv deactivate

Install the projects requirements via pip::

    pip3 install -U pip
    pip3 install -U setuptools
    pip3 install -U wheel
    pip3 install -r requirements

Finally install stdlib in development mode from the root stdlib::

    $ cd stdlib
    pip3 install -e .

