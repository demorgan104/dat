import os
from dat.core.conf_reader import get_package_config

class ReleaseApi(object):

    def __init__(self) -> None:
        super().__init__()
        self.current_dir = os.getcwd()

    def release(self):
        config = get_package_config(os.getcwd())

        print('releasing package {}'.format(
            config['name']
        ))
