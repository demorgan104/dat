import os
import yaml
from dat.errors.dat_exception import DatException


def get_package_config(package_location):
    conf_file = os.path.join(package_location, 'conf', 'package.yml')

    with open(conf_file, 'r') as yaml_stream:
        try:
            config = yaml.safe_load(yaml_stream)
            print("Loaded \n {}".format(config))
            return config
        except yaml.scanner.ScannerError as e:
            raise DatException(
                'Could not load the build configuration file. The following errors occured: \n{}\n Check your build file and try again !'
                .format(str(e)))


if __name__ == "__main__":
    print("Loading yaml file")
    get_package_config("/Users/timo/swd/packages_project/hello/")
