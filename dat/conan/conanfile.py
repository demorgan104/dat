import os
from conans import ConanFile, tools



class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"


    def source(self):
        #self.run("git clone https://github.com/demorgan104/hello")
        pass


    def build(self):
        conan_dir = os.getcwd()
        with tools.chdir(os.path.join(conan_dir, '..')):
            # create venv
            self.run("python -m venv ./venv")
            # install scons
            self.run("pip install scons")
            # activate venv and run scons
            self.run("source ./venv/bin/activate")
            self.run("scons --build-workarea={}".format(conan_dir))
        

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy(".*", dst="bin", src="bin")

    def package_info(self):
        self.cpp_info.libs = ["hello"]

