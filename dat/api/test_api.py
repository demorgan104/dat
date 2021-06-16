import shutil
import subprocess
import os
from dat.core.conf_reader import get_package_config
from dat.utils.dat_logger import app_logger
from dat.utils import replacements


class TestApi:
    """
    TBD
    """

    def __init__(self) -> None:
        self.current_dir = os.getcwd()

    @classmethod
    def handle_tmp_folder(cls, location):
        """
        TBD
        """
        if os.path.exists(location):
            shutil.rmtree(location)
        os.mkdir(location)

    def test(self):
        app_logger.info("Testing the package for release !")
        config = get_package_config(os.getcwd())
        dat_tmp_folder = os.path.join(self.current_dir, "_dat_build")
        test_package_conanfile = os.path.join(os.path.dirname(__file__), "..", "conan", "test_package", "conanfile.py")
        test_package_location = os.path.join(dat_tmp_folder, "test_package")
        new_test_conanfile = os.path.join(test_package_location, "conanfile.py")
        self.handle_tmp_folder(test_package_location)
        # Perform conan package usage test
        # Copy the test package into _dat_build
        replace_dict = {
            "name": config["name"],
        }
        replacements.replace_and_create(replace_dict, test_package_conanfile, new_test_conanfile)
        os.chdir(dat_tmp_folder)
        package_id = "{name}/{version}@stable/release".format(
            name=config["name"], version=config["version"]
        )
        cmd = "conan test {} {}".format(test_package_location, package_id)
        try:
            subprocess.run(cmd.split(" "), check=True)
        except subprocess.CalledProcessError:
            app_logger.error("Error executing %s", cmd, exc_info=True)

        # Execute package unit/functional tests