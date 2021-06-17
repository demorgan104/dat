from conans import ConanFile
import os


class DatPackageTester(ConanFile):
    # TBD settings = "os", "compiler", "build_type", "arch", "os_build", "arch_build"
    settings = "os", "arch", "compiler", "build_type"

    def build(self):
        self.output.info("Building the test package !")
        content_folder = os.path.join(self.deps_cpp_info["<$name>"].rootpath, "content")
        if os.path.exists(content_folder):
            self.output.success("I could find the package <$name> content folder !")
            for file in os.listdir(content_folder):
                self.output.success("File found {}".format(file))
        self.output.info("Done")

    def imports(self):
        pass

    def test(self):
        self.output.info("Executing the test package test method !")
        self.output.info("Done")
