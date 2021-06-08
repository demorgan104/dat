"""
    Configuration reader for DAT
"""
import os
import yaml
from dat.errors.dat_exception import DatException
from dat.utils.dat_logger import app_logger


def get_package_config(package_location):
    """
    Create a config dict based on the package location
    """
    conf_file = os.path.join(package_location, "conf", "package.yml")

    with open(conf_file, "r") as yaml_stream:
        try:
            config = yaml.safe_load(yaml_stream)
            config["package_path"] = package_location
            app_logger.info("Loaded \n %s", config)
            return config
        except yaml.scanner.ScannerError as scanner_error:
            # pylint: disable=C0301
            raise DatException(
                "Could not load the build configuration file. The following errors occured: \n{}\n Check your build file and try again !".format(
                    str(scanner_error)
                )
            ) from scanner_error
