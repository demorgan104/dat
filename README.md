# DAT

![logo](img/dat_logo.png)

Accelerate your C/C++ development.

Generate your package:

![dat_new](img/dat_new.gif)

Use it:

![dat_flow](img/dat_flow.gif)



DAT is setting up the following for you:

- a standard repository structure
- the [Conan](https://conan.io/) package flow
- use any build tool you want
- the starter package generated with dat new contains a basic Bazel build with GTest integrated
- release the package in [Artifactory](https://jfrog.com/artifactory/)
- documentation with [Mkdocs](https://www.mkdocs.org/)
- through extensions, testing and running your package (check the extensions folder)

Create your own templates and generate your own packages using DAT.

Although a work in progress, DAT provides already the basics to start using it and benefit from increased development efficiency.

## Write your own templates and use them:

`
    dat new -n <package_name> -t <your_template_file> -d <destination>
`

Check https://github.com/demorgan104/dat-templates.git for samples.

<br/>
<br/>


# Getting started

## Install DAT in your python environment

    Clone DAT:
        git clone https://github.com/demorgan104/dat
        
    Make sure your Python version is 3.9.0

    Create a python virtual environment:
        python -m venv ./venv

    Activate the virtual environment
        Windows:
          venv/Scripts/activate
        Macos:
          source venv/bin/activate

    Install DAT:
        python setup.py install

    Test the setup:
        dat -h


## Using DAT

Typical usage:

- Generate a package:

    `
        dat new -n dat_hello
    `

- Change the directory to your package:

    `
        cd dat_hello
    `
- Build your package:
   
   This step requires the installation of Bazel: https://docs.bazel.build/versions/4.1.0/install.html
   
    `
        dat build
    `

- Test the package:

    `
        dat test
    `

    This test is for both testing that the package can be used by other packages and executing the unit tests.

- Check the documentation:

    `
        dat document
    `

- Run the application (this works for desktop apps only of course):

    `
        dat run
    `

- Releasing to artifactory:

    For this you need to setup an artifactory server. You can use the following repo for the demo: https://github.com/demorgan104/dat-infrastructure

    Clone this repo and navigate to artifactory directory. There you can run:
        `
            docker-compose up
        `

    DAT is for the moment configured to work with that and there is no portable configuration available. Feel free to open a pull request for that or modify the source code :)

    Then you can use:
        `
            dat release
        `


<br/>
<br/>



DAT Commands

NAME|DESCRIPTION
----|-----------
dat new|Create a new ready to use package
dat build|Build a package
dat release|Release a package
dat test|Test your package
dat run|Run your executable
dat document|Check your documentation

<br/>
<br/>
<br/>
<br/>


# DAT Repositories

NAME|DESCRIPTION|LINK
----|-----------|----
dat|Dat main repository|https://github.com/demorgan104/dat
dat-infrastructure|Dat package infrastructure repo|https://github.com/demorgan104/dat-infrastructure
dat-templates|Templates for DAT|https://github.com/demorgan104/dat-templates.git

