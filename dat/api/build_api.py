import os
import subprocess
import shutil
from dat.core.conf_reader import get_package_config
from dat.conan.conan_handler import generate_conanfile

class BuildApi(object):

    def __init__(self):
        self.current_dir = os.getcwd()


    def build(self, variant):
        print('current path: {}'.format(__file__))
        print('current dir: {}'.format(self.current_dir))
        config = get_package_config(os.getcwd())
        if os.path.exists('_dat_build'):
            shutil.rmtree('_dat_build')
        os.mkdir(
            '_dat_build'
        )
        generate_conanfile(
            self.current_dir,
            config
        )
        os.chdir(
            '_dat_build'
        )
        subprocess.run(
            [
                "conan",
                "install",
                "-if",
                ".",
                "."
            ]
        )
        subprocess.run(
            [
                "conan",
                "build",
                "-bf",
                ".",
                "-if",
                ".",
                "."
            ]
        )
        subprocess.run(
            [
                "conan",
                "export-pkg",
                ".",
                "{name}/{version}".format(
                    name=config['name'],
                    version=config['version']
                ),
                "-f"
            ]
        )

    # Support with statement in the future
    def __enter__(self):
        pass 


    def __exit__(self):
        pass
