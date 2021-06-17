# DAT

![logo](logos/dat_logo.png)

Generate ready to use C/C++ packages.

Just start writing your source code afterwards. The package infrastructure will already be ready for you.

# Getting started

## Install DAT in your python environment

    Clone DAT:
        git clone https://github.com/demorgan104/dat
        
    Create a python virtual environment:
        python -m venv ./venv
        
    Activate the virtual environment
        Windows: 
          venv/Source/activate
        Macos: 
          source venv/bin/activate
          
    Install DAT:
        python setup.py install

    Test the setup:
        dat -h

## Using DAT

DAT Commands

NAME|DESCRIPTION
----|-----------
dat new|Create a new ready to use package
dat build|Build a package
dat release|Release a package
dat test|Test your package 




# DAT Repositories

NAME|DESCRIPTION|LINK
----|-----------|----
dat|Dat main repository|https://github.com/demorgan104/dat
dat-infrastructure|Dat package infrastructure repo|https://github.com/demorgan104/dat-infrastructure
dat-website|Dat website|https://github.com/demorgan104/dat-website
hello|Sample DAT package|https://github.com/demorgan104/hello
world|Sample DAT package|https://github.com/demorgan104/world
hello-world|Sample DAT package that uses hello and world package|https://github.com/demorgan104/hello-world
package-template|DAT Package template used by DAT package generator|https://github.com/demorgan104/package-template
platforms|DAT platforms|https://github.com/demorgan104/platforms

