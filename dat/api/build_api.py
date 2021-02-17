import subprocess

class BuildApi(object):

    def build(self, variant):
        subprocess.run(
            [
                "conan",
                "install",
                "-if",
                "dat_build",
                "."
            ]
        )
        subprocess.run(
            [
                "conan",
                "build",
                "-bf",
                "dat_build",
                "-if",
                "dat_build",
                "."
            ]
        )

    # Support with statement in the future
    def __enter__(self):
        pass 


    def __exit__(self):
        pass
