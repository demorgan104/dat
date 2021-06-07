"""
    Generates a completely functional DAT package
"""
import os
import shutil
from dat.errors.dat_exception import DatException

class NewApi:
    def __init__(self) -> None:
        pass

    def new(self, dest, name, forced=False):
        """
            TBD
        """
        print('Generating a DAT package')
        if not dest:
            if not name:
                raise DatException("Please provide a destination and a name !")
        if name:
            dest = os.path.join(dest, name)

        if not os.path.exists(dest):
            os.mkdir(dest)
        else:
            if forced:
                shutil.rmtree(dest)
                os.mkdir(dest)
            else:
                raise DatException("Destination {} already exists !".format(dest))


        template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates', 'package_template')
        
        for dirpath, dirnames, filenames in os.walk(template_dir):
            print(dirpath)
            print(dirnames)
            print(filenames)
            if not os.path.exists(dirpath) and 'package_template' not in dirpath:
                os.mkdir(dirpath)

        
        #template_elems = ["conf", "doc", "src", "tests"]

        #for elem in template_elems:
            #path = os.path.join(dest, elem)
            #os.mkdir(path)