"""
    TBD
"""
import os
import subprocess
from dat.core.conf_reader import get_package_config
from dat.conan.conan_handler import generate_conanfile
from dat.utils.dat_logger import app_logger
from dat.utils import utils
from dat.errors.dat_exception import DatException


class BuildApi:
    """
    TBD
    """

    def __init__(self):
        self.current_dir = os.getcwd()

    # pylint: disable=R0914, W0613
    @classmethod
    def execute_conan_steps(cls, dat_tmp, generated_conan_file, config):
        """
        TBD
        """
        dat_tmp_tmp = os.path.join(dat_tmp, "tmp")
        source_folder = os.path.join(dat_tmp, "source")
        install_folder = os.path.join(dat_tmp_tmp, "install")
        build_folder = os.path.join(dat_tmp_tmp, "build")
        package_folder = os.path.join(dat_tmp_tmp, "package")
        source_folder_flag = "--source-folder={}".format(source_folder)
        source_folder_flag_package = "--source-folder={}".format(build_folder)
        install_folder_flag = "--install-folder={}".format(install_folder)
        build_folder_flag = "--build-folder={}".format(build_folder)
        package_folder_flag = "--package-folder={}".format(package_folder)
        install_cmd = "conan install {conan_file} {install_folder_flag}".format(
            conan_file=generated_conan_file, install_folder_flag=install_folder_flag
        )
        # pylint: disable=C0301
        build_cmd = "conan build {conan_file} {source_folder_flag} {install_folder_flag} {build_folder_flag}".format(
            conan_file=generated_conan_file,
            source_folder_flag=source_folder_flag,
            install_folder_flag=install_folder_flag,
            build_folder_flag=build_folder_flag,
        )
        # pylint: disable=C0301
        package_cmd = "conan package {conan_file} {source_folder_flag} {install_folder_flag} {build_folder_flag} {package_folder_flag}".format(
            conan_file=generated_conan_file,
            source_folder_flag=source_folder_flag_package,
            install_folder_flag=install_folder_flag,
            build_folder_flag=build_folder_flag,
            package_folder_flag=package_folder_flag,
        )
        # pylint: disable=C0301
        export_package_cmd = "conan export-pkg {conan_file} {pkg_id} {source_folder_flag} {install_folder_flag} {build_folder_flag} --force".format(
            conan_file=generated_conan_file,
            source_folder_flag=source_folder_flag_package,
            install_folder_flag=install_folder_flag,
            build_folder_flag=build_folder_flag,
            pkg_id="stable/release",
        )

        cmd_flow = [install_cmd, build_cmd, package_cmd, export_package_cmd]

        for cmd in cmd_flow:
            app_logger.debug('Executing cmd "%s"', cmd)
            try:
                subprocess.run(cmd.split(" "), check=True)
            except subprocess.CalledProcessError as error:
                app_logger.error("Error executing %s", cmd, exc_info=True)
                raise DatException(error) from error

    def build(self, variant):
        """
        TBD
        """
        config = get_package_config(os.getcwd())
        dat_tmp_folder = os.path.join(self.current_dir, "_dat_build")
        utils.handle_tmp_folder(dat_tmp_folder)
        generated_conan_file = generate_conanfile(dat_tmp_folder, config)
        self.execute_conan_steps(dat_tmp_folder, generated_conan_file, config)
